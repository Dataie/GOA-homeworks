#def sum(a, b):   
   # print("The sum of", a, "and", b, "is",a+b)
#num1=float(input("Enter number here: "))
#num2=float(input("Enter number here: "))
#sum(num1,num2)


#def even_or_odd(number):
 #   if number/2==0:
  #      print("Your number is even.")
   #lif number%2!=1 and number/2!=0:
      #  print("Your numberr is not an integer number.")
#num1=float(input("Enter your number here: "))
#even_or_odd(num1)


#def reversed_string(string):
 #   print("your reversed string is:", string[::-1])
#string1=input("Enter your string here: ")
#reversed_string(string1)


#def maximum(list):
  #  max_value=list[0]
   # for i in list:
   #     if i>max_value:
   #         max_value=i
   # print(max_value)
#list1=[3, 5, 3, 8, 64, 1 ]
#maximum(list1)


def factorial(num):
    result=1
    for i in range(2, num +1): result*=i
    print(result)
factorial(5)

