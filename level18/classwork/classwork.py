for i in range(1, 20, 2):
    print(i)

#საკლასო დავალება 3: 10-დან 30-ის ჩათვლით დაბეჭდეთ
#  ყველა რიცხვი და თან მიუწერეთ ლუწია თუ კენტი, მაგ:
#10 - even, 11 - odd, 12 - even და ასე გაგრძელდება 30-ის ჩათვლით

for i in range(10, 31):
    if i % 2 == 0:
        print(str(i), "-even")
    else:
        print((i), "-odd")


num1=int(input("Enter first number: "))  
num2=int(input("Enter second number"))
if num1>num2:
    range1=range(num2, num1+1)
    sum1=0
    #print only even numbers
    for i in range:
        if i%2 == 0:
            print(i)
            sum1+=i
    print("Sum of all even numbers are:", str(sum1))
else:
    range2=range(num1, num2+1)
    sum2=0
    #print only odd numbers
    for i in range2:
        if i%2 !=0:
            print(i)
            sum2+=1
    print("Sum of all odd numbers are:", str(sum2))