n = int(input().strip())
for i in range(n):
    grade = int(input().strip())
    new_grade = grade
    while new_grade % 5 != 0 and new_grade >= 38:
        new_grade += 1
    if new_grade - grade < 3:
        print(new_grade)
    else:
        print(grade)
