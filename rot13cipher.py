"""
ROT13 Cipher by Brian Ngoya
For more info on rot13 cipher visit
https://en.wikipedia.org/wiki/ROT13
"""

try:
    import pyperclip
except ImportError:
    pass

# Set up the constants
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

print('ROT13 Cipher by Brian Ngoya')
print()

while True:
    print('Enter a message to encrypt or decrypt (or QUIT): ')
    message = input('> ')

    if message.upper() == 'QUIT':
        break

    # Rotate the Letters in the message by 13 characters
    translated = ''
    for character in message:
        if character.isupper():
            # Concatenate uppercase translated letters
            transCharIndex = (UPPER_LETTERS.find(character) + 13) % 26
            translated += UPPER_LETTERS[transCharIndex]
        elif character.islower():
            # Concatenate lowercase translated letters
            transCharIndex = (LOWER_LETTERS.find(character) + 13) % 26
            translated += LOWER_LETTERS[transCharIndex]
            print(translated)
        else:
            # Concatenate the character untranslated
            translated += character

    # Display the translation
    print('The translated message is: ')
    print(translated)
    print()

    try:
        # copy the translation to the clipboard
        pyperclip.copy(translated)
        print('Translated message copied to the clipboard')
    except  :
        pass

