import json

def data_load(path):
    with open(path, 'r', encoding='UTF-8') as dict_eval:
        templates = {}
        templates = json.load(dict_eval)
        return templates

def print_register(dict_base, class_num, subject):
    print(f'Журнал: {class_num} предмет: {subject}')
    print(f'ФИО ученика {" "*15} Оценка {" "*15} Средняя оценка')
    class_reg = dict_base.get(class_num)
    class_sub = class_reg.get(subject)
    for key, val in sorted(class_sub.items()):
        if val != None:
            a = ' '.join(val.split(','))
            b = list(map(int, val.split(',')))
            print(f'{key}  {" "*(24 - len(key))}  {a} {" "*(22- len(a))} {sum(b)/len(b)}')
        elif val == None:
            print(f'{key}  {" "*(24 - len(key))}   {" "*14}')

def give_class(dict_base):
    sch_class = ", ".join(list(dict_base.keys()))
    return sch_class

def give_subject(dict_base, sch_class):
    subject = ", ".join(list(dict_base.get(sch_class).keys()))
    return subject

def find_pupil(dict_base, pupil):
    pupil_dict = {}
    current_class = ""
    for num_class, sch_class in dict_base.items():
        for subject, val in sch_class.items():
            if val.get(pupil) != None:
                pupil_dict[subject] = val.get(pupil)
                current_class = num_class
    return pupil_dict, current_class

def dict_all_pupil(dict_base):
    all_pupil = {}
    for num_class, sch_class in dict_base.items():
        for pupil, val in sch_class.items():
            for el in val.keys():
                all_pupil[el] = num_class
    return all_pupil

def save_base(dict_base):
    with open('path_base.json', 'w', encoding='UTF-8') as file_base:
        json.dump(dict_base, file_base, ensure_ascii=False)

def add_pupil(dict_base, sch_class, new_pupil):
    for el, val in dict_base.get(sch_class).items():
        val.setdefault(new_pupil)

def delete_pupil(dict_base, sch_class, del_pupil):
    for el, val in dict_base.get(sch_class).items():
        val.pop(del_pupil)


