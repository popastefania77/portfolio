"""
CAZINO (https://drive.google.com/file/d/1GjAgEtgEBB3RQlSHIebI-kQdebMjDJ_3/view?usp=drive_link)

Se dorește să se descopere dacă vreunul dintre jucatori a scos cărți din buzunar. Jocul monitorizat se joacă cu
două pachete clasice (52 de cărți fiecare, fără Joker).

CERINTA:
Scrieți un program care să ajute la detectarea trișorilor.

DATE DE INTRARE:
- n = numarul maxim de maini ce vor fi jucate
- n linii = n carti de joc(<număr_carte> <semn_carte>)

DATE DE IESIRE:
- JOC OK -> in cazul in care nimeni nu vrea sa triseze
- cartea problema -> in cazul in care cineva a incercat sa triseze

EXEMPLU:
5
2 trefla
11 caro
14 cupa
14 pica
6 caro

Nicio carte nu a fost jucata de 3 ori => jocul decurge normal => se afiseaza: JOC OK
"""


#set 1 date de intrare
#date_intrare = [5, '2 trefla', '11 caro', '14 cupa', '14 pica', '6 caro']

#set 2 date de intrare
#date_intrare = [7, '2 trefla', '11 caro', '11 caro', '11 caro', '14 cupa', '14 pica', '6 caro']

#set 3 date de intrare
#date_intrare = [7, '2 trefla', '11 caro', '11 caro', '6 caro', '11 caro', '14 cupa', '14 pica']

#set 4 date de intrare
date_intrare = [8, '11 caro', '11 pica', '11 caro', '11 pica', '11 pica', '11 caro', '14 pica', '6 caro']


n = date_intrare[0]
print('Numarul maxim de maini ce vor fi jucate :', n)
carti = {}  # initializez un dictionar in care pun cartile, respectiv numarul de carti de fiecare fel

def adaugare(carte):
    if not carti.get(carte, None):  # daca cartea nu exista in dictionar
        carti[carte] = 1  # o adaug
    else:  # daca exista in dictionar
        carti[carte] += 1  # cresc numarul de aparitii

def verificare(carte):
    if carti[carte] == 3:  # daca respectiva carte a aparut de 3 ori
        print(carte)  # o afisez
        return 1

contor = 0
for index in range(0, n):
    carte = date_intrare[index + 1]  #preiau cartea
    adaugare(carte)  # adaug cartea in dictionar
    if verificare(carte) == 1:  # daca respectiva carte a aparut de 3 ori
        contor = 1
        break  # intrerup programul
    #print(contor)
    #print(carti)
if contor == 0:
    print('JOC OK')
    
"""
DATE DE INTRARE:
5
2 trefla
11 caro
14 cupa
14 pica
6 caro

DATE DE IESIRE:
JOC OK


DATE DE INTRARE:
7
2 trefla
11 caro
11 caro
11 caro
14 cupa
14 pica
6 caro

DATE DE IESIRE:
11 caro


DATE DE INTRARE:
7
2 trefla
11 caro
11 caro
6 caro
11 caro
14 cupa
14 pica

DATE DE IESIRE:
11 caro


DATE DE INTRARE:
8 (greseala in pdf -> sunt 8 carti dar n = 7)
11 caro
11 pica
11 caro
11 pica
11 pica
11 caro
14 pica
6 caro

DATE DE IESIRE:
11 pica
"""