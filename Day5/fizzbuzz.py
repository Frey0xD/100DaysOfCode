# Fizz is the number is % by 3
# Buzz if the number is % by 5
# Fizz-Buzz if the number is % by both of the number (3,5)


for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number} = Fizz-Buzz")
    elif number % 5 == 0:
        print(f"{number} = Buzz")
    elif number % 3 == 0:
        print(f"{number} = Fizz")
    else:
        print(number)
