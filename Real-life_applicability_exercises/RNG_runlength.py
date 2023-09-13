"""
RNG RUNLENGTH (https://drive.google.com/file/d/1epg8DloUsevXs5Ng-6shX2CxDg0XNhl8/view?usp=drive_link)

Pentru ca secvența de biți generată să fie aleatoare, trebuie ca numărul de secvențe de un bit 1 să fie mai mare
sau egal decât numărul de secvențe de doi biți 1 care trebuie să fie mai mare sau egal decât numărul de secvențe
de trei biți 1, șamd.

CERINTA:
Să se decidă dacă generatorul este valid sau nu.

DATE DE INTRARE:
- n = numarul de biti generati
- o secventa continua de n biti

DATE DE IESIRE:
- numărul de apariții pentru fiecare lungime de secvență de biți 1, începând cu numărul de apariții pentru o
secvență de un singur bit 1 (delimitat de biți 0) și terminând cu ultimul număr de apariții nenul.
- valoarea 1 dacă generatorul este valid sau 0 dacă nu este.

EXEMPLU:
18
101100110111100001

Secventa are 18 biti si cuprinde:
- 2 secvente de un bit
- 2 secvente de 2 biti
- o secvente de 3 biti
- 1 secventa de 4 biti
=> se afiseaza 2 2 0 1

Sunt mai putine secvente de 3 biti decat de 4 => se afiseaza 0 - generatorul nu este valid
"""
#set 1 date de intrare
date_intrare = [18, '101100110111100001']

#set 2 date de intrare
#date_intrare = [24, '101100110111000010100100']


n = date_intrare[0]  # preiau numarul de biti
print('Numarul de biti generati n =', n)
secvente = {}  # initializez un dictionar in care o sa pun secventele de biti de 1, respectiv numarul lor
sir = date_intrare[1]  # preiau sirul de biti
print('Sirul de biti generat :', sir)
secventa = ''  # initializez secventa formata din biti de 1


def adaugare(string):
    if secvente.get(string):  # daca secventa exista in dictionar
        secvente[string] += 1  # incrementez numarul de aparitii al secventei respective
    else:  # daca secventa nu exista in dictionar
        secvente[string] = 1  # o adaug si initializez numarul de aparitii cu 1


# parcurg sirul de biti
for bit in sir:
    if bit == '1':  # atata timp cat nu apare un bit de 0
        secventa += '1'  # adaug acesti biti de 1 la secventa
        adaugat = 0  # ne spune ca secventa curenta nu a fost adaugata in dictionar
    elif bit == '0' and secventa:  # cand bitul este 0 si secventa nu e goala
        adaugare(secventa)  # adaugam secventa la dictionar
        secventa = ''  # golim secventa
        adaugat = 1  # ne spune ca secventa curenta a fost adaugata la dictionar

if adaugat != 1:  # daca secventa finala nu a fost adaugata
    adaugare(secventa)  # o adaugam



aleator = 0  # initializez o variabila care ma ajuta sa stiu daca sirul de biti este aleator sau nu


lungimea_maxima = len(max(secvente.keys()))  # aflu care este lungimea maxima a secventei formata din biti de 1
for i in range(1, lungimea_maxima):  # pentru fiecare lungime de la 1 la lungimea_maxima
    # exista = 0 => secventa de lungimea i nu exista
    # exista = 1 => secventa de lungimea i exista
    exista = 0  # initializez o variabila care ma va ajuta sa stiu daca secventa de lungimea i exista
    for key in secvente.keys():  # parcurg secventele de biti din dictionar
        if len(key) == i:  # daca exista o secventa de biti cu lungimea i
            exista = 1  # dau variabilei exista valoarea 1

    if exista == 0:  # daca secventa de lungimea i nu exista
        # o adaug in dictionar
        secventa = '1' * i
        secvente[secventa] = 0  # si ii dau valoarea 0 pentru ca nu exista
#print(secvente)
keys = list(secvente.keys())  # trag secventele intr - o lista
keys.sort()  # si le ordonez crescator : [1 , 11 , 111, ...]
for i in range(len(keys) - 1):  # pentru fiecare secventa
    # verific daca numărul de secvențe de un bit 1 este mai mare sau egal decât numărul de secvențe de doi
    # biți 1 care trebuie să fie mai mare sau egal decât numărul de secvențe de trei biți 1, șamd.
    if secvente.get(keys[i]) >= secvente.get(keys[i + 1]):
        aleator += 1
    print('Numarul de secvente de {} biti : {}'.format(i + 1, secvente.get(keys[i])))
print('Numarul de secvente de {} biti : {}'.format(len(keys), secvente[keys[len(keys) - 1]]))
# daca s-a indeplinit conditia pentru toate secventele
if aleator == len(keys) - 1:
    print('1 - generatorul este valid')  # generatorul este valid
else:  # daca nu s-a indeplinit conditia pentru toate secventele
    print('0 - generatorul este invalid')  # generatorul nu este valid

"""
DATE DE INTRARE:
18
101100110111100001

DATE DE IESIRE:
2 2 0 1
0


DATE DE INTRARE:
24
101100110111000010100100

DATE DE IESIRE:
4 2 1
1

"""