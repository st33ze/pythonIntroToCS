# student.py

class Student():
    ''' Contains student information with useful methods '''
    def __init__(self, firstName, lastName, hours, points):
        self.firstName = firstName.lower()
        self.lastName = lastName.lower()
        self.hours = float(hours)
        self.points = float(points)

    def addGrade(self, hours, points):
        self.hours = self.hours + float(hours)
        self.points = self.points + float(points)

    def getFullName(self):
        return (self.lastName + " " + self.firstName).title()

    def getGPA(self):
        return self.hours * self.points

    def getHours(self):
        return self.hours

    def getPoints(self):
        return self.points

    def getLastName(self):
        return self.lastName

    def getFirstName(self):
        return self.firstName
