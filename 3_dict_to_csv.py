"""
Домашнее задание №2
Работа csv
1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv
"""
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('students.csv', 'r', encoding = 'utf-8') as f:
        fields = ['name', 'age', 'job']   
        reader = csv.DictReader(f, fields, delimiter = ',')
        readers = []
        for row in reader:
            readers.append(row)
        print(readers)
    with open('new_students.csv', 'w', encoding = 'utf-8', newline = '') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter = ',')
        writer.writeheader
        for person in readers:
            writer.writerow(person) 
if __name__ == "__main__":
    main()
