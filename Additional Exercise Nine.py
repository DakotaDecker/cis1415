def vowel(string):
    count = 0
    string = string.lower()
    for x in string:
        if x == 'a':
            count += 1
        if x == 'e':
            count += 1
        if x == 'i':
            count += 1
        if x == 'o':
            count += 1
        if x == 'u':
            count += 1
    return count

def con(string):
    alpha = 0
    for x in string:
        if x.isalpha():
            alpha += 1
    con = alpha - vowel(user)
    return con

user = input('Enter a string:\n')
print('\nString contains %d vowels.' % vowel(user))
print('String contains %d consonants.' % con(user))
