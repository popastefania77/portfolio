"""
CAPIONAT DE FOTBAL (https://drive.google.com/file/d/1w8C6zlgDSdzMSsQl9lfz_2S63s5atNFt/view?usp=drive_link)

Fotbalul se joacă pe goluri, astfel că o echipă este declarată câştigătoare dacă înscrie mai multe goluri decât
cealaltă. Dacă ambele echipe înscriu la fel de multe goluri, meciul este declarat remiză. Este cunoscut faptul că :
- o victorie se punctează cu 3 puncte
- o remiză cu un punct
- în cazul unei înfrângeri echipa în cauză nu primeşte niciun punct
La finalul campionatului, echipele sunt ordonate în funcţie de numărul de puncte acumulate, cea cu cele mai multe
puncte câştigând trofeul.

CERINTA:
- stabiliţi clasamentul final al campionatului de fotbal pe baza rezultatelor directe între echipele participante

DATE DE INTRARE:
- k = numărul de echipe participante
- n = numărul de meciuri disputate în campionat
- n linii = rezultatele celor n meciuri disputate
# cele n linii sunt de forma <Nume echipa 1> <Numar goluri echipa 1> – <Numar goluri echipa 2> <Nume echipa 2>

DATE DE IESIRE:
- lista de k echipe participante, sortată în ordinea numărului de puncte
# cele k linii vor fi de forma <Nume echipa> <Numar puncte> <Numar goluri inscrise> < Numar goluri primite>

EXEMPLU:
Date de intrare:
4
6
Romania 4 – 0 Franta
Italia 2 – 1 Rusia
Franta 3 – 0 Italia
Rusia 2 – 2 Romania
Romania 1 – 0 Italia
Franta 2 – 1 Rusia

- Romania: 3 puncte din meciul cu Franta + 1 punct din meciul cu Rusia + 3 puncte din
meciul cu Italia. 7 goluri înscrise (4 cu Franta, 2 cu Rusia şi 1 cu Italia). 2 goluri primite
(2 cu Rusia)
- Italia: 3 puncte din meciul cu Rusia + 0 puncte din meciul cu Franta + 0 puncte din
meciul cu Romania. 2 goluri înscrise (2 cu Rusia). 5 goluri primite (1 cu Rusia, 3 cu
Franta, 1 cu Romania)

Date de iesire:
Romania 7 7 2
Franta 6 5 5
Italia 3 2 5
Rusia 1 4 6
"""


def initializare(nume_echipa1, nume_echipa2):
    # verific daca exista numele echipei in fiecare dintre cele 3 dictionare,
    # daca nu exista initializez punctele si golurile inscrise/primite cu 0
    if not d_puncte.get(nume_echipa1, None):
        d_puncte[nume_echipa1] = 0
        
    if not d_puncte.get(nume_echipa2, None):
        d_puncte[nume_echipa2] = 0
        
    if not d_goluri_inscrise.get(nume_echipa1, None):
        d_goluri_inscrise[nume_echipa1] = 0
        
    if not d_goluri_inscrise.get(nume_echipa2, None):
        d_goluri_inscrise[nume_echipa2] = 0
        
    if not d_goluri_primite.get(nume_echipa1, None):
        d_goluri_primite[nume_echipa1] = 0
        
    if not d_goluri_primite.get(nume_echipa2, None):
        d_goluri_primite[nume_echipa2] = 0

def puncte_goluri(nume_echipa1, nr_gol_echipa1, nr_gol_echipa2, nume_echipa2):
    if nr_gol_echipa1 > nr_gol_echipa2:
        d_puncte[nume_echipa1] += 3  # echipa1 are scor mai mare -> primeste 3 puncte
        
    elif nr_gol_echipa1 < nr_gol_echipa2:
        d_puncte[nume_echipa2] += 3  # echipa2 are scor mai mare -> primeste 3 puncte
       
    else:
        # remiza -> fiecare echipa primeste cate un punct
        d_puncte[nume_echipa1] += 1
        d_puncte[nume_echipa2] += 1
    # actualizez numarul de goluri inscrise/primite pentru fiecare echipa
    d_goluri_inscrise[nume_echipa1] += nr_gol_echipa1
    d_goluri_inscrise[nume_echipa2] += nr_gol_echipa2
    d_goluri_primite[nume_echipa1] += nr_gol_echipa2
    d_goluri_primite[nume_echipa2] += nr_gol_echipa1
    

# functie echivalenta cu lambda x: x[1]
def valoare(x):
    return x[1] 


# SET 1 DATE DE INTRARE:
date_intrare = '''4
6
Romania 4 – 0 Franta
Italia 2 – 1 Rusia
Franta 3 – 0 Italia
Rusia 2 – 2 Romania
Romania 1 – 0 Italia
Franta 2 – 1 Rusia'''

date_intrare = date_intrare.splitlines()

k = int(date_intrare[0])
n = int(date_intrare[1])

print('Numărul de echipe participante :', k)
print('Numărul de meciuri disputate în campionat :', n)

d_puncte = {}
d_goluri_inscrise = {}
d_goluri_primite = {}

print('Meciurile sunt :')
for i in range(0, n):
    nume_echipa1, nr_gol_echipa1, char, nr_gol_echipa2, nume_echipa2 = date_intrare[i + 2].split()
    print(nume_echipa1, nr_gol_echipa1, char, nr_gol_echipa2, nume_echipa2)
    nr_gol_echipa1 = int(nr_gol_echipa1)
    nr_gol_echipa2 = int(nr_gol_echipa2)

    initializare(nume_echipa1, nume_echipa2)
    puncte_goluri(nume_echipa1, nr_gol_echipa1, nr_gol_echipa2, nume_echipa2)


# sortez dictionarul
d_puncte = sorted(d_puncte.items(), key=valoare, reverse=True) # returneaza o lista
# d_puncte.items()-> returnează un obiect dict_items care conține tupluri cu perechile (cheie, valoare)
# key=valoare -> sortez dupa valoare (d_puncte.items()[1])

# convertesc lista in dictionar
d_puncte = dict(d_puncte)

# afisez clasamentul
print('\nClasamentul final :')
for echipa in list(d_puncte.keys()):
    print(echipa, d_puncte.get(echipa), d_goluri_inscrise.get(echipa), d_goluri_primite.get(echipa))
    

"""
DATE DE INTRARE:
4
6
Romania 4 – 0 Franta
Italia 2 – 1 Rusia
Franta 3 – 0 Italia
Rusia 2 – 2 Romania
Romania 1 – 0 Italia
Franta 2 – 1 Rusia

DATE DE IESIRE:
Romania 7 7 2
Franta 6 5 5
Italia 3 2 5
Rusia 1 4 6

"""



    
