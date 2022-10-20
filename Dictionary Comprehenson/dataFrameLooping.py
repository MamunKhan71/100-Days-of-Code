import pandas

student_dict = {
    "student": ["Angela","James", "Lily"],
    "score": [56,76,98]

}


studentDataFrame = pandas.DataFrame(student_dict)
print(studentDataFrame)

for (index, row) in studentDataFrame.iterrows():
    print(row.student)