# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re

subject = {}
with open("data/hw_06.txt", encoding="utf-8") as temp_file:
    for el in temp_file:
        sub_name, lectures, practice, lab = el.split()
        temp_num = re.findall(r"[-+]?\d*\.\d+|\d+", el)
        temp_num = [int(item) for item in temp_num]
        subject[sub_name] = sum(temp_num)

    print(subject)

