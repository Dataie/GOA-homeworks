list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num1=int(input("Enter number: "))
if num1>=0 and num1< 10:
    print(list[num1])
elif num1>=-10 and num1<=-1:
    print(list[num1])
else:
    print("wrong index")

list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for i in list1:
    print(i*2)
    print(i/2)