### Инвариантне задание
#### 1.1. Разработать программу с реализацией функции для считывания json- данных из файла и вывод их в табличном виде на экран. Реализовать базовый синтаксис для обработки исключений (try .. except)
#### 1.2. Дополнение программы для считывания данных проверкой утверждений или высказываний (assert). Создание отдельного блока для такой проверки (с помощью __name__) и скрипта командной строки для запуска этих проверок.
#### 1.3. Дополнение программы для считывания данных с использованием менеджера контекстов и реализации расширенного синтаксиса для обработки исключений.
#### 1.4. Формирование отчета по практическому заданию и публикация его в портфолио.

Дан JSON-файл - [Guest_book.json](https://github.com/python-advance/sem5-exceptions-Bolzuka/blob/master/CP/Guest_book.json "Guest_book.json" )


Импортируем JSON
Создаем функцию для считывания json- данных из файла с обработкой исключений (ошибка может возникнуть при попытки открытия файла)
Дополняем программу для считывания данных с использованием менеджера контекстов
Затем, для элементов из списка значений, помещаем ключи элементов в дополнительные списки
Используем библиотеку PrettyTable, чтобы создать таблицу с элементами

```
import json
from prettytable import PrettyTable

Guest_book ='Guest_book.json'

def read(Guest_book):
  try:
        file_book = open(Guest_book, 'r') 
        data = json.loads(file_book.read())
  except FileNotFoundError:
        print ("Файл не найден!")
  except Exception:
        print("Произошла неизвестная ошибка")

  with open(Guest_book, 'r') as f:
     data = json.loads(f.read())

  name = []
  surname = []
  for i in range(len(data["Guests"])):
    name.append(data["Guests"][i]["Guest name"])
    surname.append(data["Guests"][i]["Guest surname"])
  
  x = PrettyTable()
  column_names = ['Guest name', 'Guest surname']
  x.add_column(column_names[0], name)
  x.add_column(column_names[1], surname)
  print(x)
  return len(data["Guests"]) 

read('Guest_book.json')
```
Ввод в консоли: 

![Скрин](https://github.com/python-advance/sem5-exceptions-Bolzuka/blob/master/CP/скрин.png "Скрин")



Создаем pytest в отдельном файле, импортируем библиотеку и наш файл
Вывод - возвращаем количество элементов из списка в JSON-файле

```
import pytest
import main

def test_guestbook():
  assert main.read('Guest_book.json') == 3
```

Чтобы запустить все тесты необходимо ввести в консоли:
```
python -m pytest
```
Чтобы найти и запустить тесты в указанном файле необходимо ввести в консоли:
```
python -m pytest -q main.py
```
(Важно) Имя теста должно начинаться с test_* для поиска пакетов

Ввод и вывод в консоли: 

![Тесты скрин](https://github.com/python-advance/sem5-exceptions-Bolzuka/blob/master/CP/тесты_скрин.png "Тесты скрин")

