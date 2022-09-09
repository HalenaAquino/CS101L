# Introduction 
print('**** Welcome to the LAB grade calculator! ****')
print()

# Asks user name
name = input('Who are we calculating grades for? ==> ')
print()

# Asks user labs grade
labs_grade = int(input('Enter the Labs grade? ==> '))

# Determines if the value the user entered it greater than 100 or less than 0
if (labs_grade > 100):
    print(f'The lab value should have been 100 or less. It has been changed to 100.')
    labs_grade = 100
elif (labs_grade < 0):
    print(f'The lab value should have been zero or greater. It has been changed to zero.')
    labs_grade = 0
print()

# Asks user exams grade
exams_grade = int(input('Enter the EXAMS grade? ==> '))

# Determines if the value the user entered it greater than 100 or less than 0
if (exams_grade > 100):
    print(f'The exam value should have been 100 or less. It has been changed to 100.')
    exams_grade = 100
elif (exams_grade < 0):
    print(f'The exam value should have been zero or greater. It has been changed to zero.')
    exams_grade = 0
print()

# Asks user attendance grade
attendance_grade = int(input('Enter the Attendance grade? ==> '))

# Determines if the value the user entered it greater than 100 or less than 0
if (attendance_grade > 100):
    print(f'The attendance value should have been 100 or less. It has been changed to 100.')
    attendance_grade = 100
elif (attendance_grade < 0):
    print(f'The attendance value should have been zero or greater. It has been changed to zero.')
    attendance_grade = 0
print()

# Multiplies the user's grades by the their weight
weighted_labs = labs_grade * 0.7
weighted_exams = exams_grade * 0.2
weighted_attendance = attendance_grade * 0.1

# Calculates the user's weighted grade 
weighted_grade = weighted_labs + weighted_exams + weighted_attendance

# Prints the user their weighted grade
print(f'The weighted grade for {name} is {weighted_grade}')

# Gives the user's weighted grade the correct letter grade
if (weighted_grade >= 90 and weighted_grade <= 100):
    letter_grade = 'A'
elif (weighted_grade >= 80 and weighted_grade < 90):
    letter_grade = 'B'
elif (weighted_grade >= 70 and weighted_grade < 80):
    letter_grade = 'C'
elif (weighted_grade >= 60 and weighted_grade < 70):
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Print's the user's letter grade
print(f'{name} has a letter grade of {letter_grade}')
print()

# Ending
print('**** Thanks for using the Lab grade calculator ****')
