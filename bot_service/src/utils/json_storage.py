from typing import Any, Self
import json
import os

from src.utils.dot_dict import DotDict


class JsonStorage:
    __flyweight : dict[str, Self] = {}

    def __new__(cls, storage_path: str = 'config/jsons') -> Self:
        if storage_path not in cls.__flyweight.keys():
            instance = super().__new__(cls)
            cls.__flyweight[storage_path] = instance
        return cls.__flyweight[storage_path]

    def __init__(self, storage_path: str = 'config/jsons') -> None:
        cwd = os.getcwd()
        self.__storage_path = os.path.join(cwd, storage_path)
        files = os.listdir(self.__storage_path)
        self.__json_files = [file for file in files if file.endswith('.json')]
        self.__storage = None
        self.reload_storage()

    @property
    def storage(self) -> dict[str, Any]:
        return self.__storage

    def format(self, string: str) -> str:
        return string.format(storage=self.storage)

    def format_object(self, object: dict) -> dict[str, Any]:
        return {
            key: self.format_object(value)
            if isinstance(value, dict) else self.format(value) for key, value in object.items()
        }

    def reload_storage(self) -> dict[str, Any]:
        self.__storage = DotDict({})
        for json_file in self.__json_files:
            with open(os.path.join(self.__storage_path, json_file), 'r') as file:
                file_name, _file_ext = os.path.splitext(json_file)
                data = {file_name: json.load(file)}
                self.__storage.update(data)
