import pandas as pd        # импорт библиотеки pandas
#from datetime import datetime as dt # импорт библиотеки datetime для работы с временем
import pprint              # продвинутая версия print в Python

from operator import itemgetter
           #создает функцию, которая принимает итерируемый объект
           # (список, кортеж, множество) и возвращает n-элемент из него.

# прочитаем Excel файл и создадим из него pandas dataframe, читаем страницу 'Sheet1'
all_spisok_df = pd.read_excel('Список работников.xls',sheet_name='Лист1')

# чтобы преобразовать dataframe в словарь, в pandas есть замечательный метод,
# который так и называется “to_dict”,
# кроме того, устанавливаем индекс - ключ как 'ФИО'
all_spisok_wokers = all_spisok_df.set_index('ФИО').to_dict('index')

def update_dictionary(d, key, value):  # объявление функции добавления
                                       # работника в список (СЛОВАРЬ)
    if key in d:  # если ключ - фамилия есть в словаре
        print(f'Такая фамилия уже есть в словаре')
    if key not in d:  # если ключа-фамилии нет в словаре
        d[key] = {'Должность':'value'}  # добавление в словарь пары - фамилия: должность
    return


def del_name_dictionary(d, key):  # объявление функции удаления
                                  # работника из списка (СЛОВАРЯ)
    if key in d:  # если ключ - фамилия есть в словаре
        del d[key]  # удаление пары ФИО - должность
    if key not in d:  # если ключа - фамилии нет в словаре
        print('Такого сотрудника в словаре нет')


# Блок корректироки информации о сотрудниках
def check_all_spisok():
    print("Внести информацию о новом сотруднике в базу, введите 1")
    print("Удалить информацию о сотруднике в базе, введите 2")
    i = int(input())
    if i == 1:
        print('Введите фамилию работника и его должность')
        key = input()
        value = input()
        update_dictionary(all_spisok_wokers, key, value) # вызов функции добавления
                                                 # работника в СЛОВАРЬ
    elif i == 2:
        print('Введите фамилию работника')
        key = input()
        del_name_dictionary(all_spisok_wokers, key)  # вызов функции удаления
                                                     # рабоьника из СЛОВАРЯ
        #sort_dictionary(all_spisok_wokers)  # вызов функции сортировки СЛОВАРЯ по алфавиту
    else:
        return

check_all_spisok()


# превращаем словарь обратно в pandas dataframe
all_spisok_1 = pd.DataFrame(all_spisok_wokers)
all_spisok_1.to_excel('Список работников1.xls') # запись в файл