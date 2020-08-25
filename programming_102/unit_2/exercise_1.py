'''
Construct a Read, Evaluate, Print, Loop (REPL) which performs the following on each iteration of the loop:

Increment a counter variable to keep track of the number of loops.

Ask the user if they would like to loop again.

If the user enters 'yes', repeat the loop

If the user enters 'no', end the loop and display the number of loops performed.
'''

def loop_count():
    # loop = True
    # while loop == True:
    counter = 0
    answer = input("Would you like to loop again? Yes or no? ")
    answer = answer.lower()
    while answer == 'yes':
        counter += 1
        answer = input("Would you like to loop again? Yes or no? ")
        
    if answer == 'no':
        print (counter)
        return 

if __name__ == "__main__":
    loop_count()


        

