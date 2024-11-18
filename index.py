# empty list
my_list = []

# append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


print(my_list)

# inserting 15 at index 1
my_list.insert(1, 15)

print(my_list)

# extend the list
my_list.extend([50, 60, 70])

print(my_list)

# remove last element
my_list.pop()

print(my_list)

# sort list in ascending order
my_list.sort()

print(my_list)

# find and print index of 30
print(my_list.index(30))
