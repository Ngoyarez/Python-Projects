import random
import pyautogui

chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

allchar = list(chars)

pwd = pyautogui.password('Enter a Password: ')

sample_pwd = ''

while(sample_pwd != pwd):
    sample_pwd = random.choices(allchar, k=len(pwd))
    print('<=======' + str(sample_pwd) + '======>')

    if(sample_pwd == list(pwd)):
        print('The password is: ' + ''.join(sample_pwd))
        break