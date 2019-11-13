import translate

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
    return li


def print_whole_list_of_lists(li):
    for i in li:
        for j in i:
            print(j, end=" ")
        print()

def read_each_line_separetly():
    while (True):
        try:
            list_temp = input().split()
            list_temp = translate.to_onp(list_temp)
            for i in list_temp: print(i, end=" ")
            print()

        except EOFError:
            print()
            break

        except KeyboardInterrupt:
            print("\n")
            break


def main():
    ## reading everything and then printing
    # lists = read_whole_list_of_lists()
    # lists_changed = translate.to_onp(lists)
    # print_whole_list_of_lists(lists_changed)

    ## reding each line separetly
    read_each_line_separetly()

main()
