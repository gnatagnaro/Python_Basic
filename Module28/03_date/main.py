class Date:
    """Класс, проверяющий числа даты на корректность и
    конвертирующий строку даты в объект класса Date."""
    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self._day = day
        self._month = month
        self._year = year

    def __str__(self) -> str:
        return f'День: {self._day}\tМесяц: {self._month}\tГод: {self._year}\t'

    @classmethod
    def from_string(cls, value: str) -> 'Date':
        # dmy_list = date.split('-')
        # day, month, year = int(dmy_list[0]), int(dmy_list[1]), int(dmy_list[2])
        day, month, year = map(int, value.split('-'))
        date_obj = cls(day, month, year)
        return date_obj

    @classmethod
    def is_date_valid(cls, value: str) -> bool:
        # dmy_list = date.split('-')
        # day, month, year = int(dmy_list[0]), int(dmy_list[1]), int(dmy_list[2])
        day, month, year = map(int, value.split('-'))
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
