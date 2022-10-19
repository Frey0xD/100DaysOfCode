import random

name_strings = input("Give me names seprated by comma :-")


names = name_strings.split(",")

lenran = len(names)

random_choice = random.randint(0, lenran-1)

person_who_will_pay= names[random_choice]

print(person_who_will_pay + " is going to pay")
