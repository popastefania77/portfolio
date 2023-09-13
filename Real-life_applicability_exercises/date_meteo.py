"""
DATE METEO (https://drive.google.com/file/d/12qLIStQwXJ6SkYz5tiL29eCCuWQWoLMQ/view?usp=drive_link)

Meteorologii notează pe parcursul a N zile
consecutive temperaturile maxime zilnice şi sunt interesaţi

Cerinţă:
Să se determine :
- secvenţa de zile având lungime maximă, pentru care temperaturile înregistrate au alternat ca semn :
    - dacă există mai multe astfel de secvenţe, meteorologii sunt interesaţi de cea mai recentă
    - dacă nu există măcar două zile consecutive cu temperaturi alternante ca semn, se înregistreaza rezultatul 0
- statistica valorilor pozitive vs. negative de pe parcursul celor N zile -> se calculează ca raport între
numărul valorilor pozitive sau negative și totalul valorilor înregistrate

DATE DE INTRARE:
- N = numărul total de zile pentru care se efectuează studiul
- N numere = temperaturile din cele N zile

DATE DE IESIRE:
- NrMax = numărul maxim de zile consecutive pentru care temperaturile au alternat ca semn
- temperaturile (alternante ca semn) înregistrate în cele NrMax zile
- procentele aferente valorilor negative și pozitive de temperatură identificate pe parcursul celor N zile in
formatul +:AB.CD% -:EF.GH%
!!! În cazul în care nu există măcar două zile consecutive cu temperaturi alternante ca semn se va afisa
valoarea 0

EXEMPLU:
16
1 -5 -3 2 -1 7 -2 5 1 7 -9 0 -1 6 -1 -8

Măsurătoarea a fost efectuată pe durata a 16 zile.
În această perioadă au existat două secvenţe de zile consecutive având lungime maximă (6) în care temperaturile
au alternat ca semn => se afisaeza 6 si cea mai recenta secventa (7 -9 0 -1 6 -1)
Sunt 8 valori negative și 8 valori pozitive de temperatură în întreaga succesiune de temperaturi
înregistrate => se afiseaza +:50.00% -:50.00%
"""


# SET 1 DATE DE INTRARE
"""
date_intrare = '''16
1 -5 -3 2 -1 7 -2 5 1 7 -9 0 -1 6 -1 -8'''
"""

# SET 2 DATE DE INTRARE

date_intrare = '''9
0 -2 0 -1 -2 3 -2 -3 3'''



linii = date_intrare.splitlines()

N = int(linii[0])
print('Numărul total de zile pentru care se efectuează studiul :', N)
temperaturi = list(map(int, linii[1].split()))
print('Temperaturile inregistrate in timpul studiului :\n{}'.format(temperaturi))
# variabila in care stochez numărul maxim de zile consecutive pentru care temperaturile au alternat ca semn
NrMax = 1
# lungimea curenta a secventei de zile consecutive pentru care temperaturile au alternat ca semn
lungime_curenta = 1
temperaturi_poz = 0  # contor pentru temperaturile pozitive
temperaturi_neg = 0  # contor pentru temperaturile negative
index = 0  # il folosesc pentru a afisa secventa de temperaturi ceruta.


for i in range(len(temperaturi) - 1):
    # daca 2 temperaturi consecutive alterneaza ca semn
    if temperaturi[i] >= 0 > temperaturi[i + 1] or temperaturi[i] < 0 <= temperaturi[i + 1]:
        lungime_curenta += 1  # cresc lungimea secventei
        # verific daca lungimea curenta este mai mare decat lungimea maxima
        if NrMax <= lungime_curenta:
            NrMax = lungime_curenta
            index = i
    else:  # daca cele 2 temperaturi consecutive nu alterneaza ca semn
        lungime_curenta = 1  # se intrupe secventa

    # determin cate temepraturi pozitive, respectiv negative se gasesc in lista de temperaturi
    if temperaturi[i] >= 0:
        temperaturi_poz += 1
    else:
        temperaturi_neg += 1
# adaug si ultima temperatura in categoria ei (pozitiva/negativa)
if temperaturi[len(temperaturi) - 1] > 0:
    temperaturi_poz += 1
else:
    temperaturi_neg += 1

# verific daca exista secvente in care temperaturile consecutive alterneaza
if NrMax > 1:
    print('Numărul maxim de zile consecutive pentru care temperaturile au alternat ca semn :', NrMax)
    print(f'Temperaturile înregistrate în cele {NrMax} zile :', end=' ')
    for i in range(index - NrMax + 2, index + 2):
        print(temperaturi[i], end=' ')
    print('\n')
    print('Procentele aferente valorilor negative și pozitive de temperatură identificate pe parcursul '
          'studiului :')
    print("+:{:.2f}% -:{:.2f}%".format(temperaturi_poz / N * 100, temperaturi_neg / N * 100))
else:
    print('0 -> nu exista zile consecutive cu temperaturi alternante ca semn')


"""
DATE DE INTRARE:
16
1 -5 -3 2 -1 7 -2 5 1 7 -9 0 -1 6 -1 -8

DATE DE IESIRE:
6
7 -9 0 -1 6 -1
+:50.00% -:50.00%


DATE DE INTRARE:
9
0 -2 0 -1 -2 3 -2 -3 3

DATE DE IESIRE:
4
0 -2 0 -1
+:44.44% -:55.56%
"""