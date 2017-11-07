rainfall = []

def fill():
    for month in range(12):
        rainfall.append(float(input('Enter total rainfall for month #%d:\n' % (month + 1))))

def display():
    print('\nTotal rainfall for the year:', sum(rainfall), 'inches.')
    print('Average monthly rainfall:', (sum(rainfall) / 12), 'inches.')
    print('Month with the most rainfall: #%d' % (rainfall.index(max(rainfall)) + 1))
    print('Month with the least rainfall: #%d' % (rainfall.index(min(rainfall)) + 1))

fill()
display()
