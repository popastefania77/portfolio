"""
Write a Python method that reads bytes from a specific range from a file.
Range min and max values are sent as parameters
"""
def read_bytes(file, start, stop):
    # deschid fisierul cu permisiuni de citire
    with open(file, 'rb') as fout:  # adaug b pentru fisierele binare
        fout.seek(start)  # setez pozitia cursorului
        data = fout.read(stop - start)  # file.read([size]) -> [size] = bytes
    print(data)

read_bytes('a.txt', 10, 100)
read_bytes('Screenshot 2023-06-27 101217.png', 10, 100)
