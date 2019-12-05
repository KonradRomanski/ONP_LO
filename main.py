import onp_translation
import textpika
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--pikatchu",help="Budowa: -p 'język' (en/pl)")
parser.add_argument("-l", "--lines", action='store_true')
lili = parser.parse_args().lines # flaga do okreslenia trybu wczytywania
piki = parser.parse_args().pikatchu #flaga do określenia obecności wiadomości powitalnej i jezyka

def show_image(message):
    a = open("error_art.txt", 'r', encoding="utf-8").read()
    a = f"\033[1;31m  {message[:-5].upper()}  {a}\033[0m"
    return a

def print_whole_list_of_lists(li):
    for i in li:
        print(f"\033[33;1m{i}\033[0m")

def read_data(li = []):
    while (True):
        try:
            # if list_temp == []:
            print("\033[36;1m> \033[0m", end="", sep="")
            list_temp = input("\033[1m").split()

            if list_temp[0] in ("exit", "quit"):
                if piki: textpika.goodbye(piki)
                break

            list_temp = onp_translation.to_onp(list_temp)
            if not lili: print(f"\033[33;1m{list_temp}\033[0m \n")
            else: li.append(list_temp)

        except EOFError:
            print("\033[0m")
            if lili: return li
            if piki != False: textpika.goodbye(piki)
            break

        except KeyboardInterrupt:
            print("\033[0m\n")
            if lili == True: return li
            if piki != False: textpika.goodbye(piki)
            break
        except (ValueError, IndexError) as Error:
            print("\033[0m", end="")
            print(show_image(sys.exc_info()[0].__name__), end="")
            # print(show_image(type(Error).__name__))

def main():
    if piki != False:
        #language = textpika.choose_language()
        textpika.welcome(piki)
        if lili == True: textpika.alllines(piki)
        if lili == False: textpika.everyline(piki)
    if lili == True:
        print_whole_list_of_lists(read_data())
        if piki != False: textpika.goodbye(piki)
    else: read_data()

if __name__ == "__main__":
    main()
