"""
DECODARE MESAJ (https://drive.google.com/file/d/1OmUeqxiZmFFfZp1L11-be68LzeQ1Q7dz/view?usp=drive_link)

Se da un mesaj, format doar din cifre, codat folosind urmatoarea corespondenta:
- A → 1
- B → 2
- ...
- Z → 26

Reguli de decodare:
- Când următoarele două cifre din mesaj pot fi interpretate ca un număr de două cifre pe care îl putem decoda, le
vom interpreta astfel, ignorând posibilitatea interpretării unei singure cifre.
- Dacă pe poziţia curentă se află un 0, secvenţa 0x se va interpreta ca x, unde x este orice
cifră între 1 şi 9, iar cifra x se va decoda ca atare. (Exemplu: 01 → 1 → A).
- Două cifre de 0 consecutive vor fi decodate ca un spațiu.

CERINTA:
Să se decodeze mesajul, folosind scenariul de mai sus.

Date de intrare:
- un sir de cifre neintrerupt = mesajul codat

Date de ieşire:
- mesajul decodat

Exemplu:
195318520
- 19 -> 'S'
- 53 :
    - 5 -> 'E'
- 31 :
    - 3 -> 'C'
- 18 -> 'R'
- 52 :
    - 5 -> 'E'
- 20 -> 'T'

=> se afiseaza SECRET
"""


import string


# set 1 date de intrare
#date_intrare = '195318520'

# set 2 date de intrare
date_intrare = '2671513152000011202'


mesaj = date_intrare  # preiau mesajul
print('Mesajul codat :', mesaj)
lista_numere = []  # creez o lista in care o sa pun toate numerele de la 1 la 2
for i in range(1, 27):
    lista_numere.append(str(i))

# creez un dictionar in care voi pune corespundenta dintre numere si litere
dictionar = dict(zip(lista_numere, string.ascii_uppercase))
# adaug in dictionar si corespundenta dintre '00' si ' '(spatiu)
dictionar['00'] = ' '

mesaj_decriptat = ''  # initializez mesajul decriptat

i = 0  # initializez un contor cu ajutorul caruia percurg mesajul codat
while i < len(mesaj):  # cat timp mesajul codat nu s-a terminat
    # daca 2 cifre din mesaj pot fi interpretate ca un număr de două cifre pe care îl pot decoda
    if dictionar.get(mesaj[i:i + 2]):
        mesaj_decriptat += dictionar[mesaj[i:i + 2]]  # adaug la mesajul decriptat litera corespunzatoare
        print(mesaj[i:i + 2], '→', dictionar[mesaj[i:i + 2]])
        i += 1  # la urmatoarea iteratie pozitia curenta va fi dupa cele 2 cifre
    elif mesaj[i] == '0':  # daca pe pozitia curenta de afla un 0
        # adaug la mesajul decriptat litera corespunztoare cifrei care se afla pe pozitia i + 1
        mesaj_decriptat += dictionar[mesaj[i + 1]]
        print(mesaj[i:i + 2], '→', dictionar[mesaj[i + 1]])
        i += 1  # la urmatoarea iteratie pozitia curenta va fi dupa cele 2 cifre
    else:  # daca cele 2 cifre nu se incadreaza in cazurile de mai sus
        # adaug la mesajul decriptat litera corespunztoare cifrei de pe pozitia curenta
        mesaj_decriptat += dictionar[mesaj[i]]
        print(mesaj[i], '→', dictionar[mesaj[i]])
    i += 1  # incrementez pozitia curenta

print('Mesajul decodat :', mesaj_decriptat)


"""
Date de intrare:
195318520

Date de iesire:
SECRET


Date de intrare:
2671513152000011202

Date de iesire:
ZGOMOT ALB
"""