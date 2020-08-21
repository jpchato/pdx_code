number = 42

# 4.1

def near_hundred(number):
    if abs(100 - number) <= 10:
        print('True')
        return True
    else:
        print('False')
        return False

# 4.2

def four_point_two():
    number_1 = input('input a number: ')
    number_2 = input('input a number: ')
    limit = input('choose the limit of how many numbers may be in between the two: ')
    if abs(int(number_1) - int(number_2)) <= int(limit):
        print('True')
        return True
    else:
        print('False')
        return False

if __name__ == "__main__":
    near_hundred(number)
    four_point_two()