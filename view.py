import def_mod
from os import system

def main_menu():
    system('cls')
    print('1. Показать оценки класа по предмету')
    print('2. Показать оценки ученика по предметам')
    print('3. Показать всех учеников школы')
    print('4. Поставить оценку ученику')
    print('5. Добавить ученика в журнал')
    print('6. Удалить ученика из журнала')
    print('7. Сменить класс ученику')
    print('8. Выход')

    menu = input('Выберите пункт меню: ')
    return menu

def class_sub(dict_base):
    system('cls')
    print(f'Доступные классы: {def_mod.give_class(dict_base)}')
    sch_class = input('Введите класс: ')
    if sch_class not in def_mod.give_class(dict_base):
        print('Такого класса нет в базе')
        return False, False
    else:
        print(f'Доступные предметы: {def_mod.give_subject(dict_base, sch_class)}')
        subject = input('Введите предмет: ')
        if subject not in def_mod.give_subject(dict_base, sch_class):
            print('Такого предмета нет в базе')
            return False, False
        else:
            def_mod.print_register(dict_base, sch_class, subject)
            return sch_class, subject
        

def pupil_sub(dict_base):
    pupil = input('Введите фамилию имя ученика или нажмите ввод для выхода в основное меню: ')
    if pupil != "":
        pupil_dict, current_class = def_mod.find_pupil(dict_base, pupil)
        if current_class != "":
            system('cls')
            print(f'Ученик(-ца) {pupil} {current_class} класс:')
            print(f'Предмет {" "*15} Оценки {" "*15} Средняя оценка')
            for key, val in sorted(pupil_dict.items()):
                a = ' '.join(val.split(','))
                b = list(map(int, val.split(',')))
                print(f'{key}  {" "*(20 - len(key))}  {a} {" "*15} {sum(b)/len(b)}')
        else:
            print('Такого ученика нет в базе')
    else:
        return False
    pupil_sub(dict_base)

def print_all_pupil(dict_base):
    all_pupil = def_mod.dict_all_pupil(dict_base)
    system('cls')
    print(f'Ученик(-ца) {" "*15} номер класса:')
    for key, val in sorted(all_pupil.items()):
        print(f'{key}  {" "*(24 - len(key))}  {val}')

def set_eval(dict_base, sch_class, subject, pupil):
    eval = dict_base.get(sch_class).get(subject).get(pupil)
    print(eval)
    new_eval = input(f'Введите оценку ученик {pupil} предмет {subject}: ')
    if eval != None:
        sum_eval = eval + ',' + new_eval
    else:
        sum_eval = new_eval
    dict_base.get(sch_class).get(subject)[pupil] = sum_eval
    final_eval = dict_base.get(sch_class).get(subject).get(pupil)
    def_mod.print_register(dict_base, sch_class, subject)
    def_mod.save_base(dict_base)
    pass

def print_class_pupil(dict_base, sch_class):
    for subject, pupil in dict_base.get(sch_class).items():
        list_pupil = pupil.keys()
        break
    print(f'Ученики {sch_class} класса:')
    print('\n'.join(map(str, list_pupil)))










    