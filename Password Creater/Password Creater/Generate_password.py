# -*- coding: utf-8 -*-
import secrets
import sys

class GeneratePassword():
    """Generuje hasla o danej wielkoski i piorytetem,
    Wymagane parametry: letters, numbers, symbols;
    Opcjonalne parametry: ptype, min_lenth, max_lenth, password_color', language, int_error_msg"""
    
    def __init__(self, letters, numbers, symbols, language=1, ptype=1, min_lenth=5, max_lenth=30, password_color="green", int_error_msg="Please enter a numerical value", e_priority="[{1} 2 3]"):
        sys.stdout.reconfigure(encoding='utf-8') #ustawia kodowanie na utf-8
        self.symbols = symbols #krotka z symbolami i literami oraz liczbami [!]Wymagany parametr
        self.numbers = numbers #krotka z liczbami                           [!]Wymagany parametr
        self.letters = letters #krotka z literami (())                      [!]Wymagany parametr
        
        self.language = language #informacje o jezyku(domyslny Angielski)
        self.priority = ptype #dane o typie hasla (1-numeryczne, 2-literowe, 3-alfanumeryczne)
        self.min_lenth = min_lenth #dane o minimalnym zakresie hasla(domyslnie 5)
        self.max_lenth = max_lenth #dane o maxymalnym zakresie(dlaczego?, pewnie za duzo danych)(domyslnie 30)
        self.password_color = password_color #dane o kolorze hasla, ktore bedzie wygnerowane(domyslnie zielony(\033[32))
        self.int_error_msg = int_error_msg #zmienna(a bardziej stala) przechowujaca komunikat o bledzie
        self.e_priority = e_priority #zmienna przechowująca elegancko zformatowany text 

    def settings(self):
        """Modul, ktory wyswietla uzytkownikowi opcje zmian lub zastosowania domyslnych
        Wymagane parametry: brak"""
        options = (
            "Looking for settings.json",
            "Didn't find a file. Creating new one with default values.",
            "\nSettings:",
            f"[1] Password priority:            {self.priority}",
            f"[2] Minimum lenth of password:    {self.min_lenth}",
            f"[3] Maximum lenth of password:    {self.max_lenth}",
            f"[4] Color of generated password:  {self.password_color}",
            f"[5] Language:                     {self.language}",
            "\n\n\nWhich option will you change?(1-5,r for return): "
            ) #krotka z opcjami do zmiany

    def format_text(self):
        """Elegancko formatuje text i zwraca go.
        Wymagane parametry: brak"""
        #Typy hasel:
        if self.language == 1: #wsparcie jezyka Agnielskiego:
            type1 = "Numerical"
            type2 = "Alphabetical"
            type3 = "Alphanumerical"
        elif self.language == 0: #wsparcie dla jezyka Polskiego
            type1 = "Numeryczny"
            type2 = "Alfabetyczny"
            type3 = "Alfanumeryczny"
        #Konwersja na elegancki text
        if self.priority == 1:
            self.e_priority = f"[({type1}) {type2} {type3}]"
        elif self.priority == 2: 
            self.e_priority = f"[{type1} ({type2}) {type3}]"
        elif self.priority == 3:
            self.e_priority = f"[{type1} {type2} ({type3})]"

    def password_assistant(self):
        """Modul, ktory wita uzytkownika i pomaga tworzyc z nim haslo, zmienia wartosci.
        Wymagane parametry: brak"""
        keyword = "" #wartosc domyslna(jesli zmieniona przejdzie do zmiany wartosci innych zmiennych NIE TYKAC)
        if self.language == 1:
            welcome_steps = (
                "\n\n\n\n\n\n\n\n\n\n\n\nCreate a password with assistant------------------Steps [1] 2 3", #0
                "\n\n\n\n\n First, we have to set some things:\n", #1
                f"[1] Password type: {self.e_priority}", #2, dodac tu wartosc [1 2 3 4 {5}] przy princie
                f"[2] minimum lenth of password: {self.min_lenth}", #3, tu tez to samo tylko domyslna dac w {}
                f"[3] maximum lenth of password: {self.max_lenth}", #4, tak samo
                "\n\n", #5 - WYMAGANA
                "Are you OK with theese values?(Y/N): ", #6
                "What are you going to change?(1-3): ", #7
        ) #krotka z instrukcjami
        elif self.language == 0:
            welcome_steps = (
                "\n\n\n\n\n\n\n\n\n\n\n\nUtw")
        #Wypisywanie listy
        for line in range(0,6):
            print(welcome_steps[line])  
                     
        while True: #petla, jak uzytkownik poda zly typ danych, sie zrestartuje(aka przejdzie oblewajac wszystkie if-y)
            choose = input(welcome_steps[6]) #input od uzytkownika, w razie checi dokonania zmian  
            if choose == "y" or choose == "Y": #jezeli  uzytkownik nie chce zmienic danych, wyjdzie z petli
                break #wyjscie z petli
            choose = input(welcome_steps[7]) #jesli zostala podana inna opcja niz Y lub y przejdzie do wykonywania kodu
            try: #konwertowanie na int()
                choose = int(choose)
            except ValueError: #Jesli to inny typ niz int()
                print(self.int_error_msg + " from 1 to 3") #pisze wiadomosc, aby podac prawidlowy typ danych

            if choose == 1: #ustawianie keyword-a, aby przejsc kontrole zmiany wartosci
                keyword = "Password type"
            elif choose == 2:
                keyword = "Minimum lenth of password"
            elif choose == 3:
                keyword = "Maximum lenth of password"
            
            if keyword != "": #kontrola, czy uzytkownik chce zmienic wartosci(jesli puste, ominie)
                while True: #kolejna petla w petli :D
                    value = input(f"Enter a new value for {keyword}: ")
                    #proba przekonwertowania value z str ---> int, jesli nie przejdzie, powtarza petle
                    try:
                        value = int(value)
                    except ValueError:
                        print(self.int_error_msg)
                    #zmiana wartosci
                    if choose == 1:
                        self.priority = value #zminana wartosci dla typu hasla
                        if self.priority not in range(1,4):
                            print("Password type in out of range(1 to 3). Please enter a valid value")              
                            while self.priority not in range(1, 6):
                                try:
                                    self.priority = int(input(f"Enter a new value for {keyword}: "))
                                except ValueError:
                                    print(self.int_error_msg)
                    elif choose == 2:
                        self.min_lenth = value
                    elif choose == 3:
                        self.max_lenth = value
                    while not self.max_lenth > self.min_lenth: #jezeli MAX < MIN, prosi o poprawna wartosc
                        print("Maximum lenth value is lesser than minimum lenth.\nMaximum value must be greater than minimum.\n Please change values to be as in example:\nMinimum lenth of password: 5\nMaximum lenth of password: 15")
                        try:
                            self.min_lenth = int(input(f"Enter a new value for Minimum lenth of password: "))
                            self.max_lenth = int(input(f"Enter a new value for Maximum lenth of password: "))
                        except ValueError:
                            print(self.int_error_msg)
                    if choose in range(1,4):
                        break

    def chceck_values(self):
        """Weryfikuje wartosci podane przez uzytkownika
        Wymagane parametry: brak"""
        welcome_steps = (
            "\n\n\n\n\n\n\n\n\n\n\nCreate a password with assistant------------------Steps 1 [2] 3]", #0
            f"\n\n\n\n\nPassword type: {self.e_priority}", #1
            f"Minimum lenth od password: {self.min_lenth}", #2
            f"Maximum lenth of password: {self.max_lenth}", #3
            "\n\nAre theese values right?(Y/N): " #4
        )#krotka z dalszymi instrukcjami
        
        for i in range(0,4): #listuje krotke
            print(welcome_steps[i])
        option = input(welcome_steps[4])
   
        if option == "Y" or option == "y": #jezeli uzytkownik nie chce nic zmienic, zwroci True
            return True
        else:
            return False

    def generate_password(self, fast_mode=False):
        """Generuje haslo z danymi parametrami
        Wymagane parametry: brak
        Opcjonalne parametry: fast_mode - jesli False, pisze wiadomosc koncowa""" 
       
        password = "" #domyslna wartosc password
        if self.priority == 1: #tworzy haslo numeryczne
            min_max = int((self.max_lenth - self.min_lenth) - secrets.randbelow(int((self.max_lenth) / 2)))
            while not len(password) > (self.min_lenth + min_max):
                number = secrets.choice(self.numbers)
                password += str(number)
        
        if self.priority == 2:
            min_max = int((self.max_lenth - self.min_lenth) - secrets.randbelow(int((self.max_lenth) / 2)))
            while not len(password) > (self.min_lenth + min_max):    
                letter = secrets.choice(self.letters)
                password += letter

        if self.priority == 3:
            min_max = int((self.max_lenth - self.min_lenth) - secrets.randbelow(int((self.max_lenth) / 2)))
            while not len(password) > (self.min_lenth + min_max):    
                symbol = secrets.choice(self.symbols)
                password += symbol 

        print(f"Created Password: \033[32m{password}\033[0m")
        if fast_mode == False:
            print('Copy the password, by selecting it, pressing ctrl and "C" and paste it by pressing ctrl and "V"')
            print("Lenth of the password: " + str(len(password)))

    def input_password(self):
        welcome_steps = [
            "\n\n\n\n\n\n\n\n\n\n\n\nCheck security of your password------------------Steps [1] 2 3",
            "Notice: This will try to break a password. It won't upload or send any data to the Internet. It can take some time, it depends on lenth of password and CPU speed.",
            "\nEnter a password: ",
            "\n\n\n\n\n\n\n\n\n\n\n\nCheck security of your password------------------Steps 1 [2] 3",
            "\nYou can set an order of password breaking algorithm. Default order is:",
            "[1] Numerical password",
            "[2] Letter password",
            "[3] Alphanumerical password",
            "\n\nAre you going to change these values?(Y/N): ",
            "\nEnter order of routines(e.g: 2,3,1): ",
            "\n\n\n\n\n\n\n\n\n\n\n\nCheck security of your password------------------Steps 1 2 [3]",
            "Are these values right?",
            "Password:",
            "Order of routines:"
            ]
        for i in range(0, len(welcome_steps)):
            if i == 2:
                password = input(welcome_steps[i])
            elif i == 8:
                option = input(welcome_steps[i])
            else:
                print(welcome_steps[i]) 
        