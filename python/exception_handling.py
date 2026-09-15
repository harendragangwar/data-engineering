try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError as e:
    print(f"Invalid input: {e}. You must enter a valid integer")
except ZeroDivisionError:
    print("Error: You entered 0, which causes a division by zero")
