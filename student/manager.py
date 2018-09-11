# manager.py
# Program prints menu in the terminal and allows to:
# - Print student list loaded from text file
# - Check student with highest GPA
# - Add new grade
# - Add new student
# - Save the list to a file.

from student import Student


def main():
    print('Welcome to Student Manager')
    studentList = loadList()

    while True:
        task = printMenu()

        # Quit Check
        if task == 'q':
            break

        processTask(task, studentList)


def loadList():
    ''' Loads txt file with validateFile function and returns list of
        student objects. '''

    list = []
    file = validateFile()

    for line in file:
        createStudent = Student(*line.split('|'))
        list.append(createStudent)

    file.close()
    return list


def validateFile():
    ''' Opens and returns file from default path. If not found, ask user to
        type correct file path. '''

    try:
        file = open('list.txt', 'r')
        return file
    except:
        print('Default txt file not found.')
        print('Please type path to file with student data.')
        print('Remember that every data in line must be separated with "|".')
        while True:
            filePath = input('File path: ')
            try:
                file = open(filePath, 'r')
                return file
            except:
                print('File not found. Try again.')


def printMenu():
    ''' Prints out menu and returns user input. '''

    print()
    print('"Q" - quit program                  ', end=' || ')
    print('"L" - Print student list')
    print('"G" - Print student with highest GPA', end=' || ')
    print('"A" - Add grade')
    print('"N" - Add new student               ', end=' || ')
    print('"S" - Save list' + '\n')

    while True:
        userInput = input('What would you like to do? ').lower()
        if validateInput(userInput):
            return userInput


def validateInput(input):
    ''' Returns true if validation passed, else returns false. '''

    options = ('q', 'l', 'g', 'a', 'n', 's')
    for option in options:
        if input == option:
            return True

    return False


def processTask(task, studentList):
    ''' Takes user input from printMenu() and processes it. '''

    # Print student list
    if task == 'l':
        for std in studentList:
            formatedName = std.getFullName() + ' ' * (30 - len(std.getFullName()))
            print('{}{} hours\t{} points'.format(formatedName,
                  std.getHours(), std.getPoints()))

    # Print students with highest GPA
    elif task == 'g':
        bestGPA = [studentList[0]]

        # Search for the best GPA
        for std in studentList[1:]:
            if std.getGPA() > bestGPA[0].getGPA():
                bestGPA = []
                bestGPA.append(std)
            elif std.getGPA() == bestGPA[0].getGPA():
                bestGPA.append(std)

        # Print best GPA students
        print('\n' + 'Students with best GPA:')
        for std in bestGPA:
            print('{} with {} GPA points.'.format(std.getFullName(),
                  std.getGPA()))

    # Add grade
    elif task == 'a':
        student = None
        lastName = input('Student\'s last name: ').lower()
        firstName = input('Student\'s first name: ').lower()

        # Search the file for student with given first and last name
        for std in studentList:
            if lastName == std.getLastName() and firstName == std.getFirstName():
                student = std

        # Add new grade
        if student:
            grade = input('Grade: ')
            hours = input('Hours: ')

            student.addGrade(hours, grade)

        else:
            print('Student not found')

    # Add new student
    elif task == 'n':
        firstName = input('First name: ')
        lastName = input('Last name: ')
        hours = input('Hours: ')
        points = input('Points: ')

        newStudent = Student(firstName, lastName, hours, points)
        studentList.append(newStudent)

    # Save list
    else:
        file = input('File name: ')
        newList = open(file, 'w')

        for std in studentList:
            newList.write('{}|{}|{}|{}\n'.format(std.getFirstName(),
            std.getLastName(), std.getHours(), std.getPoints()))

        newList.close()


if __name__ == '__main__':
    main()
