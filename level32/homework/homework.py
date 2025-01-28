# def welcome_message(name, age):
    # print(f"Welcome {name}! You are {age} years old.")
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# welcome_message(name, age)

# def format_name(first_name, last_name):
    # print(f"{first_name.capitalize()} {last_name.capitalize()}")
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# format_name(first_name, last_name)

# def reverse_and_format(input_string):
    # reversed_string = input_string[::-1]
    # print(f"The reversed string is: {reversed_string}")
# input_string = input("Enter a string: ")
# reverse_and_format(input_string)

#def insertin_word(sentence,index,word):
   # print(sentence.insert(index,word))
#user_sentence=input("Enter your sentence here: ")
#user_index=input("Enter the index here: ")
#user_word=input("Enter the word you want to replace here: ")
#insertin_word

#def sentence_to_words(sentence):
  #  words = sentence.split()
  #  print(words)
#sentence = input("Enter a sentence: ")
#sentence_to_words(sentence)

csv="Hello,how,are,you,doing"
list=csv.split(",")
print(list)


#def split_paragraph(paragraph):
 #   sentences = paragraph.split('.')
  #  print(sentences)
#user_paragraph = input("Enter a paragraph: ")
#split_paragraph(user_paragraph)

def appending(list, item):
    list.append(item)
    print(list)
my_list=[1, 2, 3, 4, ]
item=5
appending(my_list, item)

def append_items(list, items):
    for i in items: list.append(items)
    print(list)
my_list=["eyrt", 12, True]
items=[32, False]
append_items(my_list, items)

def append_list(list_1, list_2):
    for i in list_1:
        list_2.append(list_1)
    print(list_2)
list1=["jeodq", 12.4, 10, True]
list2=[False, "jwimw"]
append_list(list1,list2)

def insert_item_list(list, index, item):
    list.insert(index, item)
    print(list)
list=[24, 12, 65, 23]
index=2
item=1000
insert_item_list(list, index, item)

def insert_at_beginning(my_list, item):
    my_list.insert(0, item)
    print(my_list)
my_list = [2, 3, 4]
item = 1
insert_at_beginning(my_list, item)

def insert_at_end(my_list, item):
    my_list.insert(len(my_list), item)
    print(my_list)
my_list = [1, 2, 3, 4]
item = 5
insert_at_end(my_list, item)

