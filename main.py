# 1.1. Разработать программу с реализацией функции для считывания json- данных из файла и вывод их в табличном виде на экран. Реализовать базовый синтаксис для обработки исключений (try .. except)
#1.2. Дополнение программы для считывания данных проверкой утверждений или высказываний (assert). Создание отдельного блока для такой проверки (с помощью __name__) и скрипта командной строки для запуска этих проверок.
#1.3. Дополнение программы для считывания данных с использованием менеджера контекстов и реализации расширенного синтаксиса для обработки исключений.
#1.4. Формирование отчета по практическому заданию и публикация его в портфолио.

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