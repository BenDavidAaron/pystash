from pystash import store

import pytest


def test_cache_put_and_get(tmp_path):
    """Add and fetch an item"""
    s = store.Store(tmp_path)
    s["nevada"] = "Carson City"
    assert s["nevada"] == "Carson City"


def test_cache_put_get_and_del(tmp_path):
    """Delete and fail to fetch an item"""
    s = store.Store(tmp_path)
    s["nevada"] = "Carson City"
    assert s["nevada"] == "Carson City"
    del s["nevada"]
    with pytest.raises(KeyError):
        # pylint: disable=pointless-statement
        s["nevada"]
