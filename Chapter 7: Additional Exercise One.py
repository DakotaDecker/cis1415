def initial(name):
    # Grabs the first letter of a name and returns it appended with a period
    initial = list(name)
    initial = initial[0]
    initial = initial + '.'
    return initial

fullName = input('Enter your first, middle, and last names, separated by a space:\n')

full = fullName.split() # Splits user input into a list with three strings

first = full[0]
middle = full[1]
last = full[2]

print('First name:', first)
print('Middle name:', middle)
print('Last name:', last)
print('Initials: %s%s%s' % (initial(first), initial(middle), initial(last)))
