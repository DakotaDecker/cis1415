userInput = input('Enter input string:\n')
while userInput != 'q':
    while ',' not in userInput:
        print('Error: No comma in string.\n')
        userInput = input('Enter input string:\n')
    splitString = userInput.split(',')
    print('First word: {}'.format(splitString[0].strip()))
    print('Second word: {}'.format(splitString[1].strip()))
    userInput = input('\nEnter input string:\n')
