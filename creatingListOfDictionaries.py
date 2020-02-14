#Creating a list of Dictionaries: 
gradebook = [] 
newStudent = {"name":"Samantha", "homework": 95, "test": 92, "exam": 100}
gradebook.append(newStudent)

newGradebook = {} 
newGradebook[gradebook[0]['name']] = gradebook[0]
print(newGradebook)