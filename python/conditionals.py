x = 10
if (x==10):
    print("x is 10")
elif (x==20):
    print("x is 20")
else:
    print("x is not 10 or 20")


# Python checks conditions from TOP to BOTTOM.

# As soon as ONE condition becomes TRUE:
# 1. Python runs the code inside that true block.
# 2. Python skips all the other remaining 'elif' checks.
# 3. Python skips the 'else' block completely.
# 4. The whole if-elif-else structure ends right there.
# Note: Only ONE block of code will ever run


# break statement
x = 0
while (x < 10):
    if (x == 5):
        break # break completely exits the loop right away.
    print(x)
    x += 1

# continue statement
x = 0
while (x < 10): # while loop will run as long as condition is true it wont stop until the condition is false that's why we need to increment x in the loop otherwise it will run forever
    x += 1
    if (x == 5):
        continue # continue skips the rest of the current iteration and jumps straight to the next one
    print(x)

# case statement
def get_status_message(status_code):
    match status_code:
        case 200:
            return "Success"
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status Code"  # This is the default case

print(get_status_message(404))  # Output: Not Found
print(get_status_message(999))  # Output: Unknown Status Code