# Exercise 1: Create a list of 5 elements and print it
list1 = [1, 2, 3, 4, 5]
print(list1)

# Exercise 2: Append an element to the list and print the updated list
list1.append(6)
print(list1)

# Exercise 3: Remove an element from the list and print the updated list
list1.remove(3)
print(list1)

# Exercise 4: Sort the list in ascending order and print it
list1.sort()
print(list1)

# Exercise 5: Sort the list in descending order and print it
list1.sort(reverse=True)
print(list1)

# Exercise 6: Print the length of the list
print(len(list1))

# Exercise 7: Print the first and last element of the list
print(list1[0], list1[-1])

# Exercise 8: Create a new list with squares of elements from the original list and print it
squares = [x**2 for x in list1]
print(squares)

# Exercise 9: Create a list of even numbers from the original list and print it
evens = [x for x in list1 if x % 2 == 0]
print(evens)

# Exercise 10: Create a list of tuples where each tuple contains the element and its square, and print it
tuples = [(x, x**2) for x in list1]
print(tuples)