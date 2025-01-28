#name=input("ENter your name here: ")
#surname=input("Enter your surname here: ")
#age=input("Enter your age here: ")

#def generate_big_sentence(name, surname, age):
    #print(f"Hello, my name is {name}, my surname is {surname}, my age is {age}.")
#generate_big_sentence(name, surname, age)

#def my_split(main_string, string_to_split):
  #  print(main_string.split(string_to_split))
#main_string=input("Enter your main_string here:")
#string_to_split=input("Enter your string_to_split here: ")
#my_split(main_string, string_to_split)


def manual_append(main_list, item_to_insert):
    print(main_list.insert(-1, item_to_insert))
list=input("Print main list: ")
inserted=("Print something to insert")    
manual_append(list, inserted)