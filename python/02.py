name = input("enter a name")
print(name,"is my name")
#input
number = input("enter a number")
print(number,"is my number")

#list
mylist = ["apple", "banana", "cherry"]

#loops
for i in mylist:
    print(i)

for i in range(len(mylist)):
    print(mylist[i])

#while loop
while True:
    print("hello")
    break

#function
def my_function(a, b):
    return a+b

# Defining the function
def greet():
    print("Hello")

# Calling the function
greet()

# passing arguments
def greet_with_name(name):
    print(f"Hello, {name}!")

greet_with_name("Alice")

# if-else
hello = my_function(5, 10)
print(hello)
if hello > 10:
    print("hello is greater than 10")
elif hello == 10:
    print("hello is equal to 10")
else:
    print("hello is less than to 10")