from pystash import crypt


def test_make_key():
    crypt.Crypt.make_key_from_password("test")


def test_encrypt_and_decrypt():
    data = b"bonk"
    password = "insecure"

    encrypted_data = crypt.Crypt.encrypt_with_password(data, password)
    assert crypt.Crypt.decrypt_with_password(encrypted_data, password) == data
