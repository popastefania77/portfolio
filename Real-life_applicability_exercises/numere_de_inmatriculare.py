"""
NUMERE DE INMATRICULARE (https://drive.google.com/file/d/1vs0nYw-iGg1uhvzmYvR1HzwtdEKA15Hf/view?usp=drive_link)

Un număr de înmatriculare valid trebuie sa respecte urmatoarele reguli:
- valorile valide pentru primul grup de litere sunt : AB, AR, AG, B, BC, BH, BN, BT, BV, BR, BZ, CS, CL, CJ, CT,
CV, DB, DJ, GL, GR, GJ, HR, HD, IL, IS, IF, MM, MH, MS, NT, OT, PH, SM, SJ, SB, SV, TR, TM, TL, VS, VL, VN
- al 2 - lea grup de litere e format din 2 sau 3 caractere numerice
- al 3- lea grup de litere e format din exact 3 caractere litere mari

CERINTA:
- sa se determine daca numerele de inmatriculare sunt valide

DATE DE INTRARE:
- linii de forma <String1 String2 String3>

DATE DE IESIRE:
- exclusiv liniile de intrare care reprezintă un număr de înmatriculare valid

EXEMPLU:
Date de intrare:
AB 123 ABC
B 23 DEF

Ambele numere prezentate pe intrare sunt corecte => se afiseaza amandoua

Date de iesire:
AB 123 ABC
B 23 DEF
"""


# SET 1 DATE DE INTRARE
"""
date_intrare = '''AB 123 ABC
B 23 DEF'''
"""

# SET 2 DATE DE INTRARE
"""
date_intrare = '''BB 123 ABC
SV 99 DEF'''
"""

# SET 3 DATE DE INTRARE
"""
date_intrare = '''B 1234 ABC
BV 9 ABC
VN 01 ABC'''
"""

# SET 4 DATE DE INTRARE
"""
date_intrare = '''AB 11 AAA
CT 0A XYZ
CV 01 AB8'''
"""

# SET 5 DATE DE INTRARE

date_intrare = '''B 01 abc'''



def vstr1(str1):
    lista = 'AB, AR, AG, B, BC, BH, BN, BT, BV, BR, BZ, CS, CL, CJ, CT, CV, DB, DJ, GL, GR, GJ, HR, HD, IL, IS, IF, MM, MH, MS, NT, OT, PH, SM, SJ, SB, SV, TR, TM, TL, VS, VL, VN'
    # impart stringul lista in stringurile mai mici necesare
    lista = lista.split(', ')
    # verific daca str1 se afla in lista de stringuri
    if str1 in lista:
        return True
    else:
        return False

def vstr2(str2):
    # verific daca str2 este format doar din cifre si daca are lungimea 2 sau 3
    if str2.isdigit() and (len(str2) == 2 or len(str2) == 3):
        return True
    else:
        return False

def vstr3(str3):
    # verific daca str3 este format doar din litere mari, alfabetice, cu lungimea 3
    if str3.isupper() and (len(str3) == 3) and str3.isalpha():
        return True
    else:
        return False


date_intrare = date_intrare.splitlines()

for i in range(len(date_intrare)):
    # impart linia in cele 3 stringuri
    str1, str2, str3 = date_intrare[i].split()
    # verific daca stringurile indeplinesc conditiile
    if vstr1(str1) and vstr2(str2) and vstr3(str3):
        print(str1, str2, str3)


# PENTRU INTRODUCERE DATE DE LA TASTATURA
"""
while True:
    try:
        # impart linia de la input in cele 3 stringuri
        str1, str2, str3 = input().split()
        # verific daca stringurile indeplinesc conditiile
        if vstr1(str1) and vstr2(str2) and vstr3(str3):
            print(str1, ' ', str2, ' ', str3, ' ')
    # daca am ajuns la EOF se iese din bucla
    except EOFError:
        break
"""

"""
DATE DE INTRARE:
AB 123 ABC
B 23 DEF

DATE DE IESIRE:
AB 123 ABC
B 23 DEF


DATE DE INTRARE:
BB 123 ABC
SV 99 DEF
DATE DE IESIRE:
SV 99 DEF


DATE DE INTRARE:
B 1234 ABC
BV 9 ABC
VN 01 ABC

DATE DE IESIRE:
VN 01 ABC

DATE DE INTRARE:
AB 11 AAA
CT 0A XYZ
CV 01 AB8

DATE DE IESIRE:
AB 11 AAA


DATE DE INTRARE:
B 01 abc

DATE DE IESIRE:

"""