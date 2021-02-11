sotrudnik = { #табель сотрудников, словарь с ключом - ФИО
}
sotrudnik_1 = { #табель сотрудников, словарь с ключом - ФИО
}

def check_dictionary(d):  # объявление функции
    #print(f'Проверка табеля {d}') # Ерунда какая-то... Как вывести название табеля?
    for key, value in d.items():
        count_workers = len(d) # Количество работников в табеле
        count_all_day = len(value) - 1 # Количество дней в месяце
        count_workers_day = count_workers * count_all_day # Количество человеко-дней
    print(f'количество работников в табеле - {count_workers}')
    print(f'Количество дней в месяце - {count_all_day}')
    print(f'Количество человеко-дней в месяце {count_workers_day}')

    for key, value in d.items():
        count_zero = 0
        for i in value:  # цикл проверки на незаполненные клетки строки табеля
            if i == 0 or i == '':
                count_zero += 1
        if count_zero > 0:
            print('ВНИМАНИЕ. У работника {0} ' f'в табеле не заполнено {count_zero} полей'.format(key))
        #else:
            #print('Все в порядке, у работника {0} в табеле пропусков нет'.format(key))

    for key, value in d.items():
        count_other_timesheet = 0
        for i in value:  # цикл проверки на количество дней указанных в другом табеле
            if i == 'Т':
                count_other_timesheet += 1
        if count_other_timesheet > 0:
            print('ВНИМАНИЕ. У работника {0} ' f'{count_other_timesheet} дней в другом табеле'.format(key))

check_dictionary(sotrudnik)
check_dictionary(sotrudnik_1)