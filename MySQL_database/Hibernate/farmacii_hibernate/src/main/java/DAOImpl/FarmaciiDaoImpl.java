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
import pojo.Farmacii;
import DAO.FarmaciiDao;

/**
 *
 * @author popas
 */
public class FarmaciiDaoImpl implements FarmaciiDao{

    public void adaugaFarmacii(Farmacii farmacie) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction transaction = session.beginTransaction();
        session.save(farmacie);
        transaction.commit();
        session.close();
    }

    public List<Farmacii> afiseazaFarmacii() {
        List<Farmacii> listaFarmacii = new ArrayList();
        Session session = HibernateUtil.getSessionFactory().openSession();
        org.hibernate.Query query = session.createQuery("From Farmacii");
        listaFarmacii = query.list();
        return listaFarmacii;
    }

    public void modificaFarmacii(int idFarmacie, String denumire, String telefon, String sediu) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction transaction = session.beginTransaction();
        Farmacii detaliifarmacii = (Farmacii) session.load(Farmacii.class, idFarmacie);
        detaliifarmacii.setDenumire(denumire);
        detaliifarmacii.setTelefon(telefon);
        detaliifarmacii.setSediu(sediu);
        session.update(detaliifarmacii);
        transaction.commit();
        session.close();
    }

    public void stergeFarmacie(Farmacii farmacie) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction transaction = session.beginTransaction();
        session.delete(farmacie);
        transaction.commit();
        session.close();
    }
}
