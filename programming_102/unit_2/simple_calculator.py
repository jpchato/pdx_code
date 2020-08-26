'''
Let's write a simple REPL (read, evaluate, print, loop) calculator that can handle addition and subtraction.

Ask the user for an operator and each operand. Don't forget that input returns a string, which you can convert to a float using float(user_input) where user_input is the string you got from input.

Create a separate function for each operation which takes in both operands and returns the result of its operation.

Pass the user's operands to the appropriate function based on the user's selected operator and use the value the function returns as your result.

Below is some sample input/output.
'''

def simple_calculator():
    operand = input('What is the operation you would like to perform? + - * / or type done to terminate the program: ')
    while operand != 'done':    
        number_1 = input('What is the first nubmer? ')
        number_2 = input('What is the second number? ')
        if operand == '+':
            answer = sum(number_1, number_2)
            print(f'{number_1} plus {number_2} is equal to {answer}')
            return answer

        if operand == '-':
            answer = subtract(number_1, number_2)
            print(f'{number_1} minus {number_2} is equal to {answer}')
            return answer

        if operand == '*':
            answer = multiply(number_1, number_2)
            print(f'{number_1} multiplied by {number_2} is equal to {answer}')
            return answer

        if operand == '/':
            answer = divide(number_1, number_2)
            print(f'{number_1} divided by {number_2} is equal to {answer}')
            return answer
        
        operand = input('What is the operation you would like to perform? + - * / or type done to terminate the program: ')

def sum(number_1, number_2):
    return int(number_1) + int(number_2)
    
def subtract(number_1, number_2):
    return int(number_1) - int(number_2)
    
def multiply(number_1, number_2):
    return int(number_1) * int(number_2)

def divide(number_1, number_2):
    return int(number_1) / int(number_2)
    

if __name__ == "__main__":
    simple_calculator()