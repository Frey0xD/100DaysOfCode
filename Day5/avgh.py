# let's start 

student_height = input("Enter your height:-").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)


# Not using len() or sum() for this one 

#total_height = sum(student_height)
#total_len = len(student_height)
#average = (total_height / total_len)
#print(average)

total_height = 0
for height in student_height:
    total_height += height

number_of_students = 0
for number in student_height:
    number_of_students += 1

average = (total_height / number_of_students)
print(f"The average height of the student is {average}")
