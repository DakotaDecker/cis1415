

def encryptInput(plaintext):
    encryptList = []
    for x in plaintext:
        encryptList.append(code[x])
        encrypt = ''.join(encryptList)
    print('\nEncrypted:', encrypt)
    return encrypt


def decryptEncrypted(argument):
    decryptList = []
    for x in argument:
        for original, encrypted in code.items():
            if x in encrypted:
                decryptList.append(original)
            decrypt = ''.join(decryptList)

    print('\nDecrypted:', decrypt)


code = {
    'A': '!', 'a': '@', 'B': '#', 'b': '$', 'C': '%', 'c': '^',
    'D': '&', 'd': '*', 'E': '(', 'e': ')', 'F': '_', 'f': '+',
    'G': '1', 'g': '2', 'H': '3', 'h': '4', 'I': '5', 'i': '6',
    'J': '7', 'j': '8', 'K': '9', 'k': '0', 'L': '-', 'l': '=',
    'M': '<', 'm': '>', 'N': '.', 'n': ',', 'O': '/', 'o': 'U',
    'P': ':', 'p': ';', 'Q': '"', 'q': "'", 'R': 'A', 'r': 'z',
    'S': 'L', 's': 'd', 'T': 'S', 't': 'e', 'U': 'q', 'u': 'P',
    'V': 'v', 'v': 'O', 'W': 'K', 'w': 'r', 'X': 'R', 'x': 'k',
    'Y': 'I', 'y': 'H', 'Z': 'x', 'z': 'X', ' ': 't', '.': 'F',
    ',': 'V', '?': 'W', '!': 'E', "'": 'T'
}


user = input('Enter a sentence:\n')
        
encryptedInput = encryptInput(user)

decryptEncrypted(encryptedInput)
