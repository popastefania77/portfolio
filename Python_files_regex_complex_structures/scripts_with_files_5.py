"""
Write a function that verifies if a file belongs to a directory. If directory is not specified, it should look in
the current working directory
"""

import os


def file_belongs_to_directory(file, directory=os.getcwd()):
    path = os.path.join(directory, file)  # creez calea concatenand fisierul la director
    return os.path.exists(path)  # aflu daca exista aceasta cale


print(file_belongs_to_directory('a.txt'))
print(file_belongs_to_directory('a.txt', 'C:\programare\python'))

