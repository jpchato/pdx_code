'''
Exercise 1
Create a list of 10 numbers between 1 and 10.

1.1
Print all the number in the list that are less than 5.

numbers: 3, 3, 10, 5, 4, 5, 6, 5, 7, 2

output: 
Less than five: 3, 3, 4 2
1.2
Count the number of times the number 5 occurs in your list.

numbers: 3, 3, 10, 5, 4, 5, 6, 5, 7, 2

output:
The number 5 occurs 3 times.
1.3
Change the value of each number in the list to be the square of itself. Then print the new list.

  numbers: [3, 3, 10, 5, 4, 5, 6, 5, 7, 2]

  output:
  [9, 9, 100, 25, 16, 25, 36, 25, 49, 4]
'''

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def one_point_one():
    for i in list:
        if i < 5:
            print (i)

def one_point_two():
    new_list = []
    for i in list:     
        if i == 5:
            new_list.append(i)
    print(f'there are {len(new_list)} fives in the list')

def one_point_three():
    squared_list = []
    for i in list:
        i_squared = i**2
        squared_list.append(i_squared)
    print(squared_list)

if __name__ == "__main__":
    one_point_one()
    one_point_two()
    one_point_three()
