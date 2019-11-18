def choose_language():
    print("pl/en ?")
    language = input()
    while language not in ("pl", "en"):
        print(show_image())
        language = input()
    return language


def welcome(language):
    if language == "pl":
        print("------ZAMIANA ODWROTNEJ NOTACJI POLSKIEJ NA NOTACJĘ INFIKSOWĄ------ \n")
        print("Jeżeli chcesz zamienić wiele wyrażeń na raz, wybierz")
        print("Jeżeli chcesz wyjść z programu wpisz 'exit' lub 'quit' /n")
        print("W przeciwnym przypadku wpisz swoją formułę: ")
    if language == "en":
        print("------CHANGING REVERSED POLISH NOTATION TO INFIX NOTATION------ \n")
        print("If you want to change many expressions at once, type 1")
        print("If you want to exit program, type 'exit' or 'quit' /n")
        print("Otherwise enter your expression: ")

def goodbye(language):
    if language == "pl":
        print("DO ZOBACZENIA!")
        # print("Wesprzyj nas przelewając trochę pieniędzy: <numer_konta>")
        print("© Anna Panfil & Konrad Romański")
    if language == "en":
        print("SEE YOU SOON!")
        print("© Anna Panfil & Konrad Romański")

###propozycja działania maina
def main():
    language = textpika.choose_language()
    textpika.welcome(language)
    choice = input()

    if choice == "1":
        ## reading everything and then printing
        lists = read_whole_list_of_lists()
        lists_changed = translate.to_onp(lists)
        print_whole_list_of_lists(lists_changed)
    elif choice in ("quit, exit"):
        textpika.goodbye(language)
        return None
    else:
        ## reding each line separetly
        read_each_line_separetly(choice.split())
