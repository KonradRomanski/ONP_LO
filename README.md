# Logika Obliczeniowa
## Zadanie programistyczne - część I

Zaimplementuj wczytywanie formuł rachunku predykatów w odwrotnej notacji polskiej (ONP) i wypisywanie ich w postaci infiksowej. Formuły w ONP podawane są na standardowe wejście programu,a  ich odpowiedniki powinny być wypisane na standardowe wyjście. Każda formuła na wejściu zapisana jest w nowej linii, w odpowiadających liniach wyjścia powinny być formuły zapisane w postaci infiksowej.

Przyjmij następującą konwencję:

- Kolejne **formuły** na wejściu oddzielone są znakami nowej linii.
- Kolejne **symbole** w obrębie formuły na wejściu oddzielone są spacjami.
- **Stałe** oznaczone są zawsze pojedynczą małą literą alfabetu łacińskiego od `a` do `e`
- **Zmienne** oznaczone są zawsze pojedynczą wielką literą alfabetu łacińskiego
- **Symbole funkcyjne** są zawsze oznaczone pojedynczą małą literą alfabetu łacińskieg od `f` do `n`, po której następuje `/` i jedna cyfra określająca liczbę argumentów (arność) symbolu
- **Symbole predykatywne** są zawsze oznaczone pojedynczą małą literą alfabetu łacińskieg od `p` do `z`, po której następuje `/` i jedna cyfra określająca liczbę argumentów (arność) symbolu
- **Operatory i kwantyfikatory** mogą być oznaczone w jednym ze sposobów opisanych w tabeli (program musi obsługiwać wszystkie warianty)
---
|             Elementy              |      Zapis      | Symbol |
|:---------------------------------:|:---------------:|:------:|
|               stała               |    `a`...`e`    |  `b`   |
|              zmienna              |    `A`...`Z`    |  `C`   |
|         symbol funkcyjny          |    `f`...`n`    | `h/2`  |
|        symbol predykatywny        |    `p`...`z`    | `q/3`  |
|              negacja              | `NOT`, `~`, `¬` |  `¬`   |
|            koniunkcja             | `AND`, `&`, `∧` |  `∧`   |
| alternatywa <br/>(~~dysjunkcja~~) | `OR`, `|`, `∨`  |  `∨`   |
|            implikacja             | `IMPLIES`, `→`  |  `→`   |
|           równoważność            |   `IFF`, `↔`    |  `↔`   |
|     alternatywa wykluczająca      |   `XOR`, `⊕`    |  `⊕`   |
|       kwantyfikator ogólny        |  `FORALL`, `∀`  |  `∀`   |
|     kwantyfikator szczegółowy     |  `EXISTS`, `∃`  |  `∃`   |

### Wejście (przykład):

```py
a p/1
Z Z p/1 EXISTS
Z X X a f/2 p/1 ∃ Y Y Z f/1 p/2 FORALL → FORALL
Z Y X X b c q/3 Z Y f/1 p/2 ~ & EXISTS FORALL EXISTS
```

### Wyjście (przykład):

```py
p(a)
(EXISTS Z p(Z))
(FORALL Z ((∃ X p(f(X, a))) → (FORALL Y p(Y, f(Z)))))
(EXISTS Z (FORALL Y (EXISTS X (q(X, b, c) & (~ p(Z, f(Y)))))))
```
<br/>

[link do oryginalnego opisu](https://moodle.put.poznan.pl/mod/page/view.php?id=53864)
