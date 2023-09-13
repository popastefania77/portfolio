package pojo;



import java.util.HashSet;
import java.util.Set;

public class Farmacii  implements java.io.Serializable {


	private Integer idFarmacie;
	private String denumire;
	private String telefon;
	private String sediu;
	private Set angajati = new HashSet(0);
	private Set locatii = new HashSet(0);
	public Farmacii() {
	}

	public Farmacii(String denumire, String telefon, String sediu, Set angajati, Set locatii) {
		this.denumire = denumire;
		this.telefon = telefon;
		this.sediu = sediu;
		this.angajati = angajati;
		this.locatii = locatii;
	}

	public Integer getIdFarmacie() {
		return this.idFarmacie;
	}

	public void setIdFarmacie(Integer idFarmacie) {
		this.idFarmacie = idFarmacie;
	}
	public String getDenumire() {
		return this.denumire;
	}

	public void setDenumire(String denumire) {
		this.denumire = denumire;
	}

	public String getTelefon() {
		return this.telefon;
	}

	public void setTelefon(String telefon) {
		this.telefon = telefon;
	}
	
	public String getSediu() {
		return this.sediu;
	}

	public void setSediu(String sediu) {
		this.sediu = sediu;
	}
	
	public Set getAngajati() {
		return this.angajati;
	}
	public void setAngajati(Set angajati) {
		this.angajati = angajati;
	}

	public Set getLocatii() {
		return this.locatii;
	}

	public void setLocatii(Set locatii) {
		this.locatii = locatii;
	}
}




