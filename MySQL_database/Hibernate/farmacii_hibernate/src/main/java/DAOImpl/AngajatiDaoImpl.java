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
import pojo.Angajati;
import pojo.Farmacii;
import DAO.AngajatiDao;
import DAO.FarmaciiDao;
import java.util.Date;

/**
 *
 * @author popas
 */
public class AngajatiDaoImpl implements AngajatiDao{

    public void adaugaAngajati(Angajati angajat) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction transaction = session.beginTransaction();
        session.save(angajat);
        transaction.commit();
        session.close();
    }

    public List<Angajati> afiseazaAngajati() {
        List<Angajati> listaAngajati = new ArrayList();
        Session session = HibernateUtil.getSessionFactory().openSession();
        org.hibernate.Query query = session.createQuery("From Angajati");
        listaAngajati = query.list();
        return listaAngajati;
    }

    public void modificaAngajati(int idAngajat, String nume, String prenume, Date data_nasterii, String adresa, String telefon, String functie, float salariu, Farmacii farmacie) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction transaction = session.beginTransaction();
        Angajati detaliiangajati = (Angajati) session.load(Angajati.class, idAngajat);
        detaliiangajati.setNume(nume);
        detaliiangajati.setPrenume(prenume);
        detaliiangajati.setData_nasterii(data_nasterii);
        detaliiangajati.setAdresa(adresa);
        detaliiangajati.setTelefon(telefon);
        detaliiangajati.setFunctie(functie);
        detaliiangajati.setSalariu(salariu);
        detaliiangajati.setFarmacii(farmacie);
        session.update(detaliiangajati);
        transaction.commit();
        session.close();
    }

    public void stergeAngajat(Angajati angajat) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction transaction = session.beginTransaction();
        session.delete(angajat);
        transaction.commit();
        session.close();
    }
}
