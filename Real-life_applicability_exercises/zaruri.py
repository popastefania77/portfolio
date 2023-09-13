"""
ZARURI (https://drive.google.com/file/d/1-jg4UGSBiME4QUH1BPwWFs8KIk8hMidp/view?usp=drive_link)

Costica a gasit niste zaruri si s-a apucat să le clădească, unul peste celălalt, cât de sus a putut.

CERINTA:
- Dându-se un număr N de zaruri și valorile de pe fețele vizibile ale zarurilor, calculați suma tuturor
fețelor care nu se văd.
- Se ignoră ordinea reală a numerelor pe fețele zarurilor, adică cele 6 numere pot apărea pe zar în orice
aranjament.

DATE DE INTRARE:
- N = numarul de zaruri suprapuse
- 5 numere naturale distincte în intervalul [1; 6] = cele 5 fețe vizibile pentru zarul de sus,
- (N - 1) linii a cate 4 numere naturale distincte în intervalul [1; 6] = cele 4 fețe vizibile ale zarurilor

DATE DE IESIRE:
- suma fețelor invizibile ale zarurilor.

EXEMPLU:
4
1 3 2 5 6
6 4 1 5
6 5 4 3
1 4 3 5

Avem 4 zaruri.
Primul zar : se vad fetele 1 3 2 5 6 => fata care nu se vede este 4
Al 2 - lea zar : se vad fetele 6 4 1 5 => fetele care nu se vad sunt : 2 si 3
Al 3 -lea zar : se vad fetele 6 5 4 3 => fetele care nu se vad sunt : 1 si 2
Al 4 -lea zar : se vad fetele 1 4 3 5 => fetele care nu se vad sunt : 2 si 6

Adunam valorile care nu se vad: 4 + 2 + 3 + 1 + 2 + 2 + 6 = 20 => se afiseaza 20
"""


#set 1 date de intrare
#date_intrare = [4, [1, 3, 2, 5, 6], [6, 4, 1, 5], [6, 5, 4, 3], [1, 4, 3, 5]]

#set 2 date de intrare
date_intrare = [2, [1, 2, 3, 4, 5], [1, 2, 3, 4]]


N = date_intrare[0]
# initializez suma cu 0
suma = 0

for i in range(N):  # iau cele N zaruri pe rand
    linie = date_intrare[i+1]  # citesc linia corespunzatoare zarului i
    print('Pentru zarul', i + 1, 'fetele care nu se vad sunt :')
    for numar in range(1, 7):  # iau toate numerele de la 1 la 6 pe rand
        if linie.count(numar) == 0:  # verific daca numar se afla in linie
            print(numar)
            suma = suma + numar  # adun fetele zarurilor care nu se vad


print('\nSuma tuturor fetelor care nu se vad este :',suma)

"""
DATE DE INTRARE:
4
1 3 2 5 6
6 4 1 5
6 5 4 3
1 4 3 5

DATE DE IESIRE:
20


DATE DE INTRARE:
2
1 2 3 4 5
1 2 3 4

DATE DE IESIRE:
17
"""