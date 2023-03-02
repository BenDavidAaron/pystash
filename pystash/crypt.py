import base64
import hashlib
import pathlib
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class KeyDerivationError(Exception):
    pass


class Crypt:
    def __init__(self, dir_root: pathlib.Path):
        self.dir = pathlib.Path(dir_root) / "crypt"
        self.__prep_dir()

    def __prep_dir(self):
        self.dir.resolve().mkdir(parents=True, exist_ok=True)

    def record_key_hash(self, key: bytes):
        m = hashlib.sha256()
        m.update(key)
        with (self.dir / "key").open("wb") as f:
            f.write(m.digest())

    def check_key_hash(self, key: bytes):
        m = hashlib.sha256()
        m.update(key)
        with (self.dir / "key").open("rb") as f:
            disk_digest = f.read()
        return disk_digest == m.digest()

    def exists(self) -> bytes:
        return (self.dir / "key").exists()

    def clear(self):
        with (self.dir / "key").open("wb") as f:
            f.write(os.urandom(1024))
        (self.dir / "key").unlink()

    @staticmethod
    def make_key_from_password(password: str) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            iterations=69420,
            salt=b"NotSecureDoNotUse",
        )
        key = base64.urlsafe_b64encode(kdf.derive(bytes(password, encoding="utf-8")))
        try:
            Fernet(key)
        except ValueError as exc:
            raise KeyDerivationError from exc
        return key

    @staticmethod
    def encrypt_with_password(data: bytes, password: str) -> bytes:
        f = Fernet(Crypt.make_key_from_password(password))
        encrypted_data = f.encrypt(data)
        return encrypted_data

    @staticmethod
    def decrypt_with_password(data: bytes, password: str) -> bytes:
        f = Fernet(Crypt.make_key_from_password(password))
        encrypted_data = f.decrypt(data)
        return encrypted_data
