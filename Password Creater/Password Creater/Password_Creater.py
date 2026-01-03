from random import random
import UI
from Generate_password import GeneratePassword
from load_values import load_values

#Krotki:
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

gp = GeneratePassword(letters, numbers, symbols) #Przypisanie klasy

while True:
    gp.generate_password(True)
    option = UI.text_ui() #przypisanie funkcji
    if option == 1: #ustawienia
        print("We're sorry, but this option is still in implemenation.") #jeszcze w implementacji

    elif option == 2: #Tworzy haslo z asystentem
        option = False #Przypisanie opcji = False
        while option == False:  
            gp.format_text() #formatuje opcje self.priority na self.e_priority
            gp.password_assistant() #laduje asystenta hasla
            gp.format_text() #formatuje text
            option = gp.chceck_values() #zwraca opcje 
            if option:
                break #wylamuje sie z petli
            else:
                pass
        gp.generate_password() #generuje haslo
        while True: #wchodzi w nieskonczona petle
            pass

    elif option == 3:
        print("We're sorry, but this option is still in implemenation.") #jeszcze w implementacji

    else:
        exit() #wychodzi z programu
