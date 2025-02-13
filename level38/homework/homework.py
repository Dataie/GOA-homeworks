tuple1=(1,2,3,4,5)
tuple2=tuple1[0]
tuple3=tuple1[4]
tuple4=tuple1[2:4]

immutable_tuple = (1, 2, 3, 4, 5)
# immutable_tuple[0] = 10  # This will raise a TypeError
print(immutable_tuple)

packed_tuple=("first","second","third")
one,two,three=packed_tuple
print(one)
print(two)
print(three)


numbers = (1, 2, 3, 2, 4, 2, 5)
print(numbers.count(2))
print(numbers.index(2))

set1={1,2,3,4,5,}
set1.add(6)
set1.remove(3)


set1={1,2,3,4,5}
set2={3,4,5,6,7}
print(set1.union(set2))
print(set1.difference(set2))
print(set1.intersection(set2))


list1=[3,3,2,1,1,2,4]
list2=list(set(list1))
print(list2)