package Controller;

import DAO.AngajatiDao;
import java.io.IOException;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import org.hibernate.Session;

import jakarta.servlet.RequestDispatcher;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import pojo.Angajati;
import pojo.Farmacii;
import DAOImpl.AngajatiDaoImpl;
import DAOImpl.HibernateUtil;

/**
 *
 * @author popas
 */
public class AngajatiController extends HttpServlet {

	Angajati angajat = new Angajati();
	AngajatiDaoImpl angajatDaoImpl = new AngajatiDaoImpl();

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		if (request.getParameter("adaugaAngajat") != null) {
			// preluarea parametrilor de interes
			Integer idFarmacie = java.lang.Integer.parseInt(request.getParameter("idFarmacie"));
			Session session = HibernateUtil.getSessionFactory().openSession();
			Farmacii farmacie = (Farmacii) session.get(Farmacii.class, idFarmacie);
			String nume = request.getParameter("nume");
			String prenume = request.getParameter("prenume");
			String adresa = request.getParameter("adresa");
			DateFormat df = new SimpleDateFormat("yyyy-MM-dd");
			Date data_nasterii = null;
			try {
				data_nasterii = df.parse(request.getParameter("data_nasterii"));
			} catch (ParseException e) {
				e.printStackTrace();
			}			String telefon = request.getParameter("telefon");
			String functie = request.getParameter("functie");
			Float salariu = java.lang.Float.parseFloat(request.getParameter("salariu"));
			angajat.setNume(nume);
	        angajat.setPrenume(prenume);
	        angajat.setData_nasterii(data_nasterii);
	        angajat.setAdresa(adresa);
	        angajat.setTelefon(telefon);
	        angajat.setFunctie(functie);
	        angajat.setSalariu(salariu);
	        angajat.setFarmacii(farmacie);
	        
			angajatDaoImpl.adaugaAngajati(angajat);
			RequestDispatcher rd = request.getRequestDispatcher("adauga_Angajat.jsp");
			rd.forward(request, response);
		}
	}

	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		if (request.getParameter("afiseazaAngajati") != null) {
			List<Angajati> listaAngajati = new ArrayList();
			listaAngajati = angajatDaoImpl.afiseazaAngajati();
			request.setAttribute("listaAngajati", listaAngajati);
			RequestDispatcher rd = request.getRequestDispatcher("tabela_Angajati.jsp");
			rd.forward(request, response);
		}

		if (request.getParameter("modificaAngajat") != null) {
			int id1 = Integer.parseInt(request.getParameter("idAngajat"));
			Integer idFarmacie = Integer.parseInt(request.getParameter("idFarmacie"));
			Session session = HibernateUtil.getSessionFactory().openSession();
			Farmacii farmacie = (Farmacii) session.get(Farmacii.class, idFarmacie);
			String nume = request.getParameter("nume");
			String prenume = request.getParameter("prenume");
			String adresa = request.getParameter("adresa");
			String telefon = request.getParameter("telefon");
			String functie = request.getParameter("functie");
			DateFormat df = new SimpleDateFormat("yyyy-MM-dd");
			Date data_nasterii = null;
			try {
				data_nasterii = df.parse(request.getParameter("data_nasterii"));
			} catch (ParseException e) {
				e.printStackTrace();
			}
			
			float salariu = 0;
			if (request.getParameter("salariu") != null) {
				salariu = Float.parseFloat(request.getParameter("salariu"));
			} else {
				salariu = angajat.getSalariu();
			}
			angajatDaoImpl.modificaAngajati(id1, nume, prenume, data_nasterii, adresa, telefon, functie, salariu, farmacie);
			RequestDispatcher rd = request.getRequestDispatcher("adauga_Angajat.jsp");
			rd.forward(request, response);

		}

		if (request.getParameter("stergeAngajat") != null) {
			int id2 = Integer.parseInt(request.getParameter("idAngajat"));
			angajat.setIdAngajat(id2);
			angajatDaoImpl.stergeAngajat(angajat);
			RequestDispatcher rd = request.getRequestDispatcher("adauga_Angajat.jsp");
			rd.forward(request, response);
		}
	}

	/**
	 * Returns a short description of the servlet.
	 *
	 * @return a String containing servlet description
	 */
	@Override
	public String getServletInfo() {
		return "Short description";
	}// </editor-fold>

}


