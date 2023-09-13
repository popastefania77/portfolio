**Cerinta** : Creaţi două aplicaţii care să conţină o bază de date creată în sistemul de gestiune bazelor de date MySql şi două interfeţe la aceasta (baza de date este comună). La crearea interfeţelor se vor folosi două tehnologii(la alegere - ex.: PHP, JSP, Hibernate, JPA, .NET

etc.).

Tehnologia folosita pentru crearea bazei de date: **MySql**.

„ **MySql** este un sistem de gestiune a bazelor de date relationale, produsde compania **MySQL AB**. Este cel mai popular sistem de gestionare de acest fel.Se gaseste de obicei alaturi de limbajul **PHP** , insa cu **MySql** se pot construiaplicatii in orice limbaj. "

                                                                               - https://ro.wikipedia.org/wiki/MySQL

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

![image](https://github.com/popastefania77/portfolio/assets/137763813/303317e2-526c-4b9a-99ba-51337045b8ee)

<div align="center">
Figura 1 : diagrama asociata tabelelor
</div>


**Tehnologii utilizate**

**Java Server Pages (JSP)** este o tehnologie care ajută dezvoltatorii de software să creeze pagini Web generate dinamic, bazate pe HTML, XML sau alte tipuri de documente. Lansat în 1999 de Sun Microsystems, [1] JSP este similar cu PHP și ASP, dar utilizează limbajul de programare Java.

                                                                    - https://en.wikipedia.org/wiki/JavaServer\_Pages

Aceasta tehnologie permite crearea de interfete pentru paginiweb.

Pagina principala a interfetei ( **index.html** ) facuta prin aceastatehnologie permite accesul spre paginile de vizualizare ale tabelelor cat si spre paginile din care putemmodifica tabelele.

![image](https://github.com/popastefania77/portfolio/assets/137763813/e0bfcd53-7ffc-47e2-a034-ee5f677d6804)

<div align="center">
Figura 2 : Pagina principala a interfetei in tehnologie JSP
</div>
<br>

Din pagina principala, **index.html,** utilizatorul are posibilitatea vizualizarii sau modificarii oricarui tabel dintre cele 3 : **farmacii** , **angajati** si **locatii** , accesand butoanele corespunzatoare.

Accesand butonul **("View"**), utilizatorul poate vizualiza tabela dorita. In cazul accesarii butonului **("Edit")**, utilizatorul are posibilitatea modificarii tabelei prin operatii de stergere, modificare sau adaugare de noi instante ale tabelei.

![image](https://github.com/popastefania77/portfolio/assets/137763813/e1c673ec-99ab-4621-bca0-77588a64b318)

<div align="center">
Figura 3 : Vizualizare tabela farmacii
</div>
<br>


![image](https://github.com/popastefania77/portfolio/assets/137763813/774d8cb2-f4ed-4160-bde0-eba2da7f29e1)

<div align="center">
Figura 4 : Codul corespunzator functiei de vizualizare
</div>
<br>


![image](https://github.com/popastefania77/portfolio/assets/137763813/24931796-49eb-4657-9006-dce64099d2f3)

<div align="center">
Figura 5 : Modificare tabela farmacii
</div>
<br>


Odata cu accesarea paginii corespunzatoare pentru modificarea tabelei **farmacii** , se pot observa cele 3 butoane corespunzatoare diferitelor operatii (" **Adauga o noua farmacie**") (" **Modifica linia marcate**") (" **Sterge liniile marcate**") cat si butonul (" **Home**") care duce catre pagina de start.

![image](https://github.com/popastefania77/portfolio/assets/137763813/fa7430d2-f249-4c33-860f-05ff09517e9c)

<div align="center">
Figura 6 : Adaugare in tabela farmacii
</div>
<br>


![image](https://github.com/popastefania77/portfolio/assets/137763813/2d3eb3b8-3897-4a96-a96f-66c6c7cc82bf)

<div align="center">
Figura 7: Codul corespunzator functiei de adaugare
</div>
<br>


Dupa preluarea datelor va fi afisata o pagina cu mesajul care confirma adaugarea noii inregistrari : **"Datele au fost adaugate cu success "** , un buton **("MODIFICA TABELA FARMACII")** catre pagina de modificare si un buton **("Home")** catre pagina de start.

In cazul tabelelor **angajati** si **locatii** , adaugarea unei noi inregistrari este similara, dar apare in plus un drop-down pentru a putea alege din farmaciile disponibile.

![image](https://github.com/popastefania77/portfolio/assets/137763813/7113e930-6349-4aae-b555-abd37a35dcc4)

<div align="center">
Figura 8 : Drop-down farmacii disponibile
</div>
<br>

![](RackMultipart20230913-1-19znb0_html_840b4fa9210c885d.png)

<div align="center">
Figura 9 : Codul corespunzator pentru Drop-down farmacii disponibile
</div>
<br>

In cazul modificarii datelor, va fi afisata o pagina cu diferite mesaje referitoare la numarul de linii selectate pentru modificare. In cazul in care au fost slelectate prea multe linii se afiseaza: **"Ați selectat prea multe linii. Selectati doar una!"** , iar in cazul in care nu a fost selectata nicio linie se afiseaza: **"**** Nu ați selectat nicio linie!" **. Impreuna cu aceste mesaje sunt afisate si 2 butoane:** ("MODIFICA TABELA FARMACII") **catre pagina de modificare si un buton** ("Home")** catre pagina de start.

![image](https://github.com/popastefania77/portfolio/assets/137763813/698d1b16-5ce4-4a10-a7e4-f1515da20e4b)

<div align="center">
Figura 10 : Modificare linii din tabela farmacii
</div>
<br>


![image](https://github.com/popastefania77/portfolio/assets/137763813/ecbf849f-6130-47ce-a16c-8432a8defa8a)

<div align="center">
Figura 11 : Cod corespunzator modificare linii din tabela farmacii
</div>
<br>

Dupa preluarea datelor va fi afisata o pagina cu mesajul care confirma modificarea inregistrarii : **"Modificarile au fost realizate cu succes!"** , un buton **("MODIFICA TABELA FARMACII")** catre pagina de modificare si un buton **("Home")** catre pagina de start.

Pentru a sterge campuri din tabela se selecteaza campurile necesare, apoi se apasa pe butonul **("Sterge liniile marcate").**

In cazul stergerii datelor, va fi afisata o pagina cu mesajul **"**** Nu ați selectat nicio linie!" **in cazul in care nicio linie nu a fost selectata, respectiv o pagina cu mesajul :**"Datele au fost sterse cu succes!". **Impreuna cu aceste mesaje sunt afisate si 2 butoane :** ("MODIFICA TABELA FARMACII") **catre pagina de modificare si un hyperlink** ("Home")** catre pagina de start.

![image](https://github.com/popastefania77/portfolio/assets/137763813/2685d519-0eb9-48a4-8632-f3e89c185963)

<div align="center">
Figura 12 : Confirmarea stergerii datelor
</div>
<br>


![image](https://github.com/popastefania77/portfolio/assets/137763813/04478cbf-a80b-48e8-9873-0fdea77ee548)

<div align="center">
Figura 13: Cod corespunzator stergerii datelor</div>
</div>
<br>

In mod similar se procedeaza si pentru tabelele **angajati** si **locatii.**

De asemenea, in partea de jos a fiecarei pagini am adaugat un buton de (" **Back to top**"), util cand se aduna multe date in tabele.

Pentrua imbunatati aspectul paginilor am adaugat elemente de programareHTML, Cascading Style Sheets (CSS) si site-ul https://getbootstrap.com/.

**Bibliografie:**

1. [https://stackoverflow.com/](https://stackoverflow.com/)
2. https://ro.wikipedia.org/wiki/Pagina\_principal%C4%83[http://www.layoutit.com/](http://www.layoutit.com/)
3. [http://youtube.com/](http://youtube.com/)
4. [https://www.competentedigitale.ro/access/access\_cheie\_primara.php](https://www.competentedigitale.ro/access/access_cheie_primara.php)
5. https://getbootstrap.com/docs/4.0/examples/album/
