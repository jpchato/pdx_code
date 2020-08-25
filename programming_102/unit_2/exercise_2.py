'''
2.1
Create a blank list called colors.

Construct a Read, Evaluate, Print, Loop (REPL) which performs the following on each iteration of the loop:

Prompt the user for a color
If the user enters 'done' instead of a color, exit the loop.
If the color is already in the colors list, inform the user that the color is already in the list and repeat the loop.
If the color is not already in the colors list, add it and tell the user it was added.
When the loop ends, display the list of colors back to the user.
'''

def colors_loop():
    answer = get_color()
    colors = []

    while answer != 'done':
        
        if answer not in colors:
            if answer != 'done':
                colors.append(answer)
                print(f'{answer} has been added to the list')
                answer = input('Pick a color, or type done to terminate program: ')

        elif answer in colors:
            print('That color has already been selected')
            answer = input('Pick a color, or type done to terminate program: ')

    print(colors)

# def colors_loop():
    
#     answer = input('Pick a color, or type done to terminate program: ')
#     colors = []

#     while answer != 'done':
        
#         if answer not in colors:
#             if answer != 'done':
#                 colors.append(answer)
#                 print(f'{answer} has been added to the list')
#                 answer = input('Pick a color, or type done to terminate program: ')

#         elif answer in colors:
#             print('That color has already been selected')
#             answer = input('Pick a color, or type done to terminate program: ')

#     print(colors)


'''
2.2
Define a function get_color() which prompts the user for a color and then returns that color.

Use get_color() in your REPL to get the colors from the user.
'''

def get_color():
    answer = input('Pick a color or type done to terminate: ')
    return answer
    
    


if __name__ == "__main__":
    colors_loop()
    