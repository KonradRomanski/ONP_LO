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
        print("Aby wyjść z programu wpisz 'exit' lub 'quit' albo użyj ctrl + d lub ctrl + c\n")
        print("Możesz zacząć wpisywać swoją formułę.")
    if language == "en":
        print("\n\033[36;1m------CHANGING REVERSED POLISH NOTATION TO INFIX NOTATION------\033[0m")
        print("To exit program, type 'exit' or 'quit' either use ctrl + d or ctrl + c\n")
        print("You can enter your expression now. ")

def alllines(language):
    if language == "pl":
        print("Wybrałeś wpisywanie wielu linii naraz")
        print("Zakończ działane programu, aby zakończyć wpisywanie i wyświetlić wyniki")
    if language == "en":
        print("You have chosen to enter multiple lines at once")
        print("Exit the program to finish typing and view the results")

def everyline(language):
    if language == "pl":
        print("Wybrałeś wpisywanie pojedyncze")
        print("Wpisane formuły zatwierdzaj klawiszem Enter aby wyświetlić wynik")
    if language == "en":
        print("You have chosen to enter single lines")
        print("Entered formulas confirm with the Enter key to display the result")


def goodbye(language):
    if language == "pl":
        print("\n\033[0mDO ZOBACZENIA!")
        # print("Wesprzyj nas przelewając trochę pieniędzy: <numer_konta>")
        print("© Anna Panfil & Konrad Romański")
    if language == "en":
        print("\n\033[0mSEE YOU SOON!")
        print("© Anna Panfil & Konrad Romański")
