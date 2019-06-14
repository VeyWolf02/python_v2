'''Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и
также проверить тип и содержимое переменных.'''

str_1 = 'разработка'
str_2 = 'сокет'
str_3 = 'декоратор'

print(str_1)

print('тип переменной:', format(type(str_1)))
print('содержание переменной:', format(str_1))
print('длинна строки:', format(len(str_1)))

print(str_2)

print('тип переменной:', format(type(str_2)))
print('содержание переменной:', format(str_2))
print('длинна строки:', format(len(str_2)))

print(str_3)

print('тип переменной:', format(type(str_3)))
print('содержание переменной:', format(str_3))
print('длинна строки:', format(len(str_3)))

#из конвертера:

words = [b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
       b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82',
       b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80']

for line in words:
    print('тип переменной:', format(type(line)))
    print('содержание переменной:', format(line))
    print('длинна строки:', format(len(line)))


print(33*'#', 'END TASK 1', 33*'#')


'''Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов 
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.'''

words = [b'class', b'function', b'method']

for line in words:
    print('тип переменной:', format(type(line)))
    print('содержание переменной:', format(line))
    print('длинна строки:', format(len(line)))


print(33*'#', 'END TASK 2', 33*'#')


'''Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.'''

words_1 = b'attribute'

'''words_2 = b'класс'

words_2 = b'класс'
             ^
SyntaxError: bytes can only contain ASCII literal characters.'''

'''words_3 = b'функция'

words_3 = b'функция'
             ^
SyntaxError: bytes can only contain ASCII literal characters.'''

words_4 = b'type'


print(33*'#', 'END TASK 3', 33*'#')


'''Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
 и выполнить обратное преобразование (используя методы encode и decode).'''

words = ['разработка', 'администрирование', 'protocol', 'standard']

for line in words:
    en_line = line.encode('utf-8')
    print(en_line, type(en_line))

    de_en_line = bytes.decode(en_line, 'utf-8')
    print(de_en_line, type(de_en_line))


print(33*'#', 'END TASK 4', 33*'#')


'''Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип
на кириллице.'''

import subprocess

ping_res = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for ping in ping_res:

    ping_proc = subprocess.Popen(ping, stdout=subprocess.PIPE)

    for line in ping_proc.stdout:

        print(line)
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))
        break


print(33*'#', 'END TASK 5', 33*'#')


'''Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
 Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.'''

import locale

words = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w+') as file:
    for line in words:
        file.write(line + '\n')
    file.seek(0)

print(file)

file_coding = locale.getpreferredencoding()

with open('test_file.txt', 'r', encoding=file_coding) as file:
    for line in file:
        print(line)

    file.seek(0)
    

print(33*'#', 'END TASK 6', 33*'#')






