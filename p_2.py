# -*- coding: utf-8 -*-

'''1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
2. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и
поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
«Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для
каждого файла);
3. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение
данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
4. Проверить работу программы через вызов функции write_to_csv().'''

import os
import re
import csv

DIR = os.path.dirname(os.path.abspath(__file__))


def receive():
    data_dir = os.path.join(DIR, 'Студентам для решения домашнего задания')
    result = []
    source_files = [i for i in os.listdir(data_dir) if i.split('.')[1] == 'txt']

    for filename in source_files:
        filepath = os.path.join(data_dir, filename)

        with open(filepath,  encoding='WINDOWS-1251') as fl:
            for line in fl.readlines():
                result += re.findall(r'^(\w[^:]+).*:\s+([^:\n]+)\s*$', line)

    print(result)

    return result

def get_data():
    data = receive()
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    for item in data:
        os_prod_list.append(item[1]) if item[0] == main_data[0][0] else None
        os_name_list.append(item[1]) if item[0] == main_data[0][1] else None
        os_code_list.append(item[1]) if item[0] == main_data[0][2] else None
        os_type_list.append(item[1]) if item[0] == main_data[0][3] else None

    for i in range(len(os_prod_list)):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])

    print(main_data)

    return main_data


def write_to_csv(filepath):
    data = get_data()

    dir_, filename = os.path.split(filepath)

    os.makedirs(dir_, exist_ok=True)

    filepath = os.path.join(DIR, dir_, filename)

    with open(filepath, 'w', encoding='UTF-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)

        for line in data:
            writer.writerow(line)

    print(f'Данные сохранены в {filepath}')


if __name__ == '__main__':
    write_to_csv('Студентам для решения домашнего задания/report.csv')


print(33*'#', 'END TASK 1-4', 33*'#')


'''5. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать 
скрипт, автоматизирующий его заполнение данными. Для этого:
6. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;
7. Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.'''

import os
import json

DIR = os.path.dirname(os.path.abspath(__file__))


def write_order_to_json(item, quantity, price, buyer, date):
    filename = os.path.join(DIR, 'Студентам для решения домашнего задания', 'orders.json')

    if os.path.exists(filename):
        data = {}

        with open(filename, encoding="utf-8") as fl:
            data = json.loads(fl.read())

        data['orders'].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})

        with open(filename, "w", encoding="utf-8") as fl:
            json.dump(data, fl, indent=4, separators=(',', ': '), ensure_ascii=False)

        print(f'Данные добавлены в {filename}')

    else:
        print(f'Исходный файл по пути {filename} не найден')


if __name__ == '__main__':
    write_order_to_json('Смартфон OnePlus 6T 8/128GB', '1', '36500', 'Иванов Иван Иванович', '18.05.2019')
    write_order_to_json('Смартфон OnePlus 6 6/64GB', '1', '27990', 'Петров Петр Петрович', '17.06.2019')


print(33*'#', 'END TASK 5-7', 33*'#')


'''8. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле YAML-
формата. Для этого:
9. Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);
10. Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию
файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
11. Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.'''

import os
import yaml

DIR = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(DIR, 'Студентам для решения домашнего задания', 'file.yaml')
data = {
    'items': ['Notebook', 'PC', 'Notepad', 'NetTop'],
    'items_quantity': 4,
    'items_price': {
        'Notebook': '200€-1500€',
        'PC': '500€-5000€',
        'Notepad': '100€-500€',
        'NetTop': '100€-400€'
    }
}

with open(filename, 'w') as f_n:
    yaml.dump(data, f_n, default_flow_style=False, allow_unicode=True)

with open(filename) as f_n:
    print(f_n.read())

print(33*'#', 'END TASK 8-11', 33*'#')
