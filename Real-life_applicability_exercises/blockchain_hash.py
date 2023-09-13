"""
BLOCKCHAIN HASH (https://drive.google.com/file/d/1bMRleQAIs-PF-p8bB4YDNrDjyEp3zDjg/view?usp=drive_link)

Algoritm de hash:
- Dacă numărul are cel puțin două cifre, se iau pe rând din număr câte două cifre vecine și se scade cea mai mică
din cea mai mare. Cu cifrele astfel obținute se formează un nou număr.
- Dacă numărul este format dintr-o singură cifră, transformarea îl lasă nemodificat.
- Hash-ul se calculează realizând succesiv transformarea asupra numărului original și apoi asupra rezultatului
obținut, de k ori, și sumând toate rezultatele parțiale și rezultatul final (excluzând valoarea de start).

CERINTA:
Se cere să se determine valoarea maximă a hash-ului care se va obține aplicând algoritmul de hash celor N numere
folosind k iterații de transformare.

DATE DE INTRARE:
- două numere naturale:
    - N = numarul de numere
    - k = numarul de iteratii
- N numere

DATE DE IESIRE:
- valoarea maximă dintre toate hash-urile obținute conform procedeului descris anterior.

EXEMPLU:
2 2
5734 1234

N = 2 numere
K = 2 iteratii

Numarul 5734:
    -> iteratia 1
        7 - 5 = 2
        7 - 3 = 4
        4 - 3 = 1
    -> se formeaza numarul 241
    -> iteratia 2
        4 - 2 = 2
        4 - 1 = 3
    -> se formeaza numarul 23
    -> se aduna rezultatele partiale cu cel final => 241 + 23 = 264

Numarul 1234:
    -> iteratia 1
        2 - 1 = 1
        3 - 1 = 1
        4 - 1 = 1
    -> se formeaza numarul 111
    -> iteratia 2
        1 - 1 = 0
        1 - 1 = 0
    -> se formeaza numarul 0
    -> se aduna rezultatele partiale cu cel final => 111 + 0 = 111

Se afla maximul dintre 264 si 111 => se afiseaza 264
"""


#set 1 date de intrare
date_intrare = [2, 2, '5734', '1234']

#set 2 date de intrare
#date_intrare = [2, 3, '2228', '6']


def formare_numar(lista):
    numar_format = 0
    lista = lista[::-1]  # inversez lista pentru a putea forma numarul mai usor
    for poz in range(len(lista)):
        numar_format += lista[poz] * 10 ** poz
    return numar_format



N = date_intrare[0]  # numarul de numere
k = date_intrare[1]  # numarul de iteratii


print('Date de intrare :', date_intrare)
print('Numarul de numere N =', N)
print('Numarul de iteratii k =', k)
numar_lista = []  # in aceasta lista adaug cifrele numarului pentru care este aplicat algoritmul

maxim = 0  # maximul dintre sume(data de iesire)

numere = date_intrare[2:]  # adaug numerele pentru care trebuie sa aplic algoritmul intr-o lista

print('Numerele pentru care se aplica algoritmul :', numere)
for i in range(N):  # pentru fiecare numar din cele N numere
    suma = 0  # suma rezultatelor partiale si a rezultatului final
    # iau fiecare cifra din numar(este de tip str pentru a putea lua cifrele mai usor)
    for caracter in numere[i]:
        numar_lista.append(int(caracter))  # si o adaug la lista care contine cifrele numarului
    print('Pentru numarul', numere[i])
    if len(numar_lista) == 1:  # daca numarul are o singura cifra
        suma = numar_lista[0] * k  # suma va fi acea cifra adunata de k(numarul de interatii) ori
        print('Numarul are o singura cifra => Suma pentru toate iteratiile = {} * {}'.format(numar_lista[0], k))
    else:  # daca numarul are mai mult de o cifra
        for iteratie in range(k):  # pentru fiecare iteratie din cele k iteratii
            for cifra in range(len(numar_lista) - 1):  # pentru fiecare cifra din numar
                if len(numar_lista) > 1:  # daca exista mai multe cifre decat 1
                    # fac diferenta dintre cifra curenta si urmatoarea si aflu modulul
                    # (cifra maxima - cifra minima dintre cele 2 cifre)
                    numar_lista[cifra] = abs(numar_lista[cifra] - numar_lista[cifra+1])
                elif len(numar_lista) == 1:  # daca exista o singura cifra
                    # suma devine acea cifra adunata de (k - iteratie) = numarul de iteratii ramase ori
                    suma += numar_lista[0] * (k - iteratie)
            if numar_lista:  # daca lista are elemente(cifre)
                numar_lista.pop()  # sterg ultimul element
                suma += formare_numar(numar_lista)  # iar la suma se aduna numarul format din cifrele din lista
                print('Suma dupa iteratia', iteratie, '=', suma)
    # maximul dintre sume
    if suma > maxim:
        maxim = suma
    # curat lista in cazul in care nu au existat suficiente iteratii ca toate elementele listei sa fie sterse
    numar_lista = []
    print('Suma pentru numarul', numere[i],  ':', suma)
print('Suma maxima este :', maxim)

"""
DATE DE INTRARE:
2 2
5734 1234

DATE DE IESIRE:
264


DATE DE INTRARE:
2 3
2228 6

DATE DE IESIRE:
18
"""