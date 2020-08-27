'''
Version 1
Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.
'''

def feet_to_meters():
    feet = input('How many feet do you need to convert to meters? ')
    meters = float(feet) * 0.3048
    print(f'The conversion is {meters} meters')

'''
Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers. Hint: Try using the unit as the key and the conversion as the value.
'''
def units_to_meters():
    conversion_dict = {'feet': 0.3048, 'mile': 1609.34, 'kilometer': 1000, 'meter': 1, 'yard': 0.9144, 'inch': 0.0254}
    units = input('Which unit do you need to convert to meters? feet, mile, kilometer, meter, yard, or inch? ')
    length = input ('How many units do you need to convert? ')
    answer = conversion_dict.get(units)
    print('answer: ' + str(answer))
    print('length: ' + str(length))
    total = float(answer) * float(length)
    print('The conversion to meters is ' + str(total))

if __name__ == "__main__":
    feet_to_meters()
    units_to_meters()