#How many Days weeks months years we got left 

print(                  """Hello there ! i'm a program made by Frey
                            which tells you how many Days, weeks, months, years you got left
                            Some notes :- Enter your Name and current age :) 
                            and i will tell you for how many Days, Weeks, Months
                            you are going to live until you turn 70""")
name = (str(input("Enter your name :- ")))
current_age = (int(input("Enter your current age :- ")))
# if that user live up to 90 

#days = 365
#weeks = 52
#months = 12


years_remaining = 70 - current_age

days_left = years_remaining * 365
weeks_left = years_remaining * 52
months_left = years_remaining * 12
print(f"Hello there {name}")
print(f"The number of days you left until you turn 70 is {days_left}")
print(f"The number of Weeks you left until you turn 70 is {weeks_left}")
print(f"The number of months you left until you turn 70 is {months_left}")
print(f"The number of years you left until you turn 70 is {years_remaining}")
