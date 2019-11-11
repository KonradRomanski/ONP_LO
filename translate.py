def to_onp(li):
    i = 0
    while i < len(li):
        while (li[i].isalpha()) and (len(li[i]) == 1):         # znajduje następny operator
            i += 1
        # pobiera tyle argumentów, ile mu potrzebne
        if li[i] in {"NOT"}:                                    # operatory 1-argumentowe
            li[i-1] = li[i] + " " + li.pop(i-1)                    # do operatora dopisuje argument, na który operator działa (poprzedni element z tablicy)
        elif li[i] in {"FORALL", "EXIST"}:
            print()
        elif li[i] in {"AND", "OR", "IMPLIES", "IFF", "XOR"}:  # operatory 2-argumentowe
            arg1 = li.pop(i - 2)                                   # pobiera 2 argumenty (2 poprzednie elementy tablicy)
            arg2 = li.pop(i - 2)
            i -= 2
            li[i] = arg1 + " " + li[i] + " " + arg2
            i += 1
        else:                                                  # predykaty
            print()
    return li