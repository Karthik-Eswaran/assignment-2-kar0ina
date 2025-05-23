# assignment.py

import os
import importlib
from typing import Iterator, Any, List


def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(file_path: str, content: str) -> None:

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def list_files_in_directory(directory_path: str) -> List[str]:
    return [
        f for f in os.listdir(directory_path)
        if os.path.isfile(os.path.join(directory_path, f))
    ]


def generate_numbers(n: int) -> Iterator[int]:

    for i in range(n):
        yield i


def use_function_from_module(module_name: str, function_name: str, *args) -> Any:

    module = importlib.import_module(module_name)
    func = getattr(module, function_name)
    return func(*args)
