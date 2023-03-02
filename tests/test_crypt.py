from pystash import crypt


def test_make_key():
    crypt.Crypt.make_key_from_password("test")


def test_encrypt_and_decrypt():
    data = b"bonk"
    password = "insecure"

    encrypted_data = crypt.Crypt.encrypt_with_password(data, password)
    assert crypt.Crypt.decrypt_with_password(encrypted_data, password) == data


def test_set_and_check_key(tmp_path):
    c = crypt.Crypt(tmp_path)
    c.record_key_hash(b"bonk")
    assert c.check_key_hash(b"bonk")


def test_set_and_check_wrong_key(tmp_path):
    c = crypt.Crypt(tmp_path)
    c.record_key_hash(b"bonk")
    assert not c.check_key_hash(b"donk")
