import pathlib
import os


class Store:
    def __init__(self, dir_root: pathlib.Path):
        self.dir_root = pathlib.Path(dir_root)
        self.__init_dir()

    def __init_dir(self):
        self.dir_root.resolve().mkdir(parents=True, exist_ok=True)

    def get(self, key: str) -> bytes:
        try:
            with (self.dir_root / key).open("rb") as f:
                return f.read()
        except FileNotFoundError as exc:
            raise KeyError from exc

    def put(self, key: str, val: bytes) -> None:
        with (self.dir_root / key).open("wb") as f:
            f.write(val)

    def delete(self, key: str) -> None:
        with (self.dir_root / key).open("wb") as f:
            f.write(os.urandom(1024))
        (self.dir_root / key).unlink()

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, val):
        return self.put(key, val)

    def __delitem__(self, key):
        return self.delete(key)
