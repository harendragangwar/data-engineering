# lamda function
# A lambda function is a small anonymous function.
def square(x):
    return x * x

square = lambda x: x ** 2
print(square(5))  # Output: 25

numbers = [1, 2, 3, 4, 5, 6]
# Keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
