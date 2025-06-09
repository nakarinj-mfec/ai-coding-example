import importlib.util
import os


for file_path in ['01_implement.py', '02_improve.py', '03_refactor.py']:
    file_path = os.path.join(os.path.dirname(__file__), '..', 'code', file_path)
    spec = importlib.util.spec_from_file_location("module.name", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)