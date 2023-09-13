"""
Write a Python program that pings localhost. Use os and subprocess modules. Save command output.
Command: ‘ping localhost’ or ‘ping 127.0.0.1’
"""

import os
import subprocess


def ping_localhost(file):  # file = fisierul in care se salveaza output-ul comenzii
    output = subprocess.check_output(['ping', '127.0.0.1'])
    path = os.path.join(os.getcwd(), file)
    if os.path.isfile(path):
        with open(file, 'wb') as fin:  # b -> write() argument must be str, not bytes
            fin.write(output)
    else:
        print('Fisierul dat ca argument nu exista in directorul curent')


ping_localhost('output_localhost.txt')
