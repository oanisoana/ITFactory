my_tuple = (1, 2, 3, 4, 8, 9, 10)
my_list = [13, 28, 36,44]

print(my_tuple[3])
print(type(my_list))

new_tuple = tuple(my_list)
print(type(new_tuple))

print(1 in new_tuple)

print(new_tuple[:3])
print(len(new_tuple))

x, y, z, *other = (7, 18, 29, 5, 1, 10, 34)
print(other)

last_tuple = 12, 45, 67, 22, 30
print(last_tuple)

last_tuple.append(7) #eroare
print(list(last_tuple).append(7))
