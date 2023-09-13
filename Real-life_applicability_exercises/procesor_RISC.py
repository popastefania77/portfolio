"""
PROCESOR RISC (https://drive.google.com/file/d/18v2vWMC5aBF0aVDn5U55sRCJ1pW6ioqu/view?usp=drive_link)

Simulatorul procesorului RISC va primi, ca și procesorul real, o secvență de instrucțiuni care va trebui
executată iar starea finală a datelor va trebui afișată la ieșire. Procesorul are un set de 16 registre
numerotate de la 0 la 15 și deocamdată nu are memorie.

Procesorul știe să execute următoarele instrucțiuni :
- lconst <dst> <val> –> se scrie valoarea <val> în registrul <dst>;
- add <dst> <src0> <src> –> se adună valorile din registrele <src0> și <src1> și rezultatul se scrie în
registrul <dst>;
- mul <dst> <src0> <src> –> se înmulțesc valorile din registrele <src0> și <src1> și rezultatul se scrie în
registrul <dst>;
- div <dst> <src0> <src> –> se împart valorile din registrele <src0> și <src1> și câtul se scrie în registrul
<dst>;
- print <reg> -> se afișează valoarea din registrul <reg>.
Dacă la execuția unei instrucțiuni de tip div împărțitorul este zero, se va afișa fraza Exception: line
<index>, unde index reprezintă a câta instrucțiune nu a putut fi executată, iar programul se va încheia.
Toate registrele au inițial valoarea 0.

CERINTA:
- Dându-se o secvență de instrucțiuni ca cele de mai sus, executați-le și afișați valorile printate de program.

DATE DE INTRARE:
- n = numărul de instrucțiuni
- n linii = n instructiuni

DATE DE IESIRE:
- valorile printate de program (prin instrucțiuni de tip print)

EXEMPLU:
8
lconst 0 10
print 0
lconst 2 1
add 1 0 2
mul 2 0 1
lconst 1 2
div 0 2 1
print 0

n = 8 instructiuni:
- lconst 0 10 va încărca valoarea 10 în registrul 0
- print 0 va afișa valoarea din registrul 0 => se afiseaza 10
- lconst 2 1 va încărca valoarea 1 în registrul 2
- add 1 0 2 va aduna valorile din registrele 0 și 2 (10 și 1) și rezultatul 11 va fi scris în registrul 1
- mul 2 1 0 va înmulți valorile din registrele 1 și 0 (11 și 10) și rezultatul 110 va fi stocat în registrul 2
- lconst 1 2 va încărca valoarea 2 în registrul 1
- div 0 2 1 va calcula câtul împărțirii valorilor din registrele 2 și 1 (110 și 2) și rezultatul 55 va fi stocat
în registrul 0
- print 0 va afișa conținutul registrului 0 => se afiseaza 55
"""
# SET 1 DATE DE INTRARE
"""
date_intrare = '''8
lconst 0 10
print 0
lconst 2 1
add 1 0 2
mul 2 0 1
lconst 1 2
div 0 2 1
print 0'''
"""

# SET 2 DATE DE INTRARE

date_intrare = '''7
lconst 0 10
lconst 1 -1
print 0
add 0 0 1
print 0
add 0 0 1
print 0'''


# SET 3 DATE DE INTRARE
"""
date_intrare = '''5
lconst 0 0
lconst 1 1
print 0
div 3 1 0
print 3'''
"""


linii = date_intrare.splitlines()

n = int(linii[0])
print('Numar instructiuni :', n)
procesor = {}  # in acest dictionar stochez registrele si memoria lor


def lconst(lista):
    command, dst, val = lista
    procesor[dst] = int(val)  # scrie valoarea <val> în registrul <dst>


def add(lista):
    command, dst, src0, src1 = lista
    # se adună valorile din registrele <src0> și <src1> și rezultatul se scrie în registrul <dst>
    procesor[dst] = procesor.get(src0, 0) + procesor.get(src1, 0)


def mul(lista):
    command, dst, src0, src1 = lista
    # se înmulțesc valorile din registrele <src0> și <src1> și rezultatul se scrie în registrul <dst>;
    procesor[dst] = procesor.get(src0, 0) * procesor.get(src1, 0)


def div(lista, index):
    command, dst, src0, src1 = lista
    if procesor.get(src1, 0):
        # se împart valorile din registrele <src0> și <src1> și câtul se scrie în registrul <dst>
        procesor[dst] = int(procesor.get(src0, 0) / procesor.get(src1, 0))
    else:  # daca împărțitorul este zero
        print('Exception: line', index)  # index = a câta instrucțiune nu a putut fi executată
        return 0


def print_RISC(lista):
    reg = lista[1]
    # se afișează valoarea din registrul <reg>
    print(procesor.get(reg, 0))


for i in range(n):  # parcurgem cele n linii
    linie = linii[i + 1].split()  # punem valorile de pe linie intr-o lista
    if linie[0] == 'lconst':
        lconst(linie)
    elif linie[0] == 'add':
        add(linie)
    elif linie[0] == 'mul':
        mul(linie)
    elif linie[0] == 'div':
        #div(linie, i+1)
        if div(linie, i + 1) == 0:
            break
    else:
        print_RISC(linie)

"""
DATE DE INTRARE:
8
lconst 0 10
print 0
lconst 2 1
add 1 0 2
mul 2 0 1
lconst 1 2
div 0 2 1
print 0

DATE DE IESIRE:
10
55


DATE DE INTRARE:
7
lconst 0 10
lconst 1 -1
print 0
add 0 0 1
print 0
add 0 0 1
print 0

DATE DE IESIRE:
10
9
8


DATE DE INTRARE:
5
lconst 0 0
lconst 1 1
print 0
div 3 1 0
print 3

DATE DE IESIRE:
0
Exception: line 4
"""
