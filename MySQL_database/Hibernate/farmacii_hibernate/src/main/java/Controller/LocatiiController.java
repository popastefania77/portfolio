package Controller;

import DAO.LocatiiDao;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.hibernate.Session;

import jakarta.servlet.RequestDispatcher;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import pojo.Locatii;
import pojo.Farmacii;
import DAOImpl.HibernateUtil;
import DAOImpl.LocatiiDaoImpl;

/**
 *
 * @author popas
 */
public class LocatiiController extends HttpServlet {

	Locatii locatie = new Locatii();
	LocatiiDaoImpl locatieDaoImpl = new LocatiiDaoImpl();

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		if (request.getParameter("adaugaLocatie") != null) {
			String numar = request.getParameter("numar");
			String strada = request.getParameter("strada");
			String oras = request.getParameter("oras");
			String judet = request.getParameter("judet");
			String telefon = request.getParameter("telefon");
			Integer idFarmacie = java.lang.Integer.parseInt(request.getParameter("idFarmacie"));
			Session session = HibernateUtil.getSessionFactory().openSession();
			Farmacii farmacie = (Farmacii) session.get(Farmacii.class, idFarmacie);
			locatie.setNumar(numar);
			locatie.setStrada(strada);
			locatie.setOras(oras);
			locatie.setJudet(judet);
			locatie.setTelefon(telefon);
			locatie.setFarmacii(farmacie);
			locatieDaoImpl.adaugaLocatii(locatie);
			RequestDispatcher rd = request.getRequestDispatcher("adauga_Locatie.jsp");
			rd.forward(request, response);
		}
	}

	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		if (request.getParameter("afiseazaLocatii") != null) {
			List<Locatii> listaLocatii = new ArrayList();
			listaLocatii = locatieDaoImpl.afiseazaLocatii();
			request.setAttribute("listaLocatii", listaLocatii);
			RequestDispatcher rd = request.getRequestDispatcher("tabela_Locatii.jsp");
			rd.forward(request, response);
		}

		if (request.getParameter("modificaLocatie") != null) {
			int id1 = Integer.parseInt(request.getParameter("idLocatie"));
			String numar = request.getParameter("numar");
			String strada = request.getParameter("strada");
			String oras = request.getParameter("oras");
			String judet = request.getParameter("judet");
			String telefon = request.getParameter("telefon");
			Integer idFarmacie = java.lang.Integer.parseInt(request.getParameter("idFarmacie"));
			Session session = HibernateUtil.getSessionFactory().openSession();
			Farmacii farmacie = (Farmacii) session.get(Farmacii.class, idFarmacie);
			locatieDaoImpl.modificaLocatii(id1, numar, strada, oras, judet, telefon, farmacie);
			RequestDispatcher rd = request.getRequestDispatcher("adauga_Locatie.jsp");
			rd.forward(request, response);

		}

		if (request.getParameter("stergeLocatie") != null) {
			int id2 = Integer.parseInt(request.getParameter("idLocatie"));
			locatie.setIdLocatie(id2);
			locatieDaoImpl.stergeLocatie(locatie);
			RequestDispatcher rd = request.getRequestDispatcher("adauga_Locatie.jsp");
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


