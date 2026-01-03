def text_ui(language, program_name="PassPy", version_string="Beta 1", ):
    """Funkcja wypisujaca UI
    Wymagane parametry: language
    Opcjonalne parametry: program_name, version_string"""
    if language == 1: #wsparcie dla Angielskiego
        options = ("[1] Change settings",
                   "[2] Create password with assistant",
                   "[3] Check security of password",
                   "[4] Exit"
                   )
    elif language == 0: #wsparcie dla Polskiego
        options = ("[1] Zmień ustawienia",
                   "[2] Utwórz hasło z kreatorem",
                   "[3] Sprawdź bezpieczeństwo hasła",
                   "[4] Wyjdź")

    #pokaz komunikat
    if language == 1: #wsparcie dla Angielskiego
        print(f"{program_name} {version_string}.(C)Programiso 2026\nChoose an action: \n{options[0]}\n{options[1]}\n{options[2]}\n{options[3]}")
    elif language == 0:
        print(f"{program_name} {version_string}.(C)Programiso 2026\nWybierz akcję: \n{options[0]}\n{options[1]}\n{options[2]}\n{options[3]}")

    while True:
        choose = input(">")
        
        try: #proba przekonwertowania
            choose = int(choose)
        except ValueError: #jezeli typ jest inny
            if language == 1: #wsparcie dla Angielskiego
                print(f"The option you entered is invalid. Please enter an option between 1 and {len(options)}.")
            if language == 0: #wsparcie dla Polskiego
                print(f"Podana opcja nie jest prawidłowa. Podaj opcję pomiędzy 1 a {len(options)}")
        if choose in range(1,len(options) + 1): 
            return choose
        else:
            if language == 1: #wsparcie dla Angielskiego
                print("Please choose an option in range of 1 to 4")
            elif language == 0: #wsparcie dla Polskiego
                print("Wybierz opcję pomiędzy 1 a 4")
        

