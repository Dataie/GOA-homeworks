num1=int(input("Enter number: "))
num2=int(input("Enter number: "))
num3=int(input("Enter number: "))
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)


score=float(input("Enter you score: "))
if score>=90 and score<=100:
    print("Your score is A")
elif score>=80 and score<=89:
    print("Your score is B")
elif score>=70 and score<=79:
    print("Your score is C")
elif score>=60 and score<=69:
    print("Your score is D")
elif score<60:
    print("Your score is F")


num1=float(input("Enter number: "))
if num1>0:
    print("The number is positive")
elif num1==0:
    print("THe number is equal to 0")
else:
    print("THe number is negative")


num1=int(input("Enter number: "))
num2=int(input("Enter number: "))
total=0
for i in range(num1, num2+1):
    total+=i
print(total)
    
list=[1,2,3,4,5]
print(list[0])
print(list[2])
print(list[4])
    