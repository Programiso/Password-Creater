from random import random
import UI
from Generate_password import GeneratePassword
from load_values import load_values

letters = (
        'q','w','e','r','t','y','u','i','o','p',
        'a','s','d','f','g','h','j','k','l',
        'z','x','c','v','b','n','m',
        'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'
) #Krotka z literami
symbols = (
        '`','~','1','2','3','4','5','6','7','8','9','0','-','=','!','@','#','$','%','^','&','*','(',')','_','+',
        'q','w','e','r','t','y','u','i','o','p','[',']','{','}',
        'a','s','d','f','g','h','j','k','l',';',"'",':','"','|',
        'z','x','c','v','b','n','m',',','.','/','<','>','?',
        'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'
) #krotka z symbolami
numbers = (
    '1','2','3','4','5','6','7','8','9','0') #krotka z liczbami

gp = GeneratePassword(letters, numbers, symbols)
option = UI.text_ui()


if option == 1: #ustawienia
    gp.settings()

elif option == 2: #Tworzy haslo z asystentem
    option = False
    while option == False:  
        gp.format_text()
        gp.password_assistant()
        option = gp.chceck_values()
        if option:
            break
        else:
            print(option)
    gp.generate_password()
    while True:
        pass

elif option == 3:
    pass #jeszcze w implementacji

else:
    exit()
