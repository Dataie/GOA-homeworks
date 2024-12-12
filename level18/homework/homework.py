num1=int(input("Enter number here: "))
num2=int(input("Enter number here: "))
if num1>num2:
    print(num1)
else:
    print(num2)


num1=int(input("Enter number here: "))
if num1%2 == 0:
    print("The number is even")
else:
    print("The number is odd")


num1=int(input("Enter number here: "))
if num1<0:
    print("The number is negative")
else:
    print("The number is positive")


num1=int(input("Enter number here: "))
if num1%5==0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")


for i in range(5):
    num1=int(input("Enter number here: "))
    if num1%2==0:
        print("The number is even")
    else:
        print("The number is odd")


correct_password=("Goa best")
user_guess=input("Enter the password here: ")
count=0
while user_guess!=correct_password:
    user_guess=input("Enter the password here: ")
    print("Incorret passsword")
    count+=1
print("The count of incorrect passwords is", str(count))
