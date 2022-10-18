print("Welcome To the love calculator!!!")
name1 = str(input("Enter your name :-"))
name2 = str(input("Enter your crush name :- "))

name1.lower()
name2.lower()

true_love = name1+name2

t = true_love.count("t")
r = true_love.count("r")
u = true_love.count("u")
e = true_love.count("e")


true = (t + r + u + e)

l = true_love.count("l")
o = true_love.count("o")
v = true_love.count("v")
e = true_love.count("e")

love = (l + o + v + e)

total = int(str(true) + str(love))

if (total < 10) or (total > 90):
    print(f"Your love score is {total}, you so together like coke and mentos.")
elif (total >= 40) or (total >= 50):
    print(f"your score is {total}, and you are alright together")
else:
    print(f"Your score is {total} There is Nothing Between You two.")
