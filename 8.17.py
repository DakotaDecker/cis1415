

def print_menu():
    print('\nMENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit\n')


def print_roster():
    jerseys.sort()  # Sorts list of jersey numbers from lowest to highest
    print('ROSTER')
    for num in jerseys:
        # Prints all five jersey numbers (from list)
        # and their ratings (from corresponding dictionary values)
        print('Jersey number: %d, Rating: %d' % (num, roster[num]))


def add_player():
    new_jersey = int(input('\nEnter a new player\'s jersey number:\n'))
    new_rating = int(input('Enter the player\'s rating:\n'))
    roster[new_jersey] = new_rating  # Adds jersey number and rating to dictionary
    jerseys.append(new_jersey)  # Adds jersey number to list


def delete_player():
    delete = int(input('\nEnter a jersey number:\n'))
    jerseys.remove(delete)  # Removes jersey number from list
    del roster[delete]  # Removes jersey number and corresponding rating from dictionary


def update_player():
    up_jersey = int(input('\nEnter a jersey number:\n'))
    up_rating = int(input('Enter a new rating for player:\n'))
    new = {up_jersey: up_rating}  # Creates NEW dictionary with jersey number and NEW rating
    del roster[up_jersey]  # Removes jersey number and corresponding OLD rating from ORIGINAL dictionary
    roster.update(new)  # Adds NEW jersey number and corresponding rating to ORIGINAL dictionary


def output_above():
    user_rating = int(input('\nEnter a rating:\n'))
    print('\nABOVE', user_rating)
    for num in roster:
        if roster[num] > user_rating:
            print('Jersey number: %d, Rating: %d' % (num, roster[num]))


roster = {}
# Empty DICTIONARY that will fill with the jersey numbers as the keys and corresponding player ratings as the values

jerseys = []
# Empty LIST that will fill with jersey numbers which will allow sorting of jerseys

for x in range(5):
    # Iterates user prompts and dictionary/list additions FIVE times
    jersey = int(input('Enter player %d\'s jersey number:\n' % (x + 1)))
    rating = int(input('Enter player %d\'s rating:\n' % (x + 1)))
    roster[jersey] = rating  # Adds jersey number and rating to dictionary
    jerseys.append(jersey)  # Adds jersey number to list
    print()  # Prints blank line

print_roster()

user = 0

while user != 'q':
    print_menu()
    user = input('Choose an option:\n')
    if user == 'a':
        add_player()
        continue
    elif user == 'd':
        delete_player()
        continue
    elif user == 'u':
        update_player()
        continue
    elif user == 'r':
        output_above()
        continue
    elif user == 'o':
        print_roster()
        continue
