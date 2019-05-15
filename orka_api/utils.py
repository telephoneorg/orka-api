import importlib


def relative_import(path, relative_to_path=None):
    return importlib.import_module(path, relative_to_path)
