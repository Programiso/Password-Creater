import json

def load_values():
    """Funkcja, ktora odczytuje z pliku ustawienia.
    Wymagane parametry: brak"""
    while True:
        try:
            with open("settings.json") as f:
                content = f.read() #odczytuje wartosci z pliku
                contents = json.loads(content) #konwertuje wartosci na slownik
                for key in contents: #iteruje przez slownik
                    print(key)

        except FileNotFoundError:
            with open("settings.json", 'x') as f:
                content = {
                        "priority": 1,
                        "min_lenth": 5,
                        "max_lenth": 30,
                        "password_color": 'green', 
                        "language": 'English'
                    } #slownik ze wartosciami domyslnymi
                f.write(json.dumps(content)) #zapisuje slownik do pliku
