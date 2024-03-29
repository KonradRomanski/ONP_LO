single_argument = ["NOT", "~", "¬"]
double_argument = ["AND", "&", "∧", "OR", "|", "∨", "IMPLIES", "→", "IFF", "↔", "XOR", "⊕"]
quantifiers = ["FORALL", "∀","EXISTS", "∃"]
functions = list(map(chr, range(ord('f'), ord('n')+1)))
predicats = list(map(chr, range(ord('p'), ord('z')+1)))
constants = list(map(chr, range(ord('a'), ord('e')+1)))
variables = list(map(chr, range(ord('A'), ord('Z')+1)))

def to_onp(li):
    i = 0
    while i < len(li):
        while (li[i] in (constants + variables)):
            i += 1          # znajduje następny operator
        # pobiera tyle argumentów, ile mu potrzebne
        if li[i] in single_argument:                          # operatory 1-argumentowe
            li[i-1] = f"({li[i]} {li.pop(i-1)})"
            # print("##", li)                                 # do operatora dopisuje argument, na który operator działa (poprzedni element z tablicy)

        elif li[i] in double_argument:                        # operatory 2-argumentowe
            arg1 = li.pop(i - 2)                              # pobiera 2 argumenty (2 poprzednie elementy tablicy)
            arg2 = li.pop(i - 2)
            i -= 2
            li[i] = f"({arg1} {li[i]} {arg2})"
            i += 1
            # print("##", li)

        elif li[i] in quantifiers:
            j=i-1

            while not(li[j] in (constants + variables)):
                j -= 1
            arg1 = li.pop(j)              # zmienna kwantyfikowana
            i -= 1
            while j!=i-1:                 # zasieg kwantyfikatora
                li[j] = f"{li[j]} {li.pop(j+1)}"
                i -= 1
            li[j] = f"({li.pop(i)} {arg1} {li[j]})"
            # print("##", li)

        elif li[i][0] in (predicats + functions):
            if int(li[i][2]) == 0:
                li[i] = f"{li[i][0]}()"
                i += 1
            else:
                for j in range(int(li[i][2])):
                    li[i-1] = f"{li.pop(i)} {li[i-1]},"

                    i -= 1
                    s = li[i][4:].split()
                    s.reverse()
                    s = "_".join(s)
                li[i] = f"{li[i][0]}({s[:-1]})"
                i += 1
                # print("##", li)
        else:
            raise ValueError('Invalid value found')
    a = li.pop().replace("_", " ")
    if len(li) != 0:
        raise  IndexError

    return a
