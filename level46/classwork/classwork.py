def manual_list(start, end, step, user_num):
    return (i for i in range(start, end, step) if i>user_num)
manual_list(10, 20 ,2, 3)
manual_list(1, 3, 1, 4)
manual_list(29, 50, 4, 15)


list1=[i for i in range(1, 101) if (i%3==0 or i%5==0) and i%15!=0]
print(list1)

list2=[i for i in range(10, 201) if str(i)[::-1]==str(i)]
print(list2)