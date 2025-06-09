import importlib.util
import os

def import_module(module_name: str, file_name: str):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'code', file_name)
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module