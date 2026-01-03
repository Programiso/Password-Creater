def text_ui(program_name="PassPy", version_string="Beta 1", ):
    """Funkcja wypisujaca UI
    Wymagane parametry: brak
    Opcjonalne parametry: program_name, version_string"""
    options = ["[1] Change settings óż",
               "[2] Create password with assistant",
               "[3] Check security of password",
               "[4] Exit"
               ]

    #pokaz komunikat
    print(f"{program_name} {version_string}.(C)Programiso 2026\nChoose an action: \n{options[0]}\n{options[1]}\n{options[2]}\n{options[3]}")
    while True:
        choose = input(">")
        
        try: #proba przekonwertowania
            choose = int(choose)
        except ValueError: #jezeli typ jest inny
            print(f"The option you entered is invalid. Please enter an option between 1 and {len(options)}.")
        
        if choose in range(1,len(options) + 1): 
            return choose
        else:
            print("Please choose an option in range of 1 to 4")

        

