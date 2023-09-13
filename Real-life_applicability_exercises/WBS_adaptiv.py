"""
WBS ADAPTIV (https://drive.google.com/file/d/1c4G16mmOerPwZvscn6b_yKHti5-lL7QE/view?usp=drive_link)

WBS - White Block Skipping  = tehnica folosita pentru compresia unui şir binar
Există două codări posibile:
- codarea în care se ignoră blocurile compuse numai din biţi 0 : şirul comprimat începe cu un bit 0, la care se
adaugă codurile corespunzătoare blocurilor de biţi din şirul iniţial, codate după regula următoare: dacă toţi
biţii blocului sunt nuli, blocul este înlocuit de un bit unic de zero; dacă cel puţin un bit din bloc este
nenul, atunci biţii blocului se copiază şi în faţa lor este adăugat un bit de 1 (ca prefix).
- codarea în care se ignoră blocurile compuse numai din biţi 1 : şirul comprimat începe cu un bit 1, la care se
adaugă codurile corespunzătoare blocurilor de biţi din şirul iniţial, codate după regula următoare: dacă toţi
biţii sunt 1, blocul este înlocuit de un bit unic de 1; dacă cel puţin un bit din bloc este nul, atunci biţii
blocului se copiazăşi în faţa lor este adăugat un bit de 0 (ca prefix).

In final, se alege codarea care asigură raportul maxim de compresie.
In cazul în care cele două variante de compresie ajung la acelaşi raport de compresie, se utilizează varianta în
care se ignoră blocurile compuse numai din biţi 0.

CERINTA:
- să se genereze şirul comprimat (codat)
- să se calculeze raportul de compresie = raportul dintre numărul de biţi din şirul iniţial şi numărul de biţi
din şirul comprimat
# Dacă şirul de intrare nu poate fi împărţit exact în grupe de n biţi, ultimii biţi rămaşi se codează ca şi când
# ar face parte dintr-un grup neuniform (dar fără a adăuga biţi de completare).

DATE DE INTRARE:
- N = numărul de elemente din şir
- n = numărul de elemente din fiecare bloc ce va fi codat
- N linii = elementele sirului (numere de 0 sau 1)

DATE DE IESIRE:
- valoarea raportului de compresie
- şirul comprimat

EXEMPLU:
8
2
1
0
0
0
0
0
1
1

Pentru codarea bazată pe ignorarea blocurilor nule :
- 10 -> 110 (blocul se copiază şi în faţa lui este adăugat un bit de 1)
- 00 -> 0 (blocul este înlocuit de un singur bit de 0)
- 00 -> 0 (blocul este înlocuit de un singur bit de 0)
- 11 -> 111 (blocul se copiază şi în faţa lui este adăugat un bit de 1)

=> sirul codat : 0 110 0 0 111 -> contine 9 biti => raportul de compresie = 8/9

Pentru codarea bazată pe ignorarea blocurilor de 1 :
- 10 -> 010 (blocul se copiază şi în faţa lui este adăugat un bit de 0)
- 00 -> 000 (blocul se copiază şi în faţa lui este adăugat un bit de 0)
- 00 -> 000 (blocul se copiază şi în faţa lui este adăugat un bit de 0)
- 11 -> 1 (blocul este înlocuit de un singur bit de 1)

=> sirul codat : 1 010 000 000 1 -> contine 11 biti => raportul de compresie = 8/11

Cel mai mare raport de compresie se obţine în cazul codării bazate pe ignorarea blocurilor nule
=> se afiseaza : 0.89
0
1
1
0
0
0
1
1
1
"""


# set 1 date de intrare
"""
date_intrare = '''8
2
1
0
0
0
0
0
1
1'''
"""

# set 2 date de intrare
"""
date_intrare = '''10
5
0
0
0
0
0
0
0
0
1
1'''
"""

#set 3 date de intrare

date_intrare = '''10
3
1
1
1
0
0
0
1
1
1
0'''

date_intrare = date_intrare.splitlines()


N = int(date_intrare[0])
print('Numarul de elemente din sir :', N)
n = int(date_intrare[1])
print('Numarul de elemente din fiecare bloc ce va fi codat :', n)
sir = ''


def ignor_blocuri_0(string):  # codarea în care se ignoră blocurile compuse numai din biţi 0
    string0 = '0'  # sirul comprimat incepe cu un bit 0
    for j in range(0, N - n + 1, n):  # N - n + 1 pentru ca atunci cand fac j + n sa nu depasesc ultimul index
        contor = 0
        # iau pe rand fiecare bit din blocurile de n biti
        for caracter in string[j:j+n]:
            if caracter == '1':
                contor += 1
                break
        if contor == 0:  # dacă toţi biţii blocului sunt nuli
            string0 += '0'  # blocul este înlocuit de un bit unic de zero
        else:  # daca cel putin un bit din bloc este nenul
            string0 += '1' + string[j:j+n]  # biţii blocului se copiază şi în faţa lor este adăugat un bit de 1
    # verific daca N este divizivbil cu n pentru a afla daca mai sunt biti in sir
    if N % n != 0:
        # ultimii biţi rămaşi se codează ca şi când ar face parte dintr-un grup neuniform
        string0 += '1' + string[j + n:]
    # este returnat sirul comprimat prin codarea în care se ignoră blocurile compuse numai din biţi 0
    return string0


def ignor_blocuri_1(string):  # codarea în care se ignoră blocurile compuse numai din biţi 1
    string1 = '1'  # sirul comprimat incepe cu un bit 1
    for j in range(0, N - n + 1, n):  # N - n + 1 pentru ca atunci cand fac j + n sa nu depasesc ultimul index
        contor = 0
        # iau pe rand fiecare bit din blocurile de n biti
        for caracter in string[j:j+n]:
            if caracter == '0':
                contor += 1
                break
        if contor == 0:  # dacă toţi biţii blocului sunt nenuli
            string1 += '1'  # blocul este înlocuit de un bit unic de 1
        else:  # daca cel putin un bit din bloc este nul
            string1 += '0' + string[j:j+n]  # biţii blocului se copiază şi în faţa lor este adăugat un bit de 1
    # verific daca N este divizivbil cu n pentru a afla daca mai sunt biti in sir
    if N % n != 0:
        # ultimii biţi rămaşi se codează ca şi când ar face parte dintr-un grup neuniform
        string1 += '0' + string[j + n:]
    # este returnat sirul comprimat prin codarea în care se ignoră blocurile compuse numai din biţi 1
    return string1


# formez sirul de biti
for bit in date_intrare[2:]:
    sir += bit
print('Sirul de biti ce va fi codat :', sir)

# memorez sirul comprimat prin codarea în care se ignoră blocurile compuse numai din biţi 0 in variabila sir0
sir0 = ignor_blocuri_0(sir)
r_compresie_0 = N / len(sir0)  # calculez raportul de compresie corespunzator
print('Sirul comprimat obtinut prin codarea în care se ignoră blocurile compuse numai din biţi 0 :', sir0)
print('Raportul de compresie corespunzator : {:.2f}'.format(r_compresie_0))

# memorez sirul comprimat prin codarea în care se ignoră blocurile compuse numai din biţi 1 in variabila sir1
sir1 = ignor_blocuri_1(sir)
r_compresie_1 = N / len(sir1)  # calculez raportul de compresie corespunzator
print('Sirul comprimat obtinut prin codarea în care se ignoră blocurile compuse numai din biţi 1 :', sir1)
print('Raportul de compresie corespunzator : {:.2f}'.format(r_compresie_1))

# aleg codarea care asigură raportul maxim de compresie
if r_compresie_0 >= r_compresie_1:
    print("{:.2f}".format(r_compresie_0))
    for bit in sir0:
        print(bit)
else:
    print("{:.2f}".format(r_compresie_1))
    for bit in sir1:
        print(bit)


"""
DATE DE INTRARE:
8
2
1
0
0
0
0
0
1
1

DATE DE IESIRE:
0.89
0
1
1
0
0
0
1
1
1


DATE DE INTRARE:
10
5
0
0
0
0
0
0
0
0
1
1

DATE DE IESIRE:
1.25
0
0
1
0
0
0
1
1


DATE DE INTRARE:
10
3
1
1
1
0
0
0
1
1
1
0

Date de iesire:
1.11
1
1
0
0
0
0
1
0
0
"""