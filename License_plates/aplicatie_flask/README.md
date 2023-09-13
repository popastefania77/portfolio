# Descrierea aplicatiei
Aplicația de verificare a numerelor de înmatriculare este o soluție dezvoltată pentru a gestiona și verifica numerele de înmatriculare ale vehiculelor. Această aplicație oferă funcționalități esențiale 
pentru a lucra cu aceste numere de înmatriculare, inclusiv verificarea corectitudinii, verificarea existenței în baza de date, adăugarea lor în baza de date și vizualizarea conținutului bazei de date.

Poate fi executata doar pe Linux. A fost testata pe Ubuntu 22.04.
Componenta WEB a aplicatiei se bazeaza pe framework-ul `Flask`.

Pentru o navigare mai usoara in browser, pagina principala contine link-uri catre celelalte pagini.
Fiecare pagina specifica contine un link catre pagina principala.
Aplicatia include suport pentru containerizare in fisierul `Dockerfile` din directorul principal al aplicatiei.

## Adaugare link-uri intre pagini:<br>
* ruta standard '/' - URL: http://127.0.0.1:5011
* rute in aplicatia WEB pentru:
  * Verificare corectitudine Număr de Înmatriculare: '/verificare_corectitudine' - URL: 'http://127.0.0.1:5011/verificare_corectitudine'
  * Verificare existenta Număr de Înmatriculare in baza de date: '/verificare_existenta' - URL: 'http://127.0.0.1:5011/verificare_existenta'
  * Adaugare Număr de Înmatriculare in baza de date: '/adaugare_in_baza_date' - URL: 'http://127.0.0.1:5011/adaugare_in_baza_date'
  * Vizualizare baza de date: '/vizualizare_baza_date - URL: 'http://127.0.0.1:5011/vizualizare_baza_date'


# Funcționalități Principale

## Verificare Corectitudine Număr de Înmatriculare:

Această funcționalitate permite utilizatorilor să introducă un număr de înmatriculare și să verifice dacă acesta respectă formatul corect al numărului de înmatriculare pentru regiunea sau țara specifică.
## Verificare Existenta Număr de Înmatriculare în Baza de Date:

Utilizatorii pot folosi această opțiune pentru a verifica dacă un număr de înmatriculare specific există deja în baza de date a aplicației. Astfel, pot afla dacă vehiculul respectiv este înregistrat sau nu.
## Adăugare Număr de Înmatriculare în Baza de Date:

Această funcționalitate permite utilizatorilor să adauge noi numere de înmatriculare în baza de date a aplicației. Acest lucru este util pentru înregistrarea unui nou vehicul sau actualizarea datelor.
## Vizualizare Bază de Date:

Utilizatorii pot accesa această opțiune pentru a vizualiza întregul conținut al bazei de date a aplicației. Aceasta furnizează o perspectivă generală asupra tuturor numerelor de înmatriculare înregistrate.
# Utilizare
Aplicația este destinată utilizării de către agenții de înmatriculare, proprietari de vehicule și oricare altă persoană sau organizație care are nevoie să gestioneze și să verifice numerele de înmatriculare ale vehiculelor.

Această aplicație reprezintă o resursă utilă pentru a asigura integritatea datelor legate de înmatriculare și pentru a oferi acces facil la informații relevante despre vehicule.


# Configurare

Configurare .venv si instalare pachete

In directorul 'aplicatie_flask' rulati comenzile:

1) activeaza_venv: Incearca sa activeze venv-ul. 
                   Daca nu poate, configureaza venv-ul in directorul .venv si apoi instaleaza flask si flask-bootstrap.
                   La urmatoarea rulare, va activa doar venv-ul.
                
2) ruleaza_aplicatia: De rulat doar dupa activarea venv-ului. 
                      Va porni serverul pe IP: 127.0.0.1 si port: 5011.
                      Acces server din browser: http://127.0.0.1:5011

# Docker
Aplicatia poate fi instalata intr-un container docker.

Pentru aceasta, este nevoie de fisierul: Dockerfile.
Acesta contine informatiile de care are nevoie aplicatia docker pentru a crea containerul.

## Cerinte
Docker sa fie disponibil pe calculator.

## Creare container
Dupa creerea Dockerfile, in acelasi director cu acest fisier - pentru acest caz
aplicatie_flask, trebuie executata comanda:

    sudo docker build -t sysinfo:v01 .

Aceasta creeaza o imagine de container care poate fi vizualizata cu comanda:
    
    sudo docker images
## Executie container
Pentru a genera un container din fisierul imagine trebuie executata comanda run:

    sudo docker run --name sysinfo -p 8020:5011 sysinfo:v01 
    
    Aceasta va crea containerul si va si porni executia acestuia.
    
    Portul pe calculator unde va raspunde serverul din docker este  - 8020
    Portul in interiorul containerului este                         - 5011.

## Vizualizare containere


    - vizualizare continere care ruleaza

    sudo docker ps

    - vizualizarea tuturor containerelor (inclusiv cele oprite)

    sudo docker ps -a

# EXEMPLU activare venv si rulare

![image](https://github.com/popastefania77/portfolio/assets/137763813/fda5edbf-d5b0-42d9-a37d-f5e3c7251e92)

# EXEMPLE pagina web 
## Pagina principala

![image](https://github.com/popastefania77/portfolio/assets/137763813/93fce915-a399-446a-9646-f6fdd1c52d90)

