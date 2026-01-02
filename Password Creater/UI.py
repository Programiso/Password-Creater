def text_ui(program_name="PassPy", version_string="Beta 1.1", ):
    options = ["[1] Change settings",
               "[2] Create password with assistant",
               "[3] Check security of password",
               "[4] Exit"
               ]
    #pokaz komunikat
    print(f"Welcome to {program_name} version {version_string}.\nChoose an action: \n{options[0]}\n{options[1]}\n{options[2]}\n{options[3]}")
    while True:
        choose = input(">")
        try:
            choose = int(choose)
        except ValueError:
            print(f"The option you've entered is invalid, please choose from  1 to {len(options)}")
        
        if choose in range(1,len(options) + 1):
            return choose
        else:
            print("Please choose an option in range of 1 to 4")

        

