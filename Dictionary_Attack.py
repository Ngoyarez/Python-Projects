import random
import pyautogui

characters = "abcdefghijklmnopqrstuvwxyz0123456789"

list_chars = list(characters)

userPassword = pyautogui.password("Enter Your Password: ")

sample_pwd = ""

while sample_pwd != userPassword:
    sample_pwd = random.choices(list_chars, k=len(userPassword))

    print("-----" + str(sample_pwd) + "------")

    if sample_pwd == list(userPassword):
        print("The Password is :" + "".joins(sample_pwd))
        break