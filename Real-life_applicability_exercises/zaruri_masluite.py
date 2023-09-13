"""
ZARURI MASLUITE (https://drive.google.com/file/d/1CyJSFmjQBqPS4fiwnyaWkd9c5O3IEN7u/view?usp=drive_link)

Neavând cu cine să joace zaruri dar părându-i-se că unele din zaruri sunt mai grele decât celelalte, Costică a
ales un zar și s-a apucat să îl testeze aruncând cu el și notând de câte ori a picat fiecare față. Încearcă apoi
să-și dea seama dacă zarul e măsluit sau nu, considerând că diferența dintre numărul maxim de apariții a unei
fețe și numărul minim de apariții (a oricăror alte fețe) nu trebuie să depășească 10% din numărul total de
aruncări.

CERINTA:
- să se determine dacă zarul e măsluit conform condiției de mai sus

DATE DE INTRARE:
- N = numărul de aruncări cu zarul
- N linii = numerele obținute la aruncări

DATE DE IESIRE:
- 1 - zarul este masluit
- 0 - zarul este normal

EXEMPLU:
Date de intrare:
10
6
6
6
6
6
6
6
6
6
6

Se aruncă cu zarul de 10 ori -> toate aruncarile produc numarul 6 => diferenta dintre numărul maxim de apariții
(10) și numărul minim de apariții (0) este mai mare strict decât 10% din numărul total de aruncări (10% din 10
este 1) => zarul este masluit

Date de iesire:
1
"""


# SET 1 DATE DE INTRARE

date_intrare = '''10
6
6
6
6
6
6
6
6
6
6'''


# SET 2 DATE DE INTRARE
"""
date_intrare = '''10
1
4
2
5
4
6
2
1
3
3'''
"""


def inserare(aparitie):
    if aparitii.get(aparitie):
        aparitii[aparitie] += 1
    else:
        aparitii[aparitie] = 1


date_intrare = date_intrare.splitlines()

N = int(date_intrare[0])
print('Numarul de aruncari :', N)
aparitii = {}  # initializez un dictionar in care voi pune fiecare numar, respectiv de cate ori apare
# inserez aparitiile in dictionar
for i in range(N):
    aparitie = date_intrare[i + 1]
    inserare(aparitie)


def afisare(diferenta):
    # verific daca se indeplinste conditia din enunt
    if diferenta > 0.1 * N:
        print('1 -> zarul este masluit')
    else:
        print('0 -> zarul este normal')


print('Aparitii :', aparitii)
afisare(max(aparitii.values()) - min(aparitii.values()))

"""
DATE DE INTRARE:
10
6
6
6
6
6
6
6
6
6
6

DATE DE IESIRE:
1


DATE DE INTRARE:
10
1
4
2
5
4
6
2
1
3
3

DATE DE IESIRE:
0
"""