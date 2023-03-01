import base64

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


class KeyDerivationError(Exception):
    pass


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


def encrypt_with_password(data: bytes, password: str) -> bytes:
    f = Fernet(make_key_from_password(password))
    encrypted_data = f.encrypt(data)
    return encrypted_data


def decrypt_with_password(data: bytes, password: str) -> bytes:
    f = Fernet(make_key_from_password(password))
    encrypted_data = f.decrypt(data)
    return encrypted_data
