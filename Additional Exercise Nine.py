def num_vowels(UserInput):
    num = UserInput.count('a')
    num2 = UserInput.count('e')
    num3 = UserInput.count('i')
    num4 = UserInput.count('o')
    num5 = UserInput.count('u')
    return num + num2 + num3 + num4 + num5

def num_consonants(userinput):
    n1 = userinput.count('b')
    n2 = userinput.count('c')
    n3 = userinput.count('d')
    n4 = userinput.count('f')
    n5 = userinput.count('g')
    n6 = userinput.count('h')
    n7 = userinput.count('j')
    n8 = userinput.count('k')
    n9 = userinput.count('l')
    n10 = userinput.count('m')
    n11 = userinput.count('n')
    n12 = userinput.count('p')
    n13 = userinput.count('q')
    n14 = userinput.count('r')
    n15 = userinput.count('s')
    n16 = userinput.count('t')
    n17 = userinput.count('v')
    n18 = userinput.count('w')
    n19 = userinput.count('x')
    n20 = userinput.count('y')
    n21 = userinput.count('z')
    return n1 + n2 +n3 + n4 + n5 + n6 +n7 + n8 + n9 + n10 + n11 + n12 + n13 + n14 + n15 + n16 + n17 + n18 + n19 + n20 + n21 
    

if __name__ == '__main__':
    Input = input('Enter a String:\n')
    vowels = num_vowels(Input)
    consonants = num_consonants(Input)
    print('Number of vowels:', vowels)
    print('Number of consonants:', consonants)
