"""
Write a Python program that will parse the output returned by ‘ping google.com’ command
- Create a dictionary that will contain all packets that were sent, received, lost
- Print the TTL min and max value.
- Calculate the average time and compare it with the one in statistics

Using the output above, hide the IP address of the receiver
- E.g “Pinging google.com [216.58.214.206] with 32 bytes of data:”
=> “Pinging google.com [x.x.x.x] with 32 bytes of data:”

https://docs.python.org/3/library/subprocess.html
"""


import subprocess
import re
import time


# DECOMENTATI ACEASTA SECTIUNE PENTRU LINUX


# folosesc Popen pentru a putea interactiona cu procesul
ping_process = subprocess.Popen(["ping", "google.com"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
# astept cateva secunde pentru a se trimite/primi pachete
time.sleep(5)
# dupa cele cateva secunde trimit semnalul SIGINT(^C) pentru a intrerupe procesul
subprocess.call(["kill", "-2", str(ping_process.pid)])
# pun output-ul procesului intr-o variabila
ping_output, _ = ping_process.communicate()
print(ping_output)
# Popen.terminate() sends SIGTERM


# creez o functie care pune intr-un dictionar numarul de pachete trimise, primite respectiv pierdute
def packets_sent_received_lost(output):
    packets = {}  # initializez dictionarul
    match = re.search(r'(\d+) packets transmitted, (\d+) received', ping_output)
    packets['transmitted'] = int(match.group(1))
    packets['received'] = int(match.group(2))
    packets['lost'] = packets['transmitted'] - packets['received']
    print('Packets :')
    for cheie in packets.keys():
        print('->', cheie, ':', packets[cheie])


# creez o functie care printeaza valorile TTL minim si TTL maxim
def TTL_min_max(output):
    match = re.findall(r'ttl=(\d+) ', output)
    ttl_min = 1000
    ttl_max = 0
    for ttl in match:
        if int(ttl) > ttl_max:
            ttl_max = int(ttl)
        elif int(ttl) < ttl_min:
            ttl_min = int(ttl)
    print('TTL min :', ttl_min)
    print('TTL max :', ttl_max)


# creez o functie care calculeaza media timpului si o compara cu cea din statistici
def average_time_calculator(output):
    match = re.findall(r'time=(.+) ms', output)
    suma = 0
    for time in match:
        suma += float(time)
    average_time = suma/len(match)
    match = re.search(r'rtt min/avg/max/mdev = (.+)/(.+)/', output)
    print('Average_time_calculated :', average_time)
    print('Average_time_statistics :', match.group(2))


def hide_IP_address(output):
    output = re.sub(r'(\d+).(\d+).(\d+).(\d+)', 'x.x.x.x', output, 100)
    print(output)


packets_sent_received_lost(ping_output)
average_time_calculator(ping_output)
TTL_min_max(ping_output)
hide_IP_address(ping_output)


"""
# DECOMENTATI ACEASTA SECTIUNE PENTRU WINDOWS

# retin intr-o variabila output-ul comenzii 'ping google.com'
ping_output = subprocess.check_output(["ping", "google.com"], universal_newlines=True)
print(ping_output)


# creez o functie care pune intr-un dictionar numarul de pachete trimise, primite respectiv pierdute
def packets_sent_received_lost(output):
    packets = {}  # initializez dictionarul
    for element in ['Sent', 'Received', 'Lost']:
        # re.match va returna None daca patternul nu incepe cu inceputul stringului
        match = re.search(element + r' = (\d+)', ping_output)
        packets[element] = int(match.group(1))
        print('Packets', element, ':', packets[element])


# creez o functie care printeaza valorile TTL minim si TTL maxim
def TTL_min_max(output):
    match = re.search(r'Minimum = (\d+)ms, Maximum = (\d+)ms', output)
    print('TTL min :', match.group(1))
    print('TTL max :', match.group(2))


# creez o functie care calculeaza media timpului si o compara cu cea din statistici
def average_time_calculator(output):
    match = re.findall(r'time=(\d+)ms', output)
    suma = 0
    for time in match:
        suma += int(time)
    average_time = suma/len(match)
    match = re.search(r'Average = (\d+)ms', output)
    print('Average_time_calculated :', average_time)
    print('Average_time_statistics :', match.group(1))


def hide_IP_address(output):
    output = re.sub(r'(\w+):(\w+):(\w+):(\w+)::(\w+)', 'x:x:x:x::x', output, 100)
    print(output)


packets_sent_received_lost(ping_output)
TTL_min_max(ping_output)
average_time_calculator(ping_output)
hide_IP_address(ping_output)

"""






