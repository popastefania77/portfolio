package pojo;


import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;


public class Angajati  implements java.io.Serializable {


	private Integer idAngajat;
	private String nume;
	private String prenume;
	private Date data_nasterii;
	private String adresa;
	private String telefon;
	private String functie;
	private float salariu;
	private Farmacii farmacii;

	public Angajati() {
	}

	public Angajati(String nume, String prenume, Date data_nasterii, String adresa, String telefon, String functie, float salariu, Farmacii farmacii) {
		this.nume = nume;
		this.prenume = prenume;
		this.data_nasterii = data_nasterii;
		this.adresa = adresa;
		this.telefon = telefon;
		this.functie = functie;
		this.salariu = salariu;
		this.farmacii = farmacii;
	}

	public Integer getIdAngajat() {
		return this.idAngajat;
	}

	public void setIdAngajat(Integer idAngajat) {
		this.idAngajat = idAngajat;
	}
	public String getNume() {
		return this.nume;
	}

	public void setNume(String nume) {
		this.nume = nume;
	}
	public String getPrenume() {
		return this.prenume;
	}

	public void setPrenume(String prenume) {
		this.prenume = prenume;
	}
	public Date getData_nasterii() {
		return this.data_nasterii;
	}

	public void setData_nasterii(Date data_nasterii) {
		this.data_nasterii = data_nasterii;
	}

	public String getAdresa() {
		return this.adresa;
	}

	public void setAdresa(String adresa) {
		this.adresa = adresa;
	}
	public String getTelefon() {
		return this.telefon;
	}

	public void setTelefon(String telefon) {
		this.telefon = telefon;
	}
	public String getFunctie() {
		return this.functie;
	}

	public void setFunctie(String functie) {
		this.functie = functie;
	}
	public float getSalariu() {
		return this.salariu;
	}
	public void setSalariu(float salariu) {
		this.salariu = salariu;
	}
	public Farmacii getFarmacii() {
		return this.farmacii;
	}

	public void setFarmacii(Farmacii farmacii) {
		this.farmacii = farmacii;
	}
	
	
}




