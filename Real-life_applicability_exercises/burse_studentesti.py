"""
BURSE STUDENTESTI (https://drive.google.com/file/d/1gL5X6Lfmv5_2Bv1twS-Bs_DiSm4fuCZh/view?usp=drive_link)

Bursa de performanță se acordă studentului integralist cu media cea mai mare.
Bursele de merit se acordă în ordinea descrescătoare a mediilor, în limita numărului maxim de burse, tuturor
studenților integraliști care au media generală peste 8.00.

CERINTA:
Stabiliți ce student va lua bursă de performanță și câți studenți vor lua bursă de merit în anul
universitar următor.

DATE DE INTRARE:
- m = numărul de studenţi
- n = numărul de discipline
- p = numărul de burse de merit disponibile
- 2 * m linii = numele studentilor respectiv cele n medii

DATE DE IESIRE:
- numărul de studenți ce vor lua bursă de merit
- numele studentului care va lua bursă de performanță și media media lui

EXEMPLU:
6 3 2
George Popescu
9 9 9
Dan Pop
10 4 10
Ionela Cristescu
6 8 8
Ilie David
10 10 10
Georgiana Fus
9 10 10
Cristian Oprescu
8 9 9

Ilie David este studentul integralist cu cea mai mare medie, deci va primi bursa de performanță.
Dan Pop nu poate primi bursă pentru că nu este integralist.
Ionela Cristescu nu poate primi bursă pentru că are media sub 8.
Georgiana Fus, George Popescu și Cristian Oprescu îndeplinesc condițiile de a primi bursă, însă doar doi dintre
ei vor fi bursieri pentru că numărul maxim de burse de merit este 2.

=> se afiseaza
2
Ilie David 10.00
"""


# set 1 date de intrare
"""
date_intrare = [6, 3, 2, ['George Popescu', 9, 9, 9], ['Dan Pop', 10, 4, 10], ['Ionela Cristescu', 6, 8, 8],
                ['Ilie David', 10, 10, 10], ['Georgiana Fus', 9, 10, 10], ['Cristian Oprescu', 8, 9, 9]]
"""
# set 2 date de intrare

date_intrare = [6, 3, 5, ['George Popescu', 9, 9, 9], ['Dan Pop', 10, 4, 10], ['Ionela Cristescu', 6, 8, 8],
                ['Ilie David', 10, 10, 10], ['Georgiana Fus', 9, 10, 10], ['Cristian Oprescu', 8, 9, 9]]


m, n, p = date_intrare[0:3]
print('Numarul de studenti :', m)
print('Numarul de discipline :', n)
print('Numarul de burse de merit disponibile :', p)
d = {}  # intializez dictionarul pe care il voi utiliza

for i in range(m):
    # preiau numele studentului
    nume = date_intrare[i + 3][0]
    # preiau notele de la input intr - o lista
    note = date_intrare[i + 3][1:]
    # initializez o suma si un contor cu 0 pentru fiecare student
    contor = 0
    suma = 0
    for nota in note:
        # verific daca notele sunt indeplinesc criteriul de promovare
        if int(nota) > 4:
            suma += int(nota)
            contor += 1
    # calculez media pentru fiecare student
    media = suma/contor      
    # daca toate notele sunt de trecere si media este mai mare si egal decat 8 adaug studentul si media in dictionar
    if (contor == n) & (media >= 8):
        d[media] = nume

# verific daca numarul de burse de merit disponibile sunt suficiente si afisez numarul de burse acordate
if len(d.keys()) - 1 < p:  # am pus - 1 deoarece cel care ia bursa de performanta nu mai intra in discutie
    print('Numarul de bursieri :', len(d.keys()) - 1)
else:
    print('Numarul de bursieri :', p)



# verific care medie este cea mai mare (bursa de performanta)
cheie = max(list(d.keys()))

# afisez numele,prenumele si media studentului care ia bursa de performanta 
print('Studentul care ia bursa de performanta este :', d.get(cheie, None), "si are media : {:.2f}".format(max(
    list(d.keys()))))

"""
DATE DE INTRARE:
6 3 2
George Popescu
9 9 9
Dan Pop
10 4 10
Ionela Cristescu
6 8 8
Ilie David
10 10 10
Georgiana Fus
9 10 10
Cristian Oprescu
8 9 9

DATE DE IESIRE:
2
Ilie David 10.00


DATE DE INTRARE:
6 3 5
George Popescu
9 9 9
Dan Pop
10 4 10
Ionela Cristescu
6 8 8
Ilie David
10 10 10
Georgiana Fus
9 10 10
Cristian Oprescu
8 9 9

DATE DE IESIRE:
3
Ilie David 10.00
"""