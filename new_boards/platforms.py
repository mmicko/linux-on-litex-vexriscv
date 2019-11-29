import sys
import importlib

class Platforms:
    def __getattr__(self, name):
        if name == "__path__":
            return []
        for support in ["community"]:
            try:
                return importlib.import_module("new_boards." + support + ".platforms." + name)
            except ModuleNotFoundError:
                pass
        raise ModuleNotFoundError

sys.modules[__name__] = Platforms()
