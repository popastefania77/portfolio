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

![image](https://github.com/popastefania77/portfolio/assets/137763813/b5afc161-d0e0-4410-9df9-cf8ab07b837b)
