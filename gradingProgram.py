student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}
for keys in student_scores:
    if 91 <= student_scores[keys] <= 100:
        student_grades[keys] = "Outstanding"
    elif 81 <= student_scores[keys] <= 90:
        student_grades[keys] = "Exceeds Exceptions"
    elif 71 <= student_scores[keys] <= 80:
        student_grades[keys] = "Acceptable"
    else:
        student_grades[keys] = "Fail"

print(student_grades)
