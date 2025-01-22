   # name=input("ENter your name here: ")
    #choice=input("CHoose u or l: ")
    #if choice=="u":
      #  print(name.upper())
   # elif choice=="l":
    #    print(name.lower())
   # else:
       # print("wRONG INFORMATION")


#def manual_find(main_string, str_to_find):
 #   print(main_string.find(str_to_find))

#manual_find("hello", "r")


main_str=input("Enter main string: ")
str_to_count=input("Enter string to count")      

print(main_str.count(str_to_count))



def manual_swapcase(string):
    for i in string:
        if i.islower():
            print(i.upper())
        elif i.isupper:
            print(i.lower())