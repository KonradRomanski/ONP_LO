import translate

# Funkcja z pętlą z której aby wyjść podczas wpisywania trzeba nacisnąć Ctrl + d
def lread(li=[]):
    while (True):
        try:
            listt = input().split()
            li.append(listt)

        except EOFError:
            print()
            break

        except KeyboardInterrupt:
            print("\n")
            break
    return li


def lprint(li):
    for i in li:
        for j in i:
            print(j, end=" ")
        print()


def main():
    lists = lread()
    lists_changed = translate.to_onp(lists)
    lprint(lists_changed)


main()
