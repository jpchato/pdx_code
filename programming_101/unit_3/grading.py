grade = input('Enter a number between 0-100 that represents a letter grade: ')

def test_grade(grade):
    if (grade > '90'):
        print('A')
    elif (grade>'80'):
        print('B')
    elif (grade>'70'):
        print('C')
    elif (grade>'60'):
        print('D')
    elif (grade<'60'):
        print('F')

if __name__ == "__main__":
    test_grade(grade)
