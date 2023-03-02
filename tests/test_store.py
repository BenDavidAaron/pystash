import pytest

from pystash import store


def test_cache_put_and_get(tmp_path):
    """Add and fetch an item"""
    s = store.Store(tmp_path)
    s["nevada"] = b"Carson City"
    assert s["nevada"] == b"Carson City"


def test_cache_put_get_and_del(tmp_path):
    """Delete and fail to fetch an item"""
    s = store.Store(tmp_path)
    s["nevada"] = b"Carson City"
    assert s["nevada"] == b"Carson City"
    del s["nevada"]
    with pytest.raises(KeyError):
        # pylint: disable=pointless-statement
        s["nevada"]
