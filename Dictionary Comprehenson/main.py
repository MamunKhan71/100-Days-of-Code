import random
names = ["Mamun", "Limon", "Sayed", "Shammo", "Jony", "Rayhan"]

scores = {student: random.randint(50, 100) for student in names}

passedStudents = {student: score for (student, score) in scores.items() if score > 50}
print(passedStudents)