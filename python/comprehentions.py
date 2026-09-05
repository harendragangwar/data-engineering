# list comprehentions
my_list = [1, 2, 3, 4, 5]

# create a new list with the squares of the numbers in my_list
squared_list = [x**2 for x in my_list]
print(squared_list)  # Output: [1, 4, 9, 16, 25]

# dictionary comprehentions
my_dict = {'a': 1, 'b': 2, 'c': 3}

# create a new dictionary with the values doubled
doubled_dict = {k: v*2 for k, v in my_dict.items()}
print(doubled_dict)  # Output: {'a': 2, 'b': 4, 'c': 6}