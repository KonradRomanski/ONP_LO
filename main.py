import translate

# Funkcja z pętlą z której aby wyjść podczas wpisywania trzeba nacisnąć Ctrl + d
def lread(li=[]):
    while (True):
        try:
            listt = input().split()
            li.append(listt)

        except (EOFError):
            break
    return li


def lprint(li):
    for i in enumerate(li):
        for j in li[i[0]]:
            print(j, end=" ")
        print("")


def main():
    lists = lread()
    lists_changed = translate.to_onp(lists[0])
    lprint(lists_changed)


main()
