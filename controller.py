from view import *
from def_mod import *
import json

path_base = 'class_register.json'
# path_base = "path_base.json"

def ClickButton():
    
    dict_base = data_load(path_base)

    while True:
        choice = main_menu()
        if choice == '1':
            class_sub(dict_base)
            check = input('Для возврата нажмите Enter')
            pass
        elif choice == '2':
            pupil_sub(dict_base)
        elif choice == '3':
            print_all_pupil(dict_base)
            check = input('Для возврата нажмите Enter')
        elif choice == '4':
            if not class_sub(dict_base):
                sch_class, subject = class_sub(dict_base)
                pupil = input('Введите фамилию имя ученика: ')
                set_eval(dict_base, sch_class, subject, pupil)
                check = input('Для возврата нажмите Enter')
            else:
                pass
                check = input('Для возврата нажмите Enter')
        elif choice == '5':
            new_pupil = input('Введите фамилию имя ученика: ')
            sch_class = input('Введите класс: ')
            if sch_class in dict_base.keys():
                add_pupil(dict_base, sch_class, new_pupil)
                save_base(dict_base)
            else:
                print('Такого класса нет в базе')
            check = input('Для возврата нажмите Enter')
        elif choice == '6':
            sch_class = input('Введите класс: ')
            if sch_class in dict_base.keys():
                print_class_pupil(dict_base, sch_class)
                del_pupil = input('Введите фамилию имя ученика: ')
                if del_pupil in def_mod.dict_all_pupil(dict_base):
                    delete_pupil(dict_base, sch_class, del_pupil)
                    save_base(dict_base)
                else:
                    print('Такого ученика нет в классе')
            else:
                print('Такого класса нет в базе')
            check = input('Для возврата нажмите Enter')
        elif choice == '7':
            sch_class = input('Введите текущий класс ученика: ')
            if sch_class in dict_base.keys():
                print_class_pupil(dict_base, sch_class)
                chng_pupil = input('Введите фамилию имя ученика: ')
                if chng_pupil in def_mod.dict_all_pupil(dict_base):
                    new_class = input('Введите новый класс ученика: ')
                    add_pupil(dict_base, new_class, chng_pupil)
                    delete_pupil(dict_base, sch_class, chng_pupil)
                    save_base(dict_base)
                else:
                    print('Такого ученика нет в классе')
            else:
                print('Такого класса нет в базе')
            check = input('Для возврата нажмите Enter')
        elif choice == '8':
            exit()


