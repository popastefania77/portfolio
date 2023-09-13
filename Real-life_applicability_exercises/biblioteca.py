"""
BIBLIOTECA (https://drive.google.com/file/d/1-C0u8cGZCbhgqEVz4y-QLmf8It9UdDwz/view?usp=drive_link)

Urmărind să ocupe cât mai puţine rafturi, bibliotecara şi-a propus să aranjeze cărţile pe rafturi:
- raft după raft,
- alegând întotdeauna să completeze raftul curent cu cea mai groasă carte disponibilă,
- trecând la următorul raft numai în condiţiile în care pe raftul curent nu mai poate fi plasată nicio carte
dintre cele rămase şi
- asigurându-se că a plasat pe rafturi toate cărţile.

CERINTA:
Scrieţi un program care o poate ajuta pe bibliotecară să aranjeze cărţile pe rafturi în mod eficient,
conform regulilor enunţate mai sus.

DATE DE INTRARE:
- D = dimensiunea rafturilor exprimată în număr de pagini
- k = numărul de dimensiuni diferite pentru cărţile ce trebuie aranjate în bibliotecă
- k linii * numărul de cărţi n de grosime p pagini ce trebuie aranjate în bibliotecă
# Cele k linii ce conțin informații despre cărți sunt date în ordinea inversă a grosimii p

DATE DE IESIRE:
- m linii = m rafturi pe care a fost plasată cel puţin o carte, în ordinea completării lor (conform regulilor):
    - dimensiunile cărţilor
ce au fost plasate pe acel raft, în ordinea plasării lor pe raft (conform regulilor)

EXEMPLU:
200 5
2 130
4 120
2 80
3 60
7 50

Au fost completate 8 rafturi astfel:

Raftul #1:
- cea mai groasă carte disponibilă (130 pag),
- apoi cea mai groasă carte disponibilă (60 pag) care mai încape pe acest raft (200 -130 = 70 pag),
- alte cărţi nu mai încap în spaţiul rămas: 70-60 = 10 pagini.
=> se afiseaza : 130 60

Raftul #2: identic cu raftul #1.
=> se afiseaza : 130 60

Raftul #3:
- cea mai groasă carte disponibilă (120 pag),
- apoi cea mai groasă carte disponibilă (80 pag) care mai încape pe acest raft (200 -120 = 80 pag),
- alte cărţi nu mai încap pe raft – acesta este completat în întregime.
=> se afiseaza : 120 80

Raftul #4: identic cu raftul #3.
=> se afiseaza : 120 80

Raftul #5:
- cea mai groasă carte disponibilă (120 pag),
- apoi cea mai groasă carte disponibilă (60 pag) care mai încape pe acest raft (200 -120 = 80 pag),
- alte cărţi nu mai încap în spaţiul rămas: 80-60 = 20 pagini.
=> se afiseaza : 120 60

Raftul #6:
- cea mai groasă carte disponibilă (120 pag),
- apoi cea mai groasă carte disponibilă (50 pag) care mai încape pe acest raft (200 -120 = 80 pag),
- alte cărţi nu mai încap în spaţiul rămas: 80-50 = 30 pagini.
=> se afiseaza : 120 50

Raftul #7:
- cea mai groasă carte disponibilă (50 pag),
- apoi, în ordine, cele mai groase cărţi disponibile care mai încape pe acest raft: 50, 50, 50,
- alte cărţi nu mai încap pe raft – acesta este completat în întregime.
=> se afiseaza : 50 50 50 50

Raftul #8:
- cea mai groasă carte disponibilă (50 pag),
- apoi, în ordine, cele mai groase cărţi disponibile care mai încape pe acest raft: 50,
- au fost epuizate toate cărţile.
=> se afiseaza : 50 50
"""


# set 1 date de intrare
"""
date_intrare = '''200 5
2 130
4 120
2 80
3 60
7 50
'''
"""

# set 2 date de intrare

date_intrare = '''1100 6
4 187
10 123
9 105
2 97
5 84
3 28
'''


linii = date_intrare.splitlines()

D, k = map(int, linii[0].split())
print('Dimensiunea rafturilor :', D, 'pagini')
print('Exista', k, 'dimensiuni diferite pentru cărţile ce trebuie aranjate în bibliotecă :')

carti = {}
for i in range(1, k + 1):
    n, p = map(int, linii[i].split())
    carti[p] = n  # cheile sunt ordonate descrescator (din enunt)
    print('-', n, 'carti de grosime', p, 'pagini')


def adaugare_carte_raft():
    global pagini, numar_pagini_raft
    print(pagini[index], end=' ')  # printez numarul de pagini
    carti[pagini[index]] -= 1  # scot cartea respectiva din lista
    numar_pagini_raft -= pagini[index]  # actualizez numarul de pagini care incap in raft
    if carti[pagini[index]] == 0:  # daca nu mai exista carti cu numarul respectiv de pagini
        del carti[pagini[index]]  # sterg cartea din dictionar
        pagini = list(carti.keys())  # actualizez numarul de pagini pe care le au cartile din biblioteca

numar_raft = 0
# atata timp cat exista carti
while len(carti) > 0:
    numar_raft += 1
    # retin dimensiunea rafturilor intr-o variabila pentru a o putea actualiza (o sa am nevoie de D nemodificat
    # pentru fiecare iteratie)
    numar_pagini_raft = D
    pagini = list(carti.keys())  # extrag numarul de pagini pe care le au cartile din biblioteca
    print('Raftul', numar_raft, ':', end='\n')
    # cat timp lista de pagini nu este goala (epuizata) si exista cel putin o carte care sa mai incapa in raft
    while pagini and numar_pagini_raft >= min(pagini):
        maxim = 0  # cartea cu numarul maxim de pagini care poate incapea in raft
        for i in range(len(pagini)):  # parcurg toate cartile
            # aflu cartea cu numarul maxim de pagini ce poate incapea in raft
            if maxim < pagini[i] <= numar_pagini_raft:
                maxim = pagini[i]
                index = i
        if maxim:  # daca exista o carte care sa incapa in raft
            adaugare_carte_raft()
    print('\n')
print('Au fost epuizate toate cartile')

"""
DATE DE INTRARE:
200 5
2 130
4 120
2 80
3 60
7 50

DATE DE IESIRE:
130 60
130 60
120 80
120 80
120 60
120 50
50 50 50 50
50 50

DATE DE INTRARE:
1100 6
4 187
10 123
9 105
2 97
5 84
3 28

DATE DE IESIRE:
187 187 187 187 123 123 105
123 123 123 123 123 123 123 123 105
105 105 105 105 105 105 105 97 97 84 84
84 84 84 28 28 28
"""