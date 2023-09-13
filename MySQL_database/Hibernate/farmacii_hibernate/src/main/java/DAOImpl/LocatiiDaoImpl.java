/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package DAOImpl;

import java.util.ArrayList;
import java.util.List;
import javax.persistence.Query;
import org.hibernate.Session;
import org.hibernate.Transaction;
import pojo.Locatii;
import pojo.Farmacii;
import DAO.LocatiiDao;

/**
 *
 * @author vali
 */
public class LocatiiDaoImpl implements LocatiiDao{

    public void adaugaLocatii(Locatii locatie) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction transaction = session.beginTransaction();
        session.save(locatie);
        transaction.commit();
        session.close();
    }

    public List<Locatii> afiseazaLocatii() {
        List<Locatii> listaLocatii = new ArrayList();
        Session session = HibernateUtil.getSessionFactory().openSession();
        org.hibernate.Query query = session.createQuery("From Locatii");
        listaLocatii = query.list();
        return listaLocatii;
    }

    public void modificaLocatii(int idLocatie, String numar, String strada, String oras, String judet, String telefon, Farmacii farmacie) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction transaction = session.beginTransaction();
        Locatii detaliilocatii = (Locatii) session.load(Locatii.class, idLocatie);
        detaliilocatii.setNumar(numar);
        detaliilocatii.setStrada(strada);
        detaliilocatii.setOras(oras);
        detaliilocatii.setJudet(judet);
        detaliilocatii.setTelefon(telefon);
        detaliilocatii.setFarmacii(farmacie);
        session.update(detaliilocatii);
        transaction.commit();
        session.close();
    }

    public void stergeLocatie(Locatii locatie) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction transaction = session.beginTransaction();
        session.delete(locatie);
        transaction.commit();
        session.close();
    }
}
