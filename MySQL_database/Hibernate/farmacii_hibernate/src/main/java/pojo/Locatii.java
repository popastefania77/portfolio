package pojo;



import java.util.HashSet;
import java.util.Set;

public class Locatii  implements java.io.Serializable {


	private Integer idLocatie;
	private String numar;
	private String strada;
	private String oras;
	private String judet;
	private String telefon;
	private Farmacii farmacii;

	public Locatii() {
	}

	public Locatii(String numar, String strada, String oras, String judet, String telefon, Farmacii farmacii) {
		this.numar = numar;
		this.strada = strada;
		this.oras = oras;
		this.judet = judet;
		this.telefon = telefon;
		this.farmacii = farmacii;
	}

	public Integer getIdLocatie() {
		return this.idLocatie;
	}

	public void setIdLocatie(Integer idLocatie) {
		this.idLocatie = idLocatie;
	}
	public String getNumar() {
		return this.numar;
	}

	public void setNumar(String numar) {
		this.numar = numar;
	}
	public String getStrada() {
		return this.strada;
	}

	public void setStrada(String strada) {
		this.strada = strada;
	}
	
	public String getOras() {
		return this.oras;
	}

	public void setOras(String oras) {
		this.oras = oras;
	}
	
	public String getJudet() {
		return this.judet;
	}

	public void setJudet(String judet) {
		this.judet = judet;
	}
	
	public String getTelefon() {
		return this.telefon;
	}

	public void setTelefon(String telefon) {
		this.telefon = telefon;
	}
	
	public Farmacii getFarmacii() {
		return this.farmacii;
	}

	public void setFarmacii(Farmacii farmacii) {
		this.farmacii = farmacii;
	}

}




