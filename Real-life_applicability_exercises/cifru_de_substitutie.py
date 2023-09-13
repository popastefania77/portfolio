"""
CIFRU DE SUBSTITUTIE (https://drive.google.com/file/d/1jNP4QyZGFgfpjuuZO2IHqfHFmyQNDUW9/view?usp=drive_link)

Criptarea printr-un cifru de substituţie se realizează prin înlocuirea fiecărui caracter din textul de intrare cu
alt caracter. Doar literele mici (26), literele mari (26) şi cifrele (10) se vor înlocui în text, în total
tabelul de substituţie are deci 62 de elemente.

CERINTA:
- sa se cripteze textul de la intrare

DATE DE INTRARE:
- textul de criptat
- perechi de câte două caractere: caracterul din textul de intrare şi caracterul cu care acesta trebuie înlocuit

DATE DE IESIRE:
- textul criptat

EXEMPLU:
Date de intrare:
Ana are 37 de mere coapte (din care doar 35 coapte corespunzator)!
a,H b,j c,6 d,I e,2 f,R g,5 h,t i,h j,k k,m l,f m,D n,F o,1 p,0 q,c r,G
s,n t,N u,e v,B w,r x,U y,p z,A A,8 B,X C,S D,P E,T F,a G,M H,d I,K J,L
K,3 L,C M,i N,9 O,E P,w Q,o R,z S,4 T,O U,q V,V W,J X,x Y,Z Z,u 0,l 1,y
2,W 3,s 4,Q 5,g 6,v 7,7 8,b 9,Y

Date de iesire:
8FH HG2 s7 I2 D2G2 61H0N2 (IhF 6HG2 I1HG sg 61H0N2 61G2n0eFAHN1G)!
"""


# SET 1 DATE DE INTRARE:
"""
date_intrare = '''Ana are 37 de mere coapte (din care doar 35 coapte corespunzator)!
a,H b,j c,6 d,I e,2 f,R g,5 h,t i,h j,k k,m l,f m,D n,F o,1 p,0 q,c r,G s,n t,N u,e v,B w,r x,U y,p z,A A,8 B, X C,S D,P E,T F,a G,M H,d I,K J,L K,3 L,C M,i N,9 O,E P,w Q,o R,z S,4 T,O U,q V,V W,J X,x Y,Z Z,u 0,l 1,y 2,W 3,s 4,Q 5,g 6,v 7,7 8,b 9,Y'''
"""

# SET 2 DATE DE INTRARE:

date_intrare = '''The gme w releed n Jpn on Deember 17, 2009, nd n North Amer, Europe nd Autrl on Mrh 9, 2010
a,H b,j c,6 d,I e,2 f,R g,5 h,t i,h j,k k,m l,f m,D n,F o,1 p,0 q,c r,G s,n t,N u,e v,B w,r x,U y,p z,A A,8 B,X C,S D,P E,T F,a G,M H,d I,K J,L K,3 L,C M,i N,9 O,E P,w Q,o R,z S,4 T,O U,q V,V W,J X,x Y,Z Z,u 0,l 1,y 2,W 3,s 4,Q 5,g 6,v 7,7 8,b 9,Y'''



date_intrare = date_intrare.splitlines()

text = date_intrare[0]
print('Text de criptat :', text)


# creez un dictionar in care pun substitutiile
cifru_substituie = {}
for i in range(4):
    substitutii = date_intrare[1]
    for j in range(0, len(substitutii), 4):
        cifru_substituie[substitutii[j]] = substitutii[j+2]
# print(cifru_substituie)

# convertesc texul de la intrare intr-o lista pentru al putea modifica
# stringurile nu se pot modifica fiind imutabile
text = list(text)

# realizez codarea textului
for i in range(len(text)):
    if cifru_substituie.get(text[i]):
        text[i] = cifru_substituie.get(text[i])
# print(text)

# pun textul codat intr-un string pentru a-l afisa
secventa = ''
for litera in text:
    secventa += litera
print('Text criptat :', secventa)



"""
DATE DE INTRARE:
Ana are 37 de mere coapte (din care doar 35 coapte corespunzator)!
a,H b,j c,6 d,I e,2 f,R g,5 h,t i,h j,k k,m l,f m,D n,F o,1 p,0 q,c r,G
s,n t,N u,e v,B w,r x,U y,p z,A A,8 B,X C,S D,P E,T F,a G,M H,d I,K J,L
K,3 L,C M,i N,9 O,E P,w Q,o R,z S,4 T,O U,q V,V W,J X,x Y,Z Z,u 0,l 1,y
2,W 3,s 4,Q 5,g 6,v 7,7 8,b 9,Y

DATE DE IESIRE:
8FH HG2 s7 I2 D2G2 61H0N2 (IhF 6HG2 I1HG sg 61H0N2 61G2n0eFAHN1G)!


DATE DE INTRARE:
The gme w releed n Jpn on Deember 17, 2009, nd n North Amer, Europe nd Autrl on Mrh 9, 2010
a,H b,j c,6 d,I e,2 f,R g,5 h,t i,h j,k k,m l,f m,D n,F o,1 p,0 q,c r,G
s,n t,N u,e v,B w,r x,U y,p z,A A,8 B,X C,S D,P E,T F,a G,M H,d I,K J,L
K,3 L,C M,i N,9 O,E P,w Q,o R,z S,4 T,O U,q V,V W,J X,x Y,Z Z,u 0,l 1,y
2,W 3,s 4,Q 5,g 6,v 7,7 8,b 9,Y

DATE DE IESIRE:
6DJ IeJ n CJZJJq j ahj xj UJJe5JC rT, c88A, jq j zxCWD deJC, kNCxhJ jq dNWCZ xj 3CD A, c8r8
"""