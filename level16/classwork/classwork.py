user_num = int(input("Enter your number here: "))
sum = 0
for i in range(user_num):
   sum = sum + i
print(sum)




#საკლასო დავალება: 
#შექმენით correct_password ცვლადი და მასში შეინახეთ ნებისმიერი სთრინგი.
#სანამ მომხმარებლის შემოტანილი პაროლი არ იქნება correct_password-ის ტოლი, თავიდან შეეკითხეთ.
#საბოლოოდ, დაუბეჭდეთ access granted და ასევე რამდენჯერ მოუწია პაროლის შემოტანა.
#დაგჭირდებათ while loop, counter variable

counter = 0
correct_password = "Any_Word"
user_guess = (input("Enter password here: "))
while user_guess != correct_password:
   user_guess = (input("Enter password here: "))
   counter += 1
print("Access granted")
print("Yur count:", str(counter))

counter = 0
my_num = 5
user_guess = input("Enter your number here: ")
while user_guess != my_num :
   user_guess = input("Enter your number here: ")
   print("Try again")
   counter += 1
print("Access granted")
print("Your count:", str(counter))

