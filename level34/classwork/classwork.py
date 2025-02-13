def deleting(main_list, indexes_list):
    for i in indexes_list:
        main_list.pop(i)
        print(main_list)
deleting([1, 2, 3, 4, 5, 6,] [2, 4, 3])


def remove_one_element(list, index):
    list.pop(index)
    print(list)

remove_one_element([1, 2, 3, 4, 5, 6, 7], [7])

