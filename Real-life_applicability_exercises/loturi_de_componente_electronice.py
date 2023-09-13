"""
LOTURI DE COMPONENTE ELECTRONICE (https://drive.google.com/file/d/1YF9PEBoi6SGSQ-HvBGnoJEbuRr968ad4/view?usp=drive_link)

Gigel a dat comanda de loturi de componente electronice. Printre aceste loturi exista si loturi neconforme.
Loturile care vă sunt utile sunt doar loturile care indeplinesc simutan urmatoarele conditii:
 - au un număr de condensatoare mai mare sau egal cu numărul de tranzistoare
 - numărul de rezistoare mai mare sau egal cu numărul de condensatoare
 - au cel puțin un condensator, un tranzistor și un rezistor.
În plus, vă interesează și lotul cu cele mai multe componente, pentru că din ele o să le mai completați
pe cele lipsă.

CERINTA:
Aflati câte dintre aceste loturi vă sunt utile și câte componente are lotul cel mai mare.

DATE DE INTRARE:
- n = numărul de loturi
- n loturi:
    - k = numarul de componente din lot
    - k litere = componentele lotului:
        - R = rezistor
        - C = condensator
        - T = tranzistor

DATE DE IESIRE:
Două numere întregi:
    - numărul de loturi utile dintre cele citite
    - numărul de componente ale lotului cel mai mare

EXEMPLU:
3
5
R C R T C
5
C R T R T
6
C C T C C T

Se vor citi 3 loturi
Primul lot contine 5 componente:
    - 2 rezistoare
    - 2 condensatoare
    - 1 tranzistor
    => 2 >= 2 >= 1 => lotul este util
Al 2 - lea lot contine 5 componente:
    - 2 rezistoare
    - 1 condensator
    - 2 tranzistoare
    => 2 >= 1 < 2 => lotul nu este util
Al 3 - lea lot contine 6 componente:
    - 0 rezistoare
    - 4 condensatoare
    - 2 tranzistoare
    => 0 < 4 >= 2 => lotul nu este util
Loturi utile = 1
Dimensiunea lotului maxim = 6

=> se afiseaza : 1 6
"""


#set 1 date de intrare
date_intrare = [3, [5, 'R', 'C', 'R', 'T', 'C'], [5, 'C', 'R', 'T', 'R', 'T'], [6, 'C', 'C', 'T', 'C', 'C', 'T']]

#set 2 date de intrare
#date_intrare = [1,[0]]


n = date_intrare[0]  # preiau numarul de loturi
print('Numarul de loturi :', n, '\n')
util = 0  # initializez numarul ed loturi utile
# initializez o lista in care voi pune numarul de componente corespunzator fiecarui lot pentru a afla maximul
lista_nr_comp = []
# pentru fiecare lot
for i in range(n):
    print('Lotul', i + 1)
    k = date_intrare[i + 1][0]  # preiau numarul de componente din lot
    print('Numar componente :', k)
    lista_nr_comp.append(k)  # adaug numarul de componente in lista
    if k != 0:  # daca exista componente
        componente = date_intrare[i+1][1:]  # pun componentele lotului curent in lista
        print('''- {} rezistoare
- {} condenstaoare
- {} tranzistoare'''.format(componente.count('R'), componente.count('C'), componente.count('T')))
        # daca sunt indeplinite simultan conditiile:
        # - exista cel puțin un condensator, un tranzistor și un rezistor
        # - numărul de rezistoare este mai mare sau egal cu numărul de condensatoare
        # - numărul de condensatoare este mai mare sau egal cu numărul de tranzistoare
        if componente.count('C') and componente.count('R') and componente.count('T') \
            and componente.count('T') <= componente.count('C') <= componente.count('R'):
            util += 1  # incrementez numarul de componete utile
            print('Lot util')
        else:
            print('Lot neconform')
    else:
        print('Lotul nu contine componente')
    print('\n')

print('Numarul de loturi utile :', util)
print('Numarul maxim de componente :', max(lista_nr_comp))


"""
DATE DE INTRARE:
3
5
R C R T C
5
C R T R T
6
C C T C C T

DATE DE IESIRE:
1 6 


DATE DE INTRARE:
1
0

DATE DE IESIRE:
0 0 
"""