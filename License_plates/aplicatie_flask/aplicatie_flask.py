from flask import Flask, url_for, request
from app.lib import numere_de_inmatriculare
from app.lib import baza_date

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    ret = f'''<html>
<head>
    <title>Verificare Număr de Înmatriculare</title>
</head>
<body>
    <h1>Alegeti una dintre urmatoarele optiuni:</h1>
    <h3><a href={url_for('verificare_corectitudine')}>VERIFICARE CORECTITUDINE NUMAR DE INMATRICULARE</a><h3>
    <h3><a href={url_for('verificare_existenta')}>VERIFICARE EXSITENTA NUMAR DE INMATRICULARE IN BAZA DE DATE</a><h3>
    <h3><a href={url_for('adaugare_in_baza_date')}>ADAUGARE NUMAR DE INMATRICULARE IN BAZA DE DATE</a><h3>
    <h3><a href={url_for('vizualizare_baza_date')}>VIZUALIZARE BAZA DE DATE</a><h3>
</body>
</html>
'''
    return ret




@app.route("/verificare_corectitudine", methods=['GET', 'POST'])
def verificare_corectitudine():
    message = ''
    if request.method == 'POST':
        numar_inmatriculare = request.form.get('numar_inmatriculare')
        #print('numar_inmatriculare', numar_inmatriculare)
        if numere_de_inmatriculare.verificare(numar_inmatriculare):
            message = f"Numărul de inmatriculare {numar_inmatriculare} este valid."
        else:
            message = f"Numărul de inmatriculare {numar_inmatriculare} nu este valid."
    ret = f'''<html>
<head>
    <title>Verificare corectitudine Număr de Înmatriculare</title>
</head>
<body>
    <p><a href={url_for('index')}>REVENIRE LA PAGINA PRINCIPALA</a></p>
    <h1>Verificare corectitudine Număr de Înmatriculare</h1>
    <form method="POST">
        <label for="numar_inmatriculare">Introduceți numărul de înmatriculare:</label>
        <input type="text" id="numar_inmatriculare" name="numar_inmatriculare" required>
        <button type="submit">Verifică</button>
    </form>
    <p>{ message }</p>
</body>
</html>
'''
    return ret
    
    
@app.route("/verificare_existenta", methods=['GET', 'POST'])
def verificare_existenta():
    message = ''
    if request.method == 'POST':
        numar_inmatriculare = request.form.get('numar_inmatriculare')
        # decomentati pentru docker
        # if baza_date.verificare_existenta('/home/aplicatie_flask/baza_date.txt', numar_inmatriculare):
        # comentati pentru docker
        if baza_date.verificare_existenta('baza_date.txt', numar_inmatriculare):
            message = f"Numărul de inmatriculare {numar_inmatriculare} exista in baza de date."
        else:
            message = f"Numărul de inmatriculare {numar_inmatriculare} nu exista in baza de date."
    ret = f'''<html>
<head>
    <title>Verificare existenta Număr de Înmatriculare in baza de date</title>
</head>
<body>
    <p><a href={url_for('index')}>REVENIRE LA PAGINA PRINCIPALA</a></p>
    <h1>Verificare existenta Număr de Înmatriculare in baza de date</h1>
    <form method="POST">
        <label for="numar_inmatriculare">Introduceți numărul de înmatriculare:</label>
        <input type="text" id="numar_inmatriculare" name="numar_inmatriculare" required>
        <button type="submit">Verifică</button>
    </form>
    <p>{ message }</p>
</body>
</html>
'''
    return ret
    

@app.route("/adaugare_in_baza_date", methods=['GET', 'POST'])
def adaugare_in_baza_date():
    message = ''
    if request.method == 'POST':
        numar_inmatriculare = request.form.get('numar_inmatriculare')
        nume_prenume = request.form.get('nume_prenume')
        # decomentati pentru docker
        # message = baza_date.adaugare_in_baza_date('/home/aplicatie_flask/baza_date.txt', numar_inmatriculare, nume_prenume)
        # comentati pentru docker
        message = baza_date.adaugare_in_baza_date('baza_date.txt', numar_inmatriculare, nume_prenume)
            
    ret = f'''<html>
<head>
    <title>Adaugare Număr de Înmatriculare in baza de date</title>
</head>
<body>
    <p><a href={url_for('index')}>REVENIRE LA PAGINA PRINCIPALA</a></p>
    <h1>Verificare existenta Număr de Înmatriculare in baza de date</h1>
    <form method="POST">
        <label for="numar_inmatriculare">Introduceți numărul de înmatriculare:</label>
        <input type="text" id="numar_inmatriculare" name="numar_inmatriculare" required>
        <br><br>
        <label for="nume si prenume">Introduceți Numele si Prenumele:    </label>
        <input type="text" id="nume_prenume" name="nume_prenume" required>
        <br>
        <button type="submit">Adauga</button>
    </form>
    <p>{ message }</p>
</body>
</html>
'''
    return ret
    
@app.route("/vizualizare_baza_date", methods=['GET'])
def vizualizare_baza_date():
    # decomentati pentru docker
    # message = baza_date.vizualizare_baza_date('/home/aplicatie_flask/baza_date.txt')
    # comentati pentru docker
    message = baza_date.vizualizare_baza_date('baza_date.txt')
    ret = f'''<html>
<head>
    <title>Vizualizare baza de date</title>
</head>
<body>
    <p><a href={url_for('index')}>REVENIRE LA PAGINA PRINCIPALA</a></p>
    <h1>Vizualizare baza de date</h1>
    <h3><pre>{ message }</pre></h3>
</body>
</html>
'''
    return ret



