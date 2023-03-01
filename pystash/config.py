import os
import pathlib
import appdirs

def get_default_store_root() -> pathlib.Path:
    app_data_dir = pathlib.Path(appdirs.user_data_dir("pystash", "bda"))
    return str(app_data_dir / "secrets")

STORE_ROOT = os.environ.get("PYSTASH_ROOT", get_default_store_root())
