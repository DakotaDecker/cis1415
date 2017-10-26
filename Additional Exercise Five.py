user = input('Enter a phone number in the format XXX-XXX-XXXX:\n')
print('You entered:', user)
user = user.upper()
user = user.replace('A', '2')
user = user.replace('B', '2')
user = user.replace('C', '2')
user = user.replace('D', '3')
user = user.replace('E', '3')
user = user.replace('F', '3')
user = user.replace('G', '4')
user = user.replace('H', '4')
user = user.replace('I', '4')
user = user.replace('J', '5')
user = user.replace('K', '5')
user = user.replace('L', '5')
user = user.replace('M', '6')
user = user.replace('N', '6')
user = user.replace('O', '6')
user = user.replace('P', '7')
user = user.replace('Q', '7')
user = user.replace('R', '7')
user = user.replace('S', '7')
user = user.replace('T', '8')
user = user.replace('U', '8')
user = user.replace('V', '8')
user = user.replace('W', '9')
user = user.replace('X', '9')
user = user.replace('Y', '9')
user = user.replace('Z', '9')
print('Just digits:', user)

'''
# Excessive amount of code, but it works

for x in user:
    if x == 'A' or 'B' or 'C':
        user = user.replace('A', '2')
        user = user.replace('B', '2')
        user = user.replace('C', '2')
    if x == 'D' or 'E' or 'F':
        user = user.replace('D', '3')
        user = user.replace('E', '3')
        user = user.replace('F', '3')
    if x == 'G' or 'H' or 'I':
        user = user.replace('G', '4')
        user = user.replace('H', '4')
        user = user.replace('I', '4')
    if x == 'J' or 'K' or 'L':
        user = user.replace('J', '5')
        user = user.replace('K', '5')
        user = user.replace('L', '5')
    if x == 'M' or 'N' or 'O':
        user = user.replace('M', '6')
        user = user.replace('N', '6')
        user = user.replace('O', '6')
    if x == 'P' or 'Q' or 'R' or 'S':
        user = user.replace('P', '7')
        user = user.replace('Q', '7')
        user = user.replace('R', '7')
        user = user.replace('S', '7')
    if x == 'T' or 'U' or 'V':
        user = user.replace('T', '8')
        user = user.replace('U', '8')
        user = user.replace('V', '8')
    if x == 'W' or 'X' or 'Y' or 'Z':
        user = user.replace('W', '9')
        user = user.replace('X', '9')
        user = user.replace('Y', '9')
        user = user.replace('Z', '9')
'''

'''
# Function that replaces every character in the string
# with a 2 for some reason.
# I'm not sure why it isn't working, but theoretically
# this would be the shortest way to solve the problem.

# Make sure to call the function in the print statement!

def replace(num):
    for x in num:
        if x == 'A' or 'B' or 'C':
            num = num.replace(x, '2')
        if x == 'D' or 'E' or 'F':
            num = num.replace(x, '3')
        if x == 'G' or 'H' or 'I':
            num = num.replace(x, '4')
        if x == 'J' or 'K' or 'L':
            num = num.replace(x, '5')
        if x == 'M' or 'N' or 'O':
            num = num.replace(x, '6')
        if x == 'P' or 'Q' or 'R' or 'S':
            num = num.replace(x, '7')
        if x == 'T' or 'U' or 'V':
            num = num.replace(x, '8')
        if x == 'W' or 'X' or 'Y' or 'Z':
            num = num.replace(x, '9')
    return num

# Similarly, this function returns a string of all 9s

def replace(num):
    digits = ''
    for x in num:
        if x == 'A' or 'B' or 'C':
            x = '2'
        if x == 'D' or 'E' or 'F':
            x = '2'
        if x == 'G' or 'H' or 'I':
            x = '2'
        if x == 'J' or 'K' or 'L':
            x = '5'
        if x == 'M' or 'N' or 'O':
            x = '6'
        if x == 'P' or 'Q' or 'R' or 'S':
            x = '7'
        if x == 'T' or 'U' or 'V':
            x = '8'
        if x == 'W' or 'X' or 'Y' or 'Z':
            x = '9'
        digits += x
    return num
'''
