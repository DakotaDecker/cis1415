my_dict = {'A': 1, 'B':2, 'C':3, 'D':4}

print(my_dict, '\n')
del my_dict['D']
print('Delete a key from the dictionary: \n', my_dict, '\n')
print('Read the value of the key entry from the dict:\n', my_dict.get('B', 'N/A'), '\n')
val = my_dict.pop('A')
print('Remove and return the key value from the dictionary:\n', my_dict, '\n')
my_dict.clear()
print('Remove all items from the dictionary:\n', my_dict)
