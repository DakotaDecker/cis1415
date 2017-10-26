dictionary = {}

title = input('Enter a title for the data:\n')
print('You entered:', title)

col1 = input('\nEnter the column 1 header:\n')
print('You entered:', col1)

col2 = input('\nEnter the column 2 header:\n')
print('You entered:', col2)

userData = input('\nEnter a data point (-1 to stop input):\n')

while userData != '-1':
    while ',' not in userData:
        # Correct missing comma
        print('Error: No comma in string.')
        userData = input('\nEnter a data point (-1 to stop input):\n')

    count = userData.count(',')
    while count > 1:
        # Correct additional commas
        print('Error: Too many commas in input.')
        userData = input('\nEnter a data point (-1 to stop input):\n')
        count = userData.count(',')
        
    userSplit = userData.split(',')
    string = userSplit[0].strip()
    integer = userSplit[1].strip()
    while integer.isdigit() == False:
        # Correct integer
        print('Error: Comma not followed by an integer.')
        userData = input('\nEnter a data point (-1 to stop input):\n')
        userSplit = userData.split(',')
        integer = userSplit[1].strip()

    # Print inputs and add to dictionary
    print('Data string:', string)
    print('Data integer:', integer)
    dictionary[string] = integer
    userData = input('\nEnter a data point (-1 to stop input):\n')

# Print table
print('%33s' % title)
print('%-20s | %21s' % (col1, col2))
print('-' * 44)
for string, integer in dictionary.items():
    print('%-20s | %21s' % (string, integer))

# Print histogram
print('\n')
for string, integer in dictionary.items():
    print('%20s %s' % (string, '*' * int(integer)))
