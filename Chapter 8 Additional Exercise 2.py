
    
def edit():
    num = int(input('Enter which name you would like to change (1, 2, or 3):\n'))
    print('Name to edit:', fullName[(num - 1)])
    new = input('What would you like to change the name to?\n')
    fullName[(num - 1)] = new
    firstName = fullName[0]
    middleName = fullName[1]
    lastName = fullName[2]
    print('New full name:', firstName, middleName, lastName)

def vowels():
    nameString = ''.join(fullName)
    vowel = 0        
    for x in nameString:
        if x == 'a':
            vowel += 1
        elif x == 'e':
            vowel += 1
        elif x == 'i':
            vowel += 1
        elif x == 'o':
            vowel += 1
        elif x == 'u':
            vowel += 1
            
    print('\nThe name contains %d vowels.' % vowel)


def nick():
    nickname = input('What is your nickname?\n')
    fullName[1] = [middleName, nickname]
    print(fullName)


user = input('Enter your full name:\n')
fullName = user.split()
firstName = fullName[0]
middleName = fullName[1]
lastName = fullName[2]

print('\nFirst name:', firstName)
print('Middle name:', middleName)
print('Last name:', lastName)

userInput = input('\nWould you like to edit any of the names? (y/n)\n')
while userInput != 'y' or 'n':
    if userInput == 'y':
        edit()
    if userInput == 'n':
        break
    else:
        userInput = input('Would you like to edit the name? (y/n)\n')

vowels()

    
