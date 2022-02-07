def add_student():
    print('Please enter new student details:')

    fname = input('     First Name: ')
    lname = input('     Last Name: ')
    location = input('     Location: ')
    phone = input('     Phone Number: ')
    email = input('     E-mail id: ')
    dob = input('       Date of Birth: ')

    print('Please enter student marks obtained in the exam:')
    languages = input('        Languages: ')
    math = input('      Mathematics: ')
    art = input('       Arts: ')
    computer_science = input('      Computer science: ')
    social_studies = input('        social Studies: ')

    f = open("Studentinfo.csv", "a")
    student_info = '{0}, {1}, {2}, {3}, {4}, {5},{6}, {7}, {8}, {9}, {10}\n'.format(fname, lname, location, phone, email, dob,languages, math, art, computer_science , social_studies)
    f.write(student_info)
    f.close()
    
def list_students():
    print('List of students')
    f = open("Studentinfo.csv", "r")
    for line in f:
        student_info = line.split(",")
        fname = student_info[0]
        lname = student_info[1]
        phone = student_info[3]
        student_brief_info = '{0}, {1}, {2}'.format(fname, lname, phone)
        print(student_brief_info)
    f.close()

def  exam_results():
    print('Exam Results')
    f = open("Studentinfo.csv", "r")
    for line in f:
        student_info = line.split(",")
        fname = student_info[0]
        lname = student_info[1]

        result = "Passed"
        languages = int(student_info[6])
        math = int(student_info[7])
        art = int(student_info[8])
        computer_science = int(student_info[9])
        social_studies = int(student_info[10])

        if (languages < 70 or math < 70 or art < 70 or computer_science < 70 or social_studies < 70):
            result = "Failed"

        student_result_info = '{0}, {1}, {2}'.format(fname, lname, result)
        print(student_result_info)
    f.close()
    


def other():
    print('Others')

print('School Management')
print('Main Menu')
print("     1. Add Student")
print("     2. List Student")
print("     3. Exam Results")

print("What do you want to do?")

choice = input("Enter your choice ( 1/2/3/4): ")

print(choice)

match choice:
    case '1':
        add_student()    
    case '2':
        list_students()
    case '3':
        exam_results()
    case _:
        other()


