import pathlib


class Store:
    def __init__(self, dir_root: pathlib.Path):
        self.dir_root = pathlib.Path(dir_root)
        self.__init_dir()

    def __init_dir(self):
        self.dir_root.resolve().mkdir(parents=True, exist_ok=True)

    def get(self, key: str):
        raise NotImplementedError

    def put(self, key: str, val: bytes):
        raise NotImplementedError

    def delete(self, key: str):
        raise NotImplementedError

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, val):
        return self.put(key, val)

    def __delitem__(self, key):
        return self.delete(key)
