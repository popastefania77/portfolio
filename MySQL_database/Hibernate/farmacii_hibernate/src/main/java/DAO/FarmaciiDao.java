    /*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package DAO;

import java.util.List;
import pojo.Farmacii;

/**
 *
 * @author popas
 */
public interface FarmaciiDao {
    public void adaugaFarmacii (Farmacii farmacie);
    public List<Farmacii> afiseazaFarmacii();
    public void modificaFarmacii (int idFarmacie, String denumire, String telefon, String sediu);
    public void stergeFarmacie (Farmacii farmacie);
}

    
