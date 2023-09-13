"""
Write a Python program that reads file content and displays the number of lines that were read
"""
def number_of_lines(fisier):
    # deschid fisierul cu permisuni de citire
    with open(fisier, 'rb') as fout:  # adug b pentru fisiere binare
        count = 0  # initializez un contor
        # pentru fiecare linie din fisier incrementez contorul
        for line in fout:
            count += 1 
    # afisez numarul liniilor citite
    #fout.close() -> daca folosesc 'with open' fisierul se inchide automat
    print(count)


number_of_lines('a.txt')
number_of_lines('Screenshot 2023-06-27 101217.png')

