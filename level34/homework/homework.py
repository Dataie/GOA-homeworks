def greeting():
    print("Hello world")

def sum(num1,num2):
    print(num1+num2)

# def multiply_by_10(num1):
#     print(num1*10)

# user_num=int(input("Enter your number here: "))
# multiply_by_10(user_num)

# def greeting1(name="Guest"):
#     print(f"Greetings {name}")
# username=input("Enter your name here: ")
# greeting1(username)

def outer_function():
    print("This is the outer function.")
    def inner_function():
        print("This is the inner function.")
    inner_function()
outer_function()

def even_or_odd(num1):
    if num1%2==0:
        print(f"The number {num1} is even")
    else:
        print(f"The number {num1} is odd")

def max_number(list1):
    max=0
    for i in list:
        if i>max:
            max=i
    print(f"The max number is {max}")
list=[12, 321, 22, 654]
max_number(list)

def positive_list(list):
    new_list=[]
    for i in list:
        if i>0:
            new_list.append(i)
    print(new_list)
list1=[123, -21, 0, -31, 234, 423]
positive_list(list1)


def sum(range1):
    res=0
    for i in range(range1):
        if i%3==0:
            res+=i
    print(res)
sum(100)