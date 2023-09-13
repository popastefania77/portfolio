"""
NUMAR PALINDROMIC MAXIM (https://drive.google.com/file/d/1UydmS5R-h1mp3reEixRlPj-Zm2rqkA2F/view?usp=drive_link)

Un numar este palindrom daca se citește la fel si de la inceput spre final si de la final spre inceput.

CERINTA:
- să se determine numărul cel mai mare de tip palindrom (în situaţia în care se pot forma mai multe palindromuri)
ce se poate forma cu toate cifrele date
- dacă nu se poate forma niciun palindrom, la ieşire se va afişa cifra 0

DATE DE INTRARE:
- n = numarul de cifre
- n cifre

DATE DE IESIRE:
- numărul cel mai mare de tip palindrom

EXEMPLU:
Date de intrare:
6
5 9 8 5 9 8

Date de iesire:
985589
"""


# SET 1 DATE DE INTRARE
"""
date_intrare = '''6
5 9 8 5 9 8'''
"""

# SET 2 DATE DE INTRARE
"""
date_intrare = '''3
1 2 2'''
"""

# SET 3 DATE DE INTRARE

date_intrare = '''5
1 2 3 3 4'''


date_intrare = date_intrare.splitlines()
n = int(date_intrare[0])
print('Numarul de cifre :', n)
cifre = list(map(int, date_intrare[1].split()))
print('Cifrele din care trebuie format palindromul :', cifre)

contor1 = 0
contor2 = 0
contorn = 0

# aflu numarul de aparitii ale cifrelor
for i in range(n):
    if cifre.count(cifre[i]) == 2:
        contor2 += 1
    elif cifre.count(cifre[i]) == 1:
        contor1 += 1
    else:
        contor2 += 1

# inversez lista in care am pus cifrele palindromului pentru a obtine palindromul maxim
cifre.sort(reverse=True)


palindrom = 0
cifre_nou = list()
if contor2 == n:  # daca toate cifrele apar de 2 ori
    for i in range(0, n, 2):
        cifre_nou.append(cifre[i])  # adaug intr-o noua lista cifrele care apar la fiecare 2 pozitii
    for i in range(int(n / 2)):
        # formez palindromul
        palindrom += cifre_nou[i] * 10 ** i + cifre_nou[i] * 10**(n - 1 - i)
    print('Palindromul cu valoare maxima obtinut din cifrele date :', palindrom)
elif contor2 == n - 1 and contor1 == 1:  # daca o cifra apare o data si restul de 2 ori
    for i in range(0, n - 1, 2):
        cifre_nou.append(cifre[i])  # adaug intr-o noua lista cate o cifra din fiecare
    cifre_nou.append(cifre[n - 1])
    for i in range(int(n / 2)):
        # formez palindromul
        palindrom += cifre_nou[i] * 10 ** i + cifre_nou[i] * 10**(n - 1 - i)
    palindrom += cifre_nou[int(n / 2)] * 10 ** (int(n / 2))
    print('Palindromul cu valoare maxima obtinut din cifrele date :', palindrom)
else:
    print('0 -> Din cifrele date nu s-a putut forma palindrom')


"""
DATE DE INTRARE:
6
5 9 8 5 9 8

DATE DE IESIRE:
985589


DATE DE INTRARE:
3
1 2 2

DATE DE IESIRE:
212


DATE DE INTRARE:
5
1 2 3 3 4

DATE DE IESIRE:
0
"""