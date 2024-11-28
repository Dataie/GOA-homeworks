for i in range(50):
    print("GOA BEST!!")

sum = 0
while sum != 50:
    print("GOA BEST!!!")
    sum+=1

sum=0
while sum!=10:
    sum+=1
    print(sum)

sum=0
while sum!=20:
    sum+=2
    print(sum) 

sum=10
while sum!=1:
    sum-=1
    print(sum)    
print("Blast off")

password = 1234
user_guess = int(input("Enter your password here: "))
while password!=user_guess:
    user_guess = int(input("Enter your password here: "))
    print("try again")    

username = "Dataie"
password = "2707"

while True:
    input_name = input("Username: ")
    input_password = input("Password: ")

    if input_name == username and input_password == password:
        break
    else:
        print("Try again:)")


num = int(input("Enter number to make its factorial: "))
factorial = 1
counter = num
while counter > 0:
    factorial *= counter
    counter -= 1
print(factorial)
