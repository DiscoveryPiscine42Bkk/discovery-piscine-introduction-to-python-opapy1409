num = int(input("Enter a number: "))
if num > 25:
    print("Error")
else:
    while num <= 25:
        print("Inside the loop, my variable is,", num)
        num += 1
        