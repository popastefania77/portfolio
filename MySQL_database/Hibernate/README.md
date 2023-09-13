**Cerinta** : Creaţi două aplicaţii care să conţină o bază de date creată în sistemul de gestiune bazelor de date MySql şi două interfeţe la aceasta (baza de date este comună). La crearea interfeţelor se vor folosi două tehnologii(la alegere - ex.: PHP, JSP, Hibernate, JPA, .NET

etc.).

Tehnologia folosita pentru crearea bazei de date: **MySql**.

„ **MySql** este un sistem de gestiune a bazelor de date relationale, produsde compania **MySQL AB**. Este cel mai popular sistem de gestionare de acest fel.Se gaseste de obicei alaturi de limbajul **PHP** , insa cu **MySql** se pot construiaplicatii in orice limbaj. "

-https://ro.wikipedia.org/wiki/MySQL

Am realizat o baza de date in MySQL WORKBENCH , ea continand 3 tabele : **angajati, farmacii si locatii**. Asocierea dintre ele este de tipul M:1, respectiv 1:N.

Tabela **angajati** contine urmatoare coloane:

| **idAngajat** | int AI PK |
| --- | --- |
| nume | varchar(10) |
| prenume | varchar(10) |
| data\_nasterii | date |
| adresa | varchar(45) |
| telefon | varchar(10) |
| functie | varchar(20) |
| salariu | float |
| **idFarmacie** | int |

Tabela **farmacii** contine urmatoarele coloane :

| **idFarmacie** | int AI PK |
| --- | --- |
| **denumire** | varchar(10) |
| telefon | varchar(10) |
| sediu | varchar(10) |

Tabela contine urmatoarele coloane :

| **idLocatie** | int AI PK |
| --- | --- |
| numar | varchar(5) |
| strada | varchar(20) |
| oras | varchar(10) |
| judet | varchar(10) |
| telefon | varchar(10) |
| **idFarmacie** | int |

Datorita asocierii M:1 dintre angajati si farmacii, idFarmacie este cheie straina in tabela angajati.

Datorita asocierii 1:N dintre farmacii si locatii, idFarmacie este cheie straina in tabela locatii.

Cheile primare(PK) corespunzatoare fiecarei tabele au fost setate cu proprietatea de auto-increment (AI).

**Cheie primara** :Este un câmp care identifică în mod unic înregistrările unei tabele.

- https://www.competentedigitale.ro/access/access\_cheie\_primara.php

Diagrama asociata tabelelor este reprezentata in figura de mai jos :

![image](https://github.com/popastefania77/portfolio/assets/137763813/b5afc161-d0e0-4410-9df9-cf8ab07b837b)

<div align="center">
    Figura 1 : diagrama asociata tabelelor
</div>

**Tehnologii utilizate**

**Hibernate ORM este** un instrument de mapare obiect-relațional pentru limbajul de programare Java. Acesta oferă un cadru pentru cartografierea unui model de domeniu orientat pe obiecte într-o bază de date relațională. Hibernate se ocupă de problemele de nepotrivire a impedanței obiect-relaționale prin înlocuirea accesurilor directe și permanente ale bazei de date cu funcții de manipulare a obiectelor la nivel înalt.

-https://en.wikipedia.org/wiki/Hibernate\_(framework)

Aceasta tehnologie permite crearea de interfete pentru paginiweb.

Pagina principala a interfetei ( **index.html** ) facuta prin aceastatehnologie permite accesul spre paginile de adaugare in cele 3 tabele : **farmacii** , **angajati** si **locatii** , accesand butoanele corespunzatoare.

![image](https://github.com/popastefania77/portfolio/assets/137763813/289a0729-ca28-499d-a32e-4024e15d7d8b)



<div align="center">
    Figura 2 : Pagina principala a interfetei in tehnologie Hibernate
</div>
<br>


Accesand butonul ("ADD"), utilizatorul ajunge in pagina de adaugare in tabel. Odata cu accesarea paginii corespunzatoare pentru modificarea tabelei **farmacii** , se poate observa 3 butoane: (" **Adauga farmacie**") ("**Afiseaza farmacii")** cat si butonul (" **Home**") care duce catre pagina de start.

![image](https://github.com/popastefania77/portfolio/assets/137763813/0431bc69-d4f8-4520-99a8-1238854c1bba)


<div align="center">
Figura 3 : Adaugare farmacie
</div>
<br>

In cazul tabelelor **angajati** si **locatii** , adaugarea unei noi inregistrari este similara, dar apare in plus un drop-down pentru a putea alege din farmaciile disponibile.

![image](https://github.com/popastefania77/portfolio/assets/137763813/968380c0-e5fc-4793-9e06-cf2d53e192d0)


<div align="center">
Figura 4 : Drop-down farmacii disponibile

![image](https://github.com/popastefania77/portfolio/assets/137763813/9191aa76-b43a-4868-af95-65e6ab15d2c8)
<br>
</div>



<div align="center">
Figura 5 : Cod corespundator adaugare farmacie
</div>
<br>

Odata cu accesarea paginii corespunzatoare pentru vizualizarea tabelei **farmacii** , se pot observa cele 2 mark-uri corespunzatoare diferitelor operatii (" **Modifica**") (" **Sterge**") cat si butonul (" **Home**") care duce catre pagina de start.

![image](https://github.com/popastefania77/portfolio/assets/137763813/a252a4d6-dd3f-4266-af4f-7941172b9cb1)


<div align="center">
Figura 6 : Vizualizare tabela farmacii 1
</div>
<br>


![image](https://github.com/popastefania77/portfolio/assets/137763813/18a3412b-878e-4b1a-8ee5-00207edc3cc9)


<div align="center">
Figura 7 : Vizualizare tabela farmacii 2
</div>
<br>


![image](https://github.com/popastefania77/portfolio/assets/137763813/61703dcf-9487-469f-84f1-926df2fbece2)


<div align="center">
Figura 8 : Vizualizare tabela farmacii 3
</div><br>


Din acest meniu se poate realiza stergerea sau modificarea unei linii, prin bifarea optiunii dorite. Dupa bifarea si selectarea liniei dorite, se va activa butonul (" **Modifica**"), respectiv (" **Sterge**"), dar nu amandoua simultan. De asemenea, se poate obseva faptul ca atunci cand se activeaza butonul (" **Sterge**"), campurile de deasupra nu se pt modifica (devin readonly).

![image](https://github.com/popastefania77/portfolio/assets/137763813/cc3a0f60-a173-49e0-8412-d19482161bfa)


<div align="center">
 Figura 9 : Cod corespunzator afisare, modificare, stergere farmacie
</div>
<br>


In mod similar se procedeaza si pentru tabelele **angajati** si **locatii.**

De asemenea, in partea de jos a fiecarei pagini am adaugat un buton de (" **Back to top**"), util cand se aduna multe date in tabele.

Baza de date facuta in MySql este comuna celor 2 tehnologii, decio modificarefacutainunadinelevafivizibilasi in cealalta.

Pentruaimbunatatiaspectul paginilor am adaugat elemente de programare **HTML,** **Cascading Style Sheets (CSS)** si site-ulhttps://getbootstrap.com/.

**Bibliografie:**

1. [https://stackoverflow.com/](https://stackoverflow.com/)
2. https://ro.wikipedia.org/wiki/Pagina\_principal%C4%83[http://www.layoutit.com/](http://www.layoutit.com/)
3. [http://youtube.com/](http://youtube.com/)
4. [https://www.competentedigitale.ro/access/access\_cheie\_primara.php](https://www.competentedigitale.ro/access/access_cheie_primara.php)
5. https://getbootstrap.com/docs/4.0/examples/album/
