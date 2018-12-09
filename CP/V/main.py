# 1.3. Создание программы для считывания данных формата CSV c использованием функционала модуля contextlib.

import csv
from prettytable import PrettyTable 
from contextlib import contextmanager

@contextmanager
def openfile(file):
    try:
        data = open(file, 'r')
        yield data
    except OSError:
        print("Произошла ошибка при открытии файла")
        exit(0)
 
def read_titanic_csv(f):
    x = PrettyTable()
    read = csv.reader(f)
    x.field_names = next(read)
    for row in read:
        a =[]
        for item in row:
          a.append(item)
        x.add_row(a)
    print(x)
    with open('titanic_table.txt', 'w') as f:
      f.write(x.get_string())

if __name__ == "__main__":
  with openfile('titanic.csv') as f_obj:
        read_titanic_csv(f_obj)