# TODO Напишите функцию find_common_participants

def find_common_participants(group_1, group_2, sep=','):
    group_1 = group_1.split(sep)
    group_2 = group_2.split(sep)
    common = []
    for par in group_1:
        if par in group_2:
            common.append(par)

    common.sort()
    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, '|'))
