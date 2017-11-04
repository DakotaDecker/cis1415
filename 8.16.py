weights = []
weight1 = float(input('Enter weight 1:\n'))
weight2 = float(input('Enter weight 2:\n'))
weight3 = float(input('Enter weight 3:\n'))
weight4 = float(input('Enter weight 4:\n'))

weights.append(weight1)
weights.append(weight2)
weights.append(weight3)
weights.append(weight4)

print('Weights:', weights)

print('\nAverage weight: %.2f' % (sum(weights) / 4))
print('Max weight: %.2f' % max(weights))

index = int(input('\nEnter a list index (1 - 4):'))
print('\nWeight in pounds: %.2f' % weights[index - 1])
print('Weight in kilograms: %.2f' % (weights[index - 1] / 2.2))
weights.sort()
print('\nSorted list:', weights)