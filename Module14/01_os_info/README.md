## Задача 1. Информация о системе
### Что нужно сделать
Соберите информацию об операционной системе и версии Python. Скопируйте код ниже в main.py и запустите. Так преподавателям будет проще помочь вам, если возникнут ошибки.

```python
import platform
import sys

info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(),
    sys.version,
    platform.architecture(),
)
print(info)

with open('os_info.txt', 'w', encoding='utf8') as file:
    file.write(info)
```
### Что оценивается
- Создан файл «os_info.txt» с информацией об операционной системе и версии Python.
