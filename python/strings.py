x = "harendra gangwar"
# we start counting index from 0,   x[0], x[1], x[2], x[3].... x[n-1] and n is the length of the string 
print(x[0])  # Output: h

print(x[0:8]) # Output: harendra   0 to n-1

print(x[3:16]) # Output: endra gangwar 3 to n-1

print(x[:]) # x[0:n]  Output: harendra gangwar 0 to n-1

print(x[0:len(x)])

# strings are immutable in python, we cannot change the value 

# strings functions
print(x.upper()) # Output: HARENDRA GANGWAR
print(x.lower()) # Output: harendra gangwar
print(x.capitalize()) # Output: Harendra gangwar

print(x.replace("h", "n")) # Output: narendra gangwar

print(x.split(" ")) # Output: ['harendra', 'gangwar'] it converted the string into list of strings