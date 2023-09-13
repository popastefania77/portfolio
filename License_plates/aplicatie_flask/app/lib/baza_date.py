from app.lib import numere_de_inmatriculare
import re


def vizualizare_baza_date(file):
    with open(file, 'r') as fout:
        text = fout.read()
    return text

#print(vizualizare_baza_date('baza_date.txt'))


def verificare_existenta(file, numar_inmatriculare):
    text = vizualizare_baza_date(file)
    if re.search(numar_inmatriculare, text):
        return True
    else:
        return False
    
    
def adaugare_in_baza_date(file, numar_inmatriculare, proprietar):
    if numere_de_inmatriculare.verificare(numar_inmatriculare) \
            and not verificare_existenta(file, numar_inmatriculare):
        with open(file, 'a') as fout:  # a -> append
            fout.write(numar_inmatriculare + ' ' + proprietar + '\n')
        return 'Numarul de inmatriculare a fost adaugat cu succes'
    elif not numere_de_inmatriculare.verificare(numar_inmatriculare):
        return 'Numarul de inmantriculare nu este valid'
    elif verificare_existenta(file, numar_inmatriculare):
        return 'Numarul de inmatriculare a fost deja folosit'





#print(adaugare_in_baza_date('baza_date.txt', 'B 23 ABC', 'Popa Stefania'))


