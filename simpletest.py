#def addGrade(gradebook, studentName, newGrade):
    #if not studentName in gradebook:
        #gradebook[studentName] = []
    #gradebook[studentName].append(newGrade)
    #return gradebook

#gradebook = {"Daniel": 20, "Peter": 15, "John":19, "Mary": 21}
#print(addGrade(gradebook, "Harry", "22"))

gradebook = []
newStudent = {"name": "Samantha", "homework": 95, "test": 92, "exam": 100}
gradebook.append(newStudent)


newStudent = {"name": "Harry", "homework": 89, "test": 95, "exam": 91}
gradebook.append(newStudent)

print(gradebook[0]['name'])

newGradeBook = {}
newGradeBook[studentName] = gradebook[0]
print(newGradeBook)
