    /*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package DAO;

import java.util.List;
import pojo.Locatii;
import pojo.Farmacii;

/**
 *
 * @author popas
 */
public interface LocatiiDao {
    public void adaugaLocatii (Locatii locatie);
    public List<Locatii> afiseazaLocatii();
    public void modificaLocatii (int idLocatie, String numar, String strada, String oras, String judet, String telefon, Farmacii idFarmacie);
    public void stergeLocatie (Locatii locatie);
}

    
