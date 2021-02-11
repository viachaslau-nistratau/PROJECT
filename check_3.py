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


def random_check_timesheet(d):  # объявление функции
    #print(f'Проверка табеля {d}') # Ерунда какая-то... Как вывести название табеля?
    all_day = 0
    all_count_sick_list = 0 # Подсчет количества дней по больничному в табеле
    for key, value in d.items():
        count_sick_list = 0
        for i in value: # цикл проверки на количество больничных дней
            if i == 'Б':
                count_sick_list += 1
        if count_sick_list > 0:
            print('У работника {0} ' f'{count_sick_list} больничных дней'.format(key))
        all_count_sick_list = all_count_sick_list + count_sick_list
    print(f'ВСЕГО в этом месяце по табелю {all_count_sick_list} больничных дней')

    all_count_day_off = 0 # подсчет количества выходгых дней в табеле
    for key, value in d.items():
        count_day_off = 0
        for i in value: # цикл проверки на количество выходных дней
            if i == 'В':
                count_day_off += 1
        if count_day_off > 0:
            print('У работника {0} ' f'{count_day_off} выходных дней'.format(key))
        else:
            print('У работника {0} выходных дней не было'.format(key))
        all_count_day_off = all_count_day_off + count_day_off
    print(f'ВСЕГО в этом месяце по табелю {all_count_day_off} выходных дней')

    all_count_holiday = 0 # подсчет количества отпускных дней в табеле
    for key, value in d.items():
        count_holiday = 0
        for i in value: # цикл проверки на количество отпускных дней
            if i == 'О':
                count_holiday += 1
        if count_holiday > 0:
            print('У работника {0} ' f'{count_holiday} дней  отпуска'.format(key))
        all_count_holiday = all_count_holiday + count_holiday
    print(f'ВСЕГО в этом месяце по табелю {all_count_holiday} дней отпуска')

    all_count_truancy = 0 # подсчет количества прогулов
    for key, value in d.items():
        count_truancy = 0
        for i in value: # цикл проверки на количество прогулов
            if i == 'П':
                count_truancy += 1
        if count_truancy > 0:
            print('У работника {0} ' f'{count_truancy} дней прогулов'.format(key))
        all_count_truancy = all_count_truancy + count_truancy
    print(f'ВСЕГО в этом месяце по табелю {all_count_truancy} дней прогулов')

    all_count_at_own_expense = 0 # подсчет количества дней за свой счет
    for key, value in d.items():
        count_at_own_expense = 0
        for i in value: # цикл проверки на количество дней за свой счет
            if i == 'А':
                count_at_own_expense += 1
        if count_at_own_expense > 0:
            print('У работника {0} ' f'{count_at_own_expense} дней за свой счет'.format(key))
        all_count_at_own_expense = all_count_at_own_expense + count_at_own_expense
    print(f'ВСЕГО в этом месяце по табелю {all_count_at_own_expense} дней за свой счет')

    all_count_other_days = 0 # подсчет количества дней (военкомат, суд)
    for key, value in d.items():
        count_other_days = 0
        for i in value: # цикл проверки на количество дней (военкомат, суд)
            if i == 'Г':
                count_other_days += 1
        if count_other_days > 0:
            print('У работника {0} ' f'{count_other_days} дней (военкомат, суд)'.format(key))
        all_count_other_days = all_count_other_days + count_other_days
    print(f'ВСЕГО в этом месяце по табелю {all_count_other_days} дней (военкомат, суд)')

    all_count_mother_day = 0 # подсчет количества "материнских дней" в табеле
    for key, value in d.items():
        count_mother_day = 0
        for i in value: # цикл проверки на количество "материнских дней"
            if i == 'Д':
                count_mother_day += 1
        if count_mother_day > 0:
            print('У работника {0} ' f'{count_mother_day} материнских дней'.format(key))
        all_count_mother_day = all_count_mother_day + count_mother_day
    print(f'ВСЕГО в этом месяце по табелю {all_count_mother_day} материнских дней')

    all_count = 0     # общее количество отработанных дней в табеле
    all_count_sum = 0 # общее количество отработанных часов в табеле
    for key, value in d.items():
        count_8 = 0   # 8-ми часовой рабочий день
        count_7 = 0   # 7-ми часовой рабочий день (предпраздничный)
        count_sum = 0 #
        for i in value: # цикл подсчета рабочих дней и отработанных часов
            if i == 8:
                count_8 += 1
            elif i == 7:
                count_7 += 1
        count = count_8 + count_7
        count_sum = (count_8 * 8) + (count_7 * 7)
        print('У работника {0} ' f'{count} рабочих дней, {count_sum} рабочих часов'.format(key))
        all_count = all_count + count
        all_count_sum = all_count_sum + count_sum
    print(f'В этом месяце {all_count} рабочих дней и {all_count_sum} рабочих часов')
    all_day = all_count_sick_list + all_count_day_off + all_count_holiday + all_count_truancy + all_count_at_own_expense + all_count_other_days + all_count_mother_day + all_count
    print(f'ВСЕГО по табелю {all_day} человеко-дней')

check_dictionary(sotrudnik)
random_check_timesheet(sotrudnik)
check_dictionary(sotrudnik_1)
random_check_timesheet(sotrudnik_1)
