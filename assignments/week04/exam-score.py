exam_score = []
number = 0

# This code use to store score in exam_score to calculate.
for number in range(0,5):
    exam_score.append(int(input(f"Enter score of student {number + 1}: ")))

# This code use to check if there any score is more than 100.
for number in range(0,5):
    if exam_score[number] > 100:
        print(f"Student {number + 1} Score is more than 100. Plese enter score again.")
        exit()

print("\n")

# This code show Student's score pass or not .if below 50 then not pass.
for number in range(0,5):
    if exam_score[number] < 50:
        print(f"Student {number + 1}: {exam_score[number]} -> ไม่ผ่าน")
    else:
        print(f"Student {number + 1}: {exam_score[number]} -> ผ่าน")