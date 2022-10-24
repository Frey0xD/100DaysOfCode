student_score = input("Enter the list here ::-").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

#maximum = max(student_score)
maximum = 0
for score in student_score:
    if score > maximum:
        maximum = score
print(f"Here is the max score :- {maximum}" )
