class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
    
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)
    
    def calculate(self):
        x = len(scores)
        n = 0
        for i in range(x):
            n+=scores[i]
        avg = int(n)//int(x)
        if avg >= 90 and avg <=100:
            return "O"
        if avg >= 80 and avg < 90:
            return "E"
        if avg >= 70 and avg < 80:
            return "A"
        if avg >= 55 and avg < 70:
            return "P"
        if avg >= 40 and avg < 55:
            return "D"
        if avg < 40:
            return "T"
            

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
