# List : order, mutable, allow duplicate values/elements
# List take non homogenous data elements

# Empty List
list_empty = []
list_empty_2 = list()

# List details
list_one = [1, 2, 3, 4, 5, 2, 2]

# Print the list element
print("List : ", list_one)
print("List Value of 1th Position : ", list_one[1])

# using For Loop
print("Using for loop")
for i in list_one:
    print(i)

# The list data type has some more library methods.
# Methods of list objects:

# *******   Library Method  *******

# list.append(data_item)
# Add an item to the end of the list.

list_one.append(6)
print(list_one)

# list.insert(index, data_item)
# Add an item at given location of the list.

list_one.insert(2, "Three")
print(list_one)

# list.pop()
# Remove an item from the end of the list

list_one.pop()
print(list_one)         # remove last element

# list.remove(data_item)
# Remove specific data item form a list

list_one.remove("Three")
print(list_one)         # remove data item 'Three' from list

# list.count(data_item)
# Return the number of times data_item appears in the list.

num = list_one.count(2)
print("Number of times 2 appear : ", num)

# list.sort()
# sort the list
fruits = ["Apple", "Banana", "Orange", "Berry"]
fruits.sort()
print(fruits)

#Number sorting
list_one.sort()
print(list_one)

# list.reverse()

list_one.reverse()
print(list_one)
print(fruits)
