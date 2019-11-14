single_argument = {"NOT", "~", "¬"}
double_argument = {"AND", "&", "∧", "OR", "|", "∨", "IMPLIES", "→", "IFF", "↔", "XOR", "⊕"}
quantifiers = {"FORALL", "∀","EXISTS", "∃"}
functions = {"f", "g", "h", "i", "j", "k", "l", "m", "n"}
predicats = {"p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}

def to_onp(li):
    i = 0
    while i < len(li):
        print("@", li[i])
        while (li[i].isalpha()) and (len(li[i]) == 1):         # znajduje następny operator
            i += 1
            print("@", li[i])
        # pobiera tyle argumentów, ile mu potrzebne
        if li[i] in single_argument:                          # operatory 1-argumentowe
            li[i-1] = f"{li[i]} {li.pop(i-1)}"
            print("##", li)                                   # do operatora dopisuje argument, na który operator działa (poprzedni element z tablicy)

        elif li[i] in double_argument:                        # operatory 2-argumentowe
            arg1 = li.pop(i - 2)                              # pobiera 2 argumenty (2 poprzednie elementy tablicy)
            arg2 = li.pop(i - 2)
            i -= 2
            li[i] = f"({arg1} {li[i]} {arg2})"
            i += 1
            print("##", li)

        elif li[i] in quantifiers:
            j=i-1
            while (not(li[i].isalpha()) and (len(li[i]) != 1)):         # znajduje następny operator
                j -= 1
                print("#", j)
            j -= 1
            print("#", j)
            arg1 = li[j]
            arg2=""
            for k in range (j+1, i):
                arg2 += li[k] + " "
            #arg2 = li[j+1:i]
            # arg2 = li.pop(i-2)                        # zmienna kwantyfikowana
            # arg2 = li.pop(i-1)                        # wyrazenie
            li[i] = f"{li[i]} {arg1} {arg2}"
            i += 1
            print("##", li)

        elif li[i][0] in predicats or functions:
            for j in range(int(li[i][2])):
                li[i-1] = f"{li.pop(i)} {li[i-1]},"
                i -= 1
            li[i] = f"{li[i][0]}({li[i][4:len(li[i])-1]})"
            i += 1
            print("##", li)

    return li
