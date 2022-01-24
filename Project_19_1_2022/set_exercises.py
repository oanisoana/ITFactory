my_set = {1, 10, 21, 44, 46, 88, 10, 21}
my_set2 = {11, 100, 210, 442, 46}

print(my_set)
# print(my_set[0])

lst = [11, 14, 15, 16, 14, 15, 16]
print(list(set(lst)))

my_set.add(7)
print(my_set)

print(my_set.difference(my_set2))
print(my_set.intersection(my_set2))
