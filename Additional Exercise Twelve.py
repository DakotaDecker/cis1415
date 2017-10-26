def pig(english):
    pigLatin = '' # Empty string to later contain full pig latin translation
    phrase = english.split() # Splits english phrase into list of words
    for x in phrase:
        word = list(x) # Splits word into list of letters
        end = word[0] + 'ay' # Assigns the first letter of the word and the string 'ay' to 'end'
        del(word[0]) # Removes the first letter from the word
        word.append(end) # Appends the removed first letter and 'ay' to word
        piggy = ''.join(word) # Joins the list of letters into one word
        pigLatin += piggy + ' ' # Appends word to the end of the final pig latin translation along with a space
    return pigLatin

user = input('Enter a phrase in English using just letters and spaces:\n')

print('\nEnglish:', user)
print('Pig Latin:', pig(user))
