""" Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов.
"""


def repeating_elements(list_1):
    list_2 = [None]
    for elem in list_1:
        if (list_1.count(elem) > 1) and not list_2.count(elem):
            list_2.append(elem)
    return list_2


my_list = [2, 4, 6, 4, 2, 8, 10, 4, 2, 12, 14, 8, 12, 2, 16, 10, 10, 18]
print(repeating_elements(my_list))
 

