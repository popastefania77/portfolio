"""
Write a Python method that appends text given as parameter to the beginning of a predefined file
"""
def append_text_at_the_beginning(text, file):
    # deschid fisierul pentru citire
    with open(file, 'r') as fout:
        # citesc texul existent din fisier
        text_existent = fout.read()
        # si il cocatenez textlui pe care vreau sa il adaug
        text_nou = text + text_existent
    # deschid fisierul pentru scriere
    with open('a.txt', 'w') as fin:
        # scriu textul
        fin.write(text_nou)
        

append_text_at_the_beginning('mmcmkx\n', 'a.txt')
