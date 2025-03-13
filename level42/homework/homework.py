dict1={
    "name": "Data",
    "surname": "Pkhakadze",
    "age": 15,
    "city": "Kutaisi",
    "color": "Black"
}
print(dict1.keys())
print(dict1.values())
print(dict1.items())


dict2={
    "brand": "Mercedes-Benz",
    "model": "AMG GT",
    "year": 2023,
    "horsepower": 577,
    "engine": "4.0L V8 Biturbo"
}
for keys, value in dict2.items():
    print(f"{keys}: {value}")


dict3={
    "brand": "apple",
    "model": "iphone 15 pro",
    "year": 2023,
    "storage": "256GB",
    "color": "Titanium Blue"
}
key_to_check="storage"
if key_to_check in dict3:
    print(f"'{key_to_check}' exists in the dictionary.")
else:
    print(f"'{key_to_check}' does not exist in the dictionary.")


dict4={
    "brand": "ASUS",
    "model": "ROG Strix G16",
    "processor": "Intel Core i9",
    "RAM": "32GB",
    "GPU": "NVIDIA RTX 4080",
    "storage": "1TB SSD"
}
print(dict4.get("brand"))
print(dict4.get("price"))
dict4.update({"price": 1699.99})
print(dict4)
dict4.pop("storage")
print(dict4)


dict4.update(dict3)
print(dict4)


dict5 = {
    "brand": "Dell",
    "model": "XPS 13",
    "processor": "Intel Core i7",
    "ram": "16GB",
    "storage": "512GB SSD",
    "price": 1200
}
print(len(dict5))


dict6 = {
    "a": 5,
    "b": 10,
    "c": 3,
    "d": 7.5
}

def sum_dict(dict):
    res=0
    for value in dict.value():
        if type(value)==int or float:
            res+=value
    return res

dict6.clear()
print(dict6)
