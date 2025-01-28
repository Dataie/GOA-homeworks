sentence="random sentence"
uppercase_sentence=sentence.upper()
print(uppercase_sentence)

#name=input("Enter your name here: ")
#uppercase_name=name.upper()
#print(uppercase_name)

#def uppercase(lowercase):
   # uppercase=lowercase.upper()
   # print(uppercase)
#string=input("Enter any lowercase string here: ")
#uppercase(string)



sentence="random sentence"
lowercase_sentence=sentence.lower()
print(lowercase_sentence)

#email=input("Enter your email here: ")
#lower_email=email.lower()


def lower(mixed_case_string):
    lower_string=mixed_case_string.lower()
    print(lower_string)
lower("weJIggg w8 BDWiUGHF jJ")



#sentence=input("Enter your sentence here: ")
#cap_sentence=sentence.capitalize()
#print(cap_sentence)

list=["srtn", "weuhr", "ijnINni"]
cap_list=[i.capitalize() for i in list]
print(cap_list)


sentence="Python is a programming language"
position=sentence.find("Python")
print(position)

#string=input("Enter your string here: ")
#position=string.find(substring)
#print(position)

#def find_character_index(string, character):
   # index = string.find(character)
   # if index != -1:
   #     print(f"The character '{character}' is found at index {index}.")
  #  else:
    #    print(f"The character '{character}' was not found.")

#string = input("Enter a string: ")
#character = input("Enter the character to find: ")

#find_character_index(string, character)


#string=input("Enter your string here: ")
#length=len(string)
#print(f"The length of your dring is {length}")

#def lenght(string):
   # print(len(string))
#string=input("Enter your string: ")


paragraph="The cat jumped onto the table, and the dog quickly followed the cat’s lead."
counting_the=paragraph.count("the")
print(counting_the)

#sentence=input("Enter the sentence here: ")
#character=input("entr the character you want to count")
#print(sentence.count(character))

# def counting(sentence, character):
   #  print(f"The number of charachter '{character}' that has been count in sentence '{sentence}' is {sentence.count(character)}")

# user_sentence=input("Enter your sentence here: ")
# user_character=input("Enter the character here: ")
# counting(user_sentence, user_character)

string="hello there"
print(string.index("hello"))

#def find_character_index(string, character):
  #  index = string.find(character)
   # if index != -1:
   #     print(f"The character '{character}' is found at index {index}.")
   # else:
    #    print(f"The character '{character}' was not found.")

#string = input("Enter the string: ")
#character = input("Enter the character to find: ")
#find_character_index(string, character)


string="snfwi I IJNF iwj fF"
print(string.islower())

#def lower_or_not(sentence):
   #if sentence.islower()==True:
  #    print("Every character is in lowercase")
 #  else:
      #print("Not every character is in lowercase")

#user_sentence=input("Enter the sentence here: ")
#lower_or_not(user_sentence)


#string="WWERHWNWIBW"
#print(string.isupper())

#def lower_or_not(sentence):
  # if sentence.isupper()==True:
   #  print("Every character is in uppercase")
   #else:
    #  print("Not every character is in uppercase")
#user_sentence=input("Enter the sentence here: ")
#lower_or_not(user_sentence)


string="win NWI Ijniowwb WKjSBIW"
swap=string.swapcase()
print(swap)

#def swap_case(sentence):
    #swapped_sentence = sentence.swapcase()
  # print(swapped_sentence)
#sentence = input("Enter a sentence: ")
#swap_case(sentence)


sentence="There is a one big dog over there"
print(sentence.replace("dog","cat"))

def replace_spaces_with_underscores(string):
    modified_string = string.replace(" ", "_")
    print(modified_string)
string = input("Enter a string: ")
replace_spaces_with_underscores(string)
