"""
PERMUTARI CIRCULARE (https://drive.google.com/file/d/1OhCU6KcBo1VAp5LFoSBKd0xoef0kEX-_/view?usp=drive_link)

Într-o permutare circulară, toate cifrele secvenţei date, exceptând-o pe ultima, sunt mutate cu o poziţie spre
dreapta, ultima cifră devenind prima.

CERINTA:
Să se afle cel mai mare număr natural m, scris în baza 10, a cărui scriere în baza 2 se poate obține prin una sau
mai multe permutări circulare ale scrierii în baza 2 a numărului n.

DATE DE INTRARE:
 - n = numarul natural nenul in baza 10 (primul bit din stânga al reprezentării sale în bază 2 trebuie să fie 1)

DATE DE IESIRE:
 - m = numarul natural care are semnificatia din cerinta

EXEMPLU:
n = 13

Scrierea in baza 2 a lui 13 este : 1101 => avem 4 biti => putem avea 4 permutari circulare:
    1101 - 13
    1110 - 14
    0111 - 7
    1011 - 11

Permutarea care genereaza numarul maxim în zecimal este 1110, adică 14 => se afiseaza 14
"""


import math


def formare_numar(lista_biti):
    numar_format = 0
    lista_biti = lista_biti[::-1]  # inversez lista_biti ca sa imi fie usor sa calculez numarul in baza 10
    # formez numarul
    for putere in range(0, len(lista_biti)):
        numar_format += lista_biti[putere] * 2 ** putere
    return numar_format


def permutare(lista_biti):
    lista_biti.insert(0, lista_biti[-1])  # duc ulimul bit in fata listei
    lista_biti.pop()  # sterg bit-ul pe care l-am dus in fata listei
    return lista_biti

def afisare_numar_binar(lista_biti):
    numar_binar = ''  # initializez numarul binar de afisat
    for bit in lista_biti:  # iau fiecare bit din lista
        numar_binar += str(bit)  # si il adaug la numarul binar care urmeaza sa fie afisat
    print(numar_binar)


#set 1 date de intrare
#date_intrare = 13

#set 2 date de intrare
date_intrare = 98765


n = date_intrare

print('Numarul', n, end=' ')
n_baza_2 = []  # initializez o lista pe care o sa o folosesc in stocarea bitilor(0, 1)
# aflu numarul in baza 2 corespunzator lui n
while n > 1:
    n_baza_2.append(n % 2)  # pun resturile impartirilor la 2 in lista
    n = n // 2  # numarul n devine catul impartirii lui n la 2
n_baza_2.append(n)  # pun si ultimul rest in lista
n_baza_2 = n_baza_2[::-1]  # am inversat lista ca sa aflu numarul in baza 2
print('in baza 2 este :', end=' ')
afisare_numar_binar(n_baza_2)

# initializez o lista in care o sa stochez numerele in baza 10 corespunzatoare permutarilor circulare
numere = []
print('Permutarile circulare sunt :')
# fac atatea permutari circulare cate elemente are lista ce contine numarul in baza 2
for i in range(0, len(n_baza_2)):
    n_baza_2 = permutare(n_baza_2)
    afisare_numar_binar(n_baza_2)
    numere.append(formare_numar(n_baza_2))  # adaug numarul in baza 10 corespunzator numarului binar obtinut


print('Numerele provenite din permutarile circulare :', numere)
print('Numarul maxim provenit din permutarile circulare :', max(numere))

"""
DATE DE INTRARE:
13

DATE DE IESIRE:
14


DATE DE INTRARE:
98765

DATE DE IESIRE:
118208
"""