"""
Write a Python program that prints all ‘.txt’ files from a directory.
- Give the file extension as a parameter.
- You can use the Python installation directory (e.g C:\Python27)
"""


import glob
import os


def all_txt_files(directory):
    path = os.path.join(directory, '**', '*txt')  # creez calea concatenand '**' si '.txt' la director
    print('All files with "txt" extension :')
    # printex fiecare fisier cu extensia 'txt'
    for file in glob.glob(path, recursive=True):
        print(file)


all_txt_files(r'C:\Users\popas\AppData\Local\Programs\Python\Python311')


"""
glob.glob(r'C:\Users\**\*.py', recursive=True)

- 'r' prefix is used to treat the string as a raw sequence of characters and disable the escape character 
interpretation;
- '**' serve as a wildcard for all subdirectories. It allows glob.glob() to search for files in the current 
directory and all levels of subdirectories;
- 'recursive=True' parameter is necessary to enable recursive searching. If you set it to False, glob.glob() 
would only search for files in the specified directory (C:\Users) and not include subdirectories.
"""