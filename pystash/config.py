import os
import pathlib
import appdirs


def get_default_root_path() -> str:
    app_data_dir = pathlib.Path(appdirs.user_data_dir("pystash", "bda"))
    return str(app_data_dir)

ROOT_PATH = os.environ.get("PYSTASH_ROOT", get_default_root_path())


