def pig(english):
    pigLatin = ''
    phrase = english.split()
    for x in phrase:
        word = list(x)
        end = word[0] + 'ay'
        del(word[0])
        word.append(end)
        piggy = ''.join(word)
        pigLatin += piggy + ' '
    return pigLatin

user = input('Enter a phrase in English using just letters and spaces:\n')

print('\nEnglish:', user)
print('Pig Latin:', pig(user))
