print("\t\t\tWelcome to the BMI calculator\n\t\t\t\t\t ~ By Frey")
print("\t\t\tBelow 18.5 ======= UnderWeight")
print("\t\t\t18.5-24.9  ======= Normal")
print("\t\t\t25-29.9    ======= OverWeight")
print("\t\t\t>30        ======= Obese")
print("\t\t\tPig        ======= Pig")
name = str(input("Enter Your name: "))
height = float(input("Enter Your height: "))
weight = float(input("Enter Your Weight: "))

BMI = weight / (height / 100)**2

if BMI < 18:
    print("Hello " + name + " you are Underweight and your BMI is :- " + str(BMI) )
elif (BMI <= 24.9):
    print("Hello " + name + " you are Normal and your BMI is :- " + str(BMI) )
elif (BMI <=29.9):
    print("Hello " + name + " you are OverWeight and your BMI is :- " + str(BMI) )
elif (BMI > 30):
    print("Hello " + name + " you are Obese and your BMI is :- " + str(BMI) )
else:
    print("You Are A Pig")
