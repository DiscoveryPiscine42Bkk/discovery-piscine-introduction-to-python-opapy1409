user_input = input("Please enter a number: ")
try:
    number = float(user_input)
    
    if number % 1 !=0:
        print("The number is a decimal.")
    else:
        print("The number is not a decimal.")
except ValueError:
    print("That's not a valid number!")