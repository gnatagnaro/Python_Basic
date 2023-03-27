from typing import Any


class File:
    """Контекст-менеджер, создающий и открывающий любой файл в режиме записи или чтения."""
    def __init__(self, file_name: str, mode: str) -> None:
        self._file_name = file_name
        self._mode = mode
        self._file = None

    @property
    def file_name(self) -> str:
        return self._file_name

    @file_name.setter
    def file_name(self, value: str) -> None:
        self._file_name = value

    @property
    def mode(self) -> str:
        return self._mode

    @mode.setter
    def mode(self, value: str) -> None:
        self._mode = value

    def __enter__(self) -> Any:
        try:
            self._file = open(self._file_name, self._mode, encoding='utf8')
        except FileNotFoundError:
            self._file = open(self._file_name, 'w', encoding='utf8')
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if self._file:
            self._file.close()
        return True


with File("example.txt", "r") as file:
    file.write("Всем привет!")

