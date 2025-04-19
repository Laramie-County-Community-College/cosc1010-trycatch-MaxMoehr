'''
A pedometer treats walking 2,000 steps as walking 1 mile. 

Write a steps_to_miles() function that takes the number of steps as a parameter and returns the miles walked. 

The steps_to_miles() function raises a ValueError object with the message "Exception: Negative step count entered." when the number of steps is negative.
 Complete the main() program that reads the number of steps from a user, calls the steps_to_miles() function, and outputs the returned value from the 
 steps_to_miles() function. Use a try-except block to catch any ValueError object raised by the steps_to_miles() function and output the exception message.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')

Ex: If the input of the program is:

5345
the output of the program is:

2.67
Ex: If the input of the program is:

-3850
the output of the program is:

Exception: Negative step count entered.
'''



"""

File:5_Make.py

Name:Max Moehr


Requirements: Make Pedometer
create  steps_to_miles() function to output miles
create ValueError object with apropriate error message for values less than 0


Constants: 2000

Variables: steps_walked - user input
miles_walked - calculation from steps to miles
miles - what is returned in function steps_to_miles

input: number of steps walked

calculated: steps to miles (2,000 steps per mile)

Output: floating-point value to two cecimal places (miles)


Key design considerations: making error messages understandable and outputting converted miles

Test data: 
program start :

'enter number of steps walked: '

user input: '3000'

output: 'you wallked 1.50 miles'

"""

# Define your method here
def steps_to_miles(): #function that calculates steps to miles
    steps_walked = int(input("enter number of steps walked: ")) #user input
    miles_walked = steps_walked/2000 #calculation
    if steps_walked < 0:
        raise ValueError('Invalid Step Count') #causes the program to stop and go to error handeling
    return miles_walked

if __name__ == '__main__':
    try:
        miles = steps_to_miles()
        
        print(f'\nyou wallked {miles:.2f} miles\n') #output

    except ValueError as excpt: #what is done when error occurs
        print(excpt)
        print('Exception: Negative step count entered.\n')

