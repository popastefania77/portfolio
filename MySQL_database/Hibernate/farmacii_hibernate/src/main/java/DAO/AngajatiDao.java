    /*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package DAO;

import java.util.List;
import pojo.Angajati;
import pojo.Farmacii;
import java.util.Date;

/**
 *
 * @author popas
 */
public interface AngajatiDao {
    public void adaugaAngajati (Angajati angajat);
    public List<Angajati> afiseazaAngajati();
    public void modificaAngajati (int idAngajat, String nume, String prenume, Date data_nasterii, String adresa, String telefon, String functie, float salariu, Farmacii idFarmacie);
    public void stergeAngajat (Angajati angajat);
}

    
