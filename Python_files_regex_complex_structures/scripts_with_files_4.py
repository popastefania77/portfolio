"""
Write a python program to find the longest word in a file
"""


def longest_word_in_file(file):
    # deschid fisierul cu poermisuni de citire
    with open(file, 'r') as fout:
        data = fout.read()  # preiau stringul din interiorul fisierului
    data = data.split()  # creez o lista formata din cuvintele din fisier
    lungime_maxima = 0
    # aflu care este cuvantul cu lungimea maxima din fisier
    for i in range(len(data)):
        if lungime_maxima < len(data[i]):
            lungime_maxima = len(data[i])
            cuvant = data[i]
    return cuvant


file = 'a.txt'
print('Cel mai lung cuvant este :', longest_word_in_file(file), '-> {} caractere'.format(len(
    longest_word_in_file(file))))


