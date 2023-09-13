package Controller;

import DAO.FarmaciiDao;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import jakarta.servlet.RequestDispatcher;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import pojo.Farmacii;
import DAOImpl.FarmaciiDaoImpl;

/**
 *
 * @author popas
 */
public class FarmaciiController extends HttpServlet {

	Farmacii farmacie = new Farmacii();
	FarmaciiDaoImpl farmacieDaoImpl = new FarmaciiDaoImpl();

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		if (request.getParameter("adaugaFarmacie") != null) {
			String denumire = request.getParameter("denumire");
			String telefon = request.getParameter("telefon");
			String sediu = request.getParameter("sediu");
			farmacie.setDenumire(denumire);
			farmacie.setTelefon(telefon);
			farmacie.setSediu(sediu);
			farmacieDaoImpl.adaugaFarmacii(farmacie);
			RequestDispatcher rd = request.getRequestDispatcher("adauga_Farmacie.jsp");
			rd.forward(request, response);
		}
	}

	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		if (request.getParameter("afiseazaFarmacii") != null) {
			List<Farmacii> listaFarmacii = new ArrayList();
			listaFarmacii = farmacieDaoImpl.afiseazaFarmacii();
			request.setAttribute("listaFarmacii", listaFarmacii);
			RequestDispatcher rd = request.getRequestDispatcher("tabela_Farmacii.jsp");
			rd.forward(request, response);
		}

		if (request.getParameter("modificaFarmacie") != null) {
			int id1 = Integer.parseInt(request.getParameter("idFarmacie"));
			String nume = request.getParameter("nume");
			String prenume = request.getParameter("prenume");
			String sectie = request.getParameter("sectie");
			farmacieDaoImpl.modificaFarmacii(id1, nume, prenume, sectie);
			RequestDispatcher rd = request.getRequestDispatcher("adauga_Farmacie.jsp");
			rd.forward(request, response);

		}

		if (request.getParameter("stergeFarmacie") != null) {
			int id2 = Integer.parseInt(request.getParameter("idFarmacie"));
			farmacie.setIdFarmacie(id2);
			farmacieDaoImpl.stergeFarmacie(farmacie);
			RequestDispatcher rd = request.getRequestDispatcher("adauga_Farmacie.jsp");
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


