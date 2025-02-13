tuple1=(1,2,3,4,5,6,7,8,9,10)
res=-1
for i in range(10):
    res+=1
    print(tuple1[res])



def no_duplicates(user_list):
    return list(set(user_list))

list1=[1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ]
list2=[22,11,22,13,]
list3=['hello', "hello", 2, True, 10>1]
no_duplicates(list1)
no_duplicates(list2)
no_duplicates(list3)

