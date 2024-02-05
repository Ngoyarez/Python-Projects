"""
Caesar Cipher Algorithm by Brian Ngoya
"""

try:
    import pyperclip # pyperclip copies text to the clipboard
except ImportError:
    pass

# Symbols to be encrypted or decrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar cipher, by Brian Ngoya')
print('How it works: \n')
print('The caesar cipher encrypts letters by shifting them over by a')
print('key number. For eample, a key of two means that letter A is')
print('encrypted into C, the letter B into D and so on')

# Let the user enter  if they are encrypting or decrypting
while True:
    print('Do you want to (e)encrypt or (d)decrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    else:
        print('You can only encrypt or decrypt!')


#  Let the user enter the key to use
try:
    while True:
        maxKey = len(SYMBOLS) - 1
        print('Please enter the key (0 to {}) to use.'.format(maxKey))
        response = input('> ').upper()
        if not response.isdecimal():
            print('You can only enter an integer')
            continue

        if 0 <= int(response) < len(SYMBOLS):
            key = int(response)
            break
except ValueError:
    print('You can only enter an integer')

#  Let the user enter the message to encrypt or decrypt
print('Enter the message to {}.'.format(mode))
message = input('> ')

# Caesar cipher only works on uppercase letters
message = message.upper()

# Store the encrypted/decrypted form of the message
translated = ''

# Encrypt or decrypt each symbol in the message
for symbol in message:
    if symbol in SYMBOLS:
        # Get the encrypted(or decrypted) number for this symbol
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # Handle the wrap around if num is larger than the length of SYMBOLS or less than 0
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        # Add the encrypted or decrypted number's symbol to translated
        translated = translated + (SYMBOLS[num])

    else:
        # Just add the symbol without encrypting or decrypting
        translated = translated + symbol

# Display the encrypted/decrypted string to the screen
print('{}ed message: '.format(mode))
print(translated)

try:
    pyperclip.copy(translated)
    print('The {}ed message is copied to your clipboard'.format(mode))
except:
    pass
