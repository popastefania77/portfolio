"""
DISTRIBUTIE BITI RNG (https://drive.google.com/file/d/1pweyF3NhLmdvoqZvn4v99ng7BbkyOAe1/view?usp=drive_link)

Verificarea numarului de apariții pentru fiecare secvență posibilă de doi biți: 00, 01, 10 și 11 cât și raportul
între numărul de biți de 0 și de 1. Mai precis, trebuie ca raporturile R1 si R2 să fie mai mici sau egale cu 110%
- R1 dintre numărul de apariții a perechii care apare de  cele mai multe ori și numărul de apariții a perechii
care apare de cele mai puține ori
- R2 între numărul de apariții ale celui mai frecvent bit și numărul de apariții ale celui mai puțin frecvent bit

Cerință:
Să se calculeze raporturile R1 și R2 și să se decidă dacă generatorul este valid sau nu.

Date de intrare:
- n = numărul de biți generați
- o secvență continuă de n biți (valori de 0 sau 1), ne-separați prin spații.

Date de ieșire:
- raporturile R1 și R2 calculate conform descrierii, valori fracționare cu două zecimale
- valoarea 1 dacă generatorul este valid sau 0 dacă nu este valid

Exemplu:
18
101100110111100001

n = 18 biti
secventa de biti : 101100110111100001

Extragând secvențele de câte doi biți se observă că:
    00 - apare de 2 ori
    01 - apare de 2 ori
    10 - apare de 2 ori
    11 - apare de 3 ori
Calculand raportul dintre numarul maxim și minim de apartii => R1 = 3/2 = 150% => se afiseaza 1.50
Extragând secvențele de câte un biț se observă că:
    0 - apare de 8 ori
    1 - apare de 10 ori
Calculand raportul dintre numărul de apariții ale celui mai frecvent bit și numărul de apariții ale celui mai
puțin frecvent bit => R2 = 10/8 = 125% => se afiseaza 1.25


Pentru că cel puțin unul din raporturi este mai mare strict decât 110%, se afișează 0(secvența nu este aleatoare)
"""


#set 1 date de intrare
#date_intrare = [18, '101100110111100001']

#set 2 date de intrare
date_intrare = [24, '101100110111100001010010']


n = date_intrare[0]
print('Numarul de biti este n =', n)
biti = date_intrare[1]
print('Secventa de biti este :', biti)

d = {}
def insert(secv):
    if d.get(secv, None):  # daca secventa de biti exista in dictionar
        d[secv] += 1  # cresc numarul de aparitii
    else:  # daca secventa nu exista in dictionar
        d[secv] = 1  # initializez numarul de aparitii a secventei respective


# parcurg sirul de biti din 2 in 2 si nu pun len(biti) - 1 in range deoarece secventa
# va avea intotdeauna numar par de biti (trebuie sa avem perechi de biti)
for i in range(0, len(biti), 2):
    insert(biti[i:i+2])  # adaug in dictionar secventa de biti (00,01, 10 sau 11)
    #print(biti[i:i+2])
    insert(biti[i])  # adaug in dictionar bitul curent (0 sau 1)
    insert(biti[i+1])  # adaug in dictionar bitul urmator celui curent (0 sau 1)

# Raportul R2 se face între numărul de apariții ale celui mai frecvent bit și numărul de apariții ale celui mai
# puțin frecvent bit
if d.get('1', 0) > d.get('0', 0):  # daca bitul 1 apare de mai mute ori decat bitul 0
    # am pus 0 ca valoare default pentru cazul in care secventa de biti nu contine deloc fie 0 fie 1
    # R2 se face intre numarul de aparitii al bitului 1 si numarul de aparitii al bitului 0
    R2 = d.get('1', 0) / d.get('0', 0)
else:  # daca bitul 0 apare de mai mute ori decat bitul 1
    # R2 se face intre numarul de aparitii al bitului 0 si numarul de aparitii al bitului 1
    R2 = d.get('0', 0) / d.get('1', 0)

# dupa ce am calculat raporul R2 sterg din dictionar cheile '1' si '0' pentru a putea afla care dintre prerechile
# de biti 00, 01, 10 sau 11 apare de cele mai multe ori respectiv de cele mai putine ori
d.pop('1')
d.pop('0')

# Raportul R1 se face intre numărul de apariții a perechii care apare de cele mai multe ori și numărul de
# apariții a perechii care apare de cele mai puține ori
R1 = max(d.values())/min(d.values())
print('R1 = {:.2f} R2 = {:.2f}'.format(R1, R2))  # afisez R1 si R2 cu 2 zecimale

# Raporturile R1 respectiv R2 trebuie sa fie mai mici sau egale cu 110% pentru ca generatorul sa fie valid
if R1 < 1.10 and R2 < 1.10:
    print('1 - generator valid')  # in cazul in care se respecta conditia afisam 1 (generator valid)
else:
    print('0 - generator invalid')  # in cazul in care nu se respecta conditia afisam 0 (generator invalid)

"""
Date de intrare:
18
101100110111100001

Date de iesire:
1.50 1.25
0


Date de intrare:
24
101100110111100001010010

Date de iesire:
1.00 1.00
1
"""