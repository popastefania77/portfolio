"""
Un număr de înmatriculare valid trebuie sa respecte urmatoarele reguli:
- valorile valide pentru primul grup de litere sunt : AB, AR, AG, B, BC, BH, BN, BT, BV, BR, BZ, CS, CL, CJ, CT,
CV, DB, DJ, GL, GR, GJ, HR, HD, IL, IS, IF, MM, MH, MS, NT, OT, PH, SM, SJ, SB, SV, TR, TM, TL, VS, VL, VN
- al 2 - lea grup de litere e format din 2 sau 3 caractere numerice
- al 3 - lea grup de litere e format din exact 3 caractere litere mari
"""


def verificare_str1(str1):
    lista = 'AB, AR, AG, B, BC, BH, BN, BT, BV, BR, BZ, CS, CL, CJ, CT, CV, DB, DJ, GL, GR, GJ, HR, HD, IL, IS, IF, MM, MH, MS, NT, OT, PH, SM, SJ, SB, SV, TR, TM, TL, VS, VL, VN'
    # impart stringul lista in stringurile mai mici necesare
    lista = lista.split(', ')
    # verific daca str1 se afla in lista de stringuri
    if str1 in lista:
        return True
    else:
        return False

def verificare_str2(str2):
    # verific daca str2 este format doar din cifre si daca are lungimea 2 sau 3
    if str2.isdigit() and (len(str2) == 2 or len(str2) == 3):
        return True
    else:
        return False

def verificare_str3(str3):
    # verific daca str3 este format doar din litere mari, alfabetice, cu lungimea 3
    if str3.isupper() and (len(str3) == 3) and str3.isalpha():
        return True
    else:
        return False


#date_intrare = date_intrare.splitlines()
def verificare(date_de_intrare):
    # impart linia in cele 3 stringuri
    str1, str2, str3 = date_de_intrare.split()
    # verific daca stringurile indeplinesc conditiile
    if verificare_str1(str1) and verificare_str2(str2) and verificare_str3(str3):
        return True
    else:
        return False
'''
if verificare('B 12 ABC') == True:
    print('True')
'''


