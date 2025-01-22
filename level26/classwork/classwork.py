def greet(name):
    print("გამარჯობა",name)
greet("დათა")

def manual_range(start,end,step):
    for i in range(start,end,step):
        if i%2==0:
            print(i)
        else:
           print("Not an even number")
manual_range(34,65,4)
manual_range(10,86,3)
manual_range(30,75,2)
manual_range(2,6,1)
manual_range(15,56,7)



def manual_len(list):
    count = 0  
    for item in list:  
        count += 1  
        print(count)
my_list = [1, 2, 3, 4, 5]
manual_len(my_list)

