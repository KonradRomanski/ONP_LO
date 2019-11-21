import main

def choose_language():
    print("pl/en ?")
    language = input()
    while language not in ("pl", "en"):
        print(main.show_image("ValueError"))
        language = input()
    return language


def welcome(language):
    if language == "pl":
        print("\n\033[36;1m------ZAMIANA ODWROTNEJ NOTACJI POLSKIEJ NA NOTACJĘ INFIKSOWĄ------\033[0m")
        print("Aby wyjść z programu wpisz 'exit' lub 'quit' \n")
        print("Możesz zacząć wpisywać swoją formułę.")
    if language == "en":
        print("\n\033[36;1m------CHANGING REVERSED POLISH NOTATION TO INFIX NOTATION------\033[0m")
        print("To exit program, type 'exit' or 'quit' \n")
        print("You can enter your expression now. ")

def alllines(language):
    if language == "pl":
        print("Wybrałeś wpisywanie wielu linii naraz")
        print("Aby zakończyć wpisywanie i wyświetlić wyniki, naciśnij ctrl + d")
    if language == "en":
        print("You have chosen to enter multiple lines at once")
        print("To finish entering and display the results, press ctrl + d ")

def goodbye(language):
    if language == "pl":
        print("\n\033[0mDO ZOBACZENIA!")
        # print("Wesprzyj nas przelewając trochę pieniędzy: <numer_konta>")
        print("© Anna Panfil & Konrad Romański")
    if language == "en":
        print("\n\033[0mSEE YOU SOON!")
        print("© Anna Panfil & Konrad Romański")
