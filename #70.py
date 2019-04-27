
a = [[10, 13, 16, 5], [5, 14, 7, 4], [7, 18, 15, 15], [18, 10, 16, 12]]


def sort_row_column(a_list):
    print('!!')

    print("Исходный массив а: ", a)

    for i in range(a_list.__len__()):
        a_list[i].sort()
    print("Сортированный массив а: ", a)
    b = [[], [], [], []]
    for j in range(a.__len__()):
        for i in range(a.__len__()):
            b[j].append(a[i][j])
        b[j].sort()
    print("Полученный массив b: ", b)
    return b


p = []


def find_element(element, b_list):
    trigger = False
    for i in range(b_list.__len__()):
        for j in range(b_list[i].__len__()):
            if element == b_list[i][j]:
                p.append([i, j])
                trigger = True
    if trigger:
        return p
    else:
        print("Элемент не найден")


print("Что ищем?")
element = int(input())

b_list = sort_row_column(a)
print(find_element(element, b_list))
