import random  # add library random
print('Welcome to the Guess the Number game!\n')
print('I have generated a secret number between 1 and 100. You have 5 guesses.\n')  # fixed colon & quote

n = 5
real = random.randint(1, 100)
max = 100
min = 1

while n > 0:
    print('Attempts left:', n)
    n = n - 1
    try:
        x = int(input("Enter your guess: "))  # fixed: 'even' -> 'int'
    except ValueError:
        print("Invalid input. Please enter an integer.\n")
        continue

    if x == real:
        n = -1
        print('Your guess is correct. The secret number is', real)
    elif x < real and x >= min and n > 0:
        min = x + 1
        print('Your guess is not correct. The secret number is between', min, 'and', max, '\n')
    elif x > real and x <= max and n > 0:
        max = x - 1
        print('Your guess is not correct. The secret number is between', min, 'and', max, '\n')
    elif (x < min or x > max) and n > 0:
        print('That number is not within the range. Please enter a number between', min, 'and', max, '\n')
    elif x != real and n == 0:
        print('The secret number is', real)




