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

#while loop
while True:
    print("hello")
    break

#function
def my_function(a, b):
    return a+b

# if-else
hello = my_function(5, 10)
print(hello)
if hello > 10:
    print("hello is greater than 10")
else:
    print("hello is less than or equal to 10")