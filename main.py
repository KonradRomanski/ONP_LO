import translate
import sys

def show_image(message):
    a = open("error_art.txt", 'r', encoding="utf-8").read()
    a = f"\033[1;31m  {message[:-5].upper()}  {a}\033[0m"
    return a

def read_whole_list_of_lists(li=[]):
    while (True):
        try:
            list_temp = input().split()
            li.append(list_temp)

        except EOFError:
            print()
            break

        except KeyboardInterrupt:
            print("\n")
            break
        except (ValueError, IndexError):
            print(show_image())
            break
    return li


def print_whole_list_of_lists(li):
    for i in li:
        for j in i:
            print(j, end=" ")
        print()

def read_each_line_separetly():
    while (True):
        try:
            print("\033[36;1m> \033[0m", end="", sep="")
            list_temp = input("\033[1m").split()
            list_temp = translate.to_onp(list_temp)
            # print(list_temp)
            print(f"\033[33;1m{list_temp}\033[0m")

        except EOFError:
            print("\033[0m")
            break

        except KeyboardInterrupt:
            print("\033[0m\n")
            break
        except (ValueError, IndexError) as Error:
            print("\033[0m", end="")
            print(show_image(sys.exc_info()[0].__name__), end="")
            # print(show_image(type(Error).__name__))
            # break

def main():
    ## reading everything and then printing
    # lists = read_whole_list_of_lists()
    # lists_changed = translate.to_onp(lists)
    # print_whole_list_of_lists(lists_changed)

    ## reding each line separetly
    read_each_line_separetly()

if __name__ == "__main__":
    main()
