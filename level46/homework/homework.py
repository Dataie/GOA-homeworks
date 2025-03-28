numbers=[x for x in range(1,11)]
print(numbers)

squared=[y**2 for y in range(1,6)]
print(squared)

even=[z for z in range(1,21) if z%2==0]
print(even)

words = ["apple", "banana", "cherry", "date", "elderberry"]
first_letter=[i[0] for i in words]
print(first_letter)

upper_case=[a.upper() for a in words]
print(upper_case)

divisible_3=[b for b in range(1,51) if b%3==0]
print(divisible_3)

extract_words=[j for j in words if len(j)>4]
print(extract_words)

celsius = [0, 10, 20, 30, 40]
celius_fahrenheit=[t*9/5+32 for t in celsius]
print(celius_fahrenheit)

sentence = "This is an example sentence with some words containing vowels"
vowels = "aeiou"
extract_words2=()

