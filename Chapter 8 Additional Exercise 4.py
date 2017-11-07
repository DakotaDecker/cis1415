

def printMenu():
    print('\nMENU')
    print('1. Add a new hike')
    print('2. View hikes')
    print('3. Remove hike')
    print('4. Modify hike')
    print('q. Quit')



def addHike():
    newHike = input('\nEnter name for hike:\n')
    newTrail = input('Enter name of trail:\n')
    newDistance = float(input('Enter total distance (in KM):\n'))
    newTime = input('Enter total time (in minutes):\n')

    hikes[newHike] = {'Trail': newTrail, 'Distance': newDistance, 'Time': newTime}
    print(newHike, 'added!')
    

def viewHikes():
    if hikes == {}:
        print('No hikes entered')
    else:
        for x in hikes:
            print('\nName:', x)
            print('Trail:', hikes[x]['Trail'])
            print('Distance: %.2f KM' % hikes[x]['Distance'])
            print('Time:', hikes[x]['Time'], 'minutes')


def removeHike():
    if hikes == {}:
        print('No hikes entered')
    else:
        print('Current hikes:')
        for x in hikes.keys():
            print(x)
        remove = input('Which would you like to remove?\n')
        del hikes[remove]
        print(remove, 'removed!')
    
def modifyHike():
    if hikes == {}:
        print('No hikes entered')
    else:
        print('Current hikes:')
        for x in hikes.keys():
            print(x)
        modHike = input('Which would you like to modify?\n')
        modVal = input('Which value would you like to modify? (Trail, Distance, Time)\n')
        newVal = input('What would you like to change it to?\n')
        new = {modVal: newVal}
        del hikes[modHike][modVal]
        hikes.update(new)
        print(modHike, 'updated!')

hikes = {}

user = 0
while user != 'q':
    printMenu()
    user = input('\nWhat would you like to do?\n')
    if user == '1':
        addHike()
        continue
    elif user == '2':
        viewHikes()
        continue
    elif user == '3':
        removeHike()
        continue
    elif user == '4':
        modifyHike()
        continue
