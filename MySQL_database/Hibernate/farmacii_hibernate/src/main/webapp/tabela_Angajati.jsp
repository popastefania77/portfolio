<%-- 
    Document   : tabela_Angajati
    Created on : Nov 22, 2016, 6:20:29 PM
    Author     : popas
--%>
<%@page import="DAOImpl.FarmaciiDaoImpl"%>
<%@page import="pojo.Farmacii"%>
<%@page import="java.util.ArrayList"%>
<%@page import="java.util.List"%>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="/docs/4.0/assets/img/favicons/favicon.ico">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Tabela Angajati</title>
            <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script>
            $(document).ready(function () {
                $("#stergeAngajat").hide();
                $("#modificaAngajat").hide();

                $("#update").click(function () {
                    $("#modificaAngajat").show();
                    $("#stergeAngajat").hide();
                });
                $("#delete").click(function () {
                    $("#stergeAngajat").show();
                    $("#modificaAngajat").hide();
                });
            });
        </script>
    
    <link href="https://getbootstrap.com/docs/4.0/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <!-- Link to Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link href="farmacii.css" rel="stylesheet">
    <script src="bootstrap-scripts.js"></script>
</head>

<body>
	<header>
	      <div class="collapse bg-dark" id="navbarHeader">
	        <div class="container">
	          <div class="row">
	            <div class="col-sm-8 col-md-7 py-4">
	              <h4 class="text-white">About</h4>
	              <p class="text-muted">Proiectul "FARMACII DATABASE" constă în dezvoltarea unei aplicații web pentru gestionarea și monitorizarea informațiilor legate de diferite farmacii.</p>
	            </div>
	            <div class="col-sm-4 offset-md-1 py-4">
	              <h4 class="text-white">Contact</h4>
	              <ul class="list-unstyled">
	                <li><a href="#" class="text-white">Follow on Twitter</a></li>
	                <li><a href="#" class="text-white">Like on Facebook</a></li>
	                <li><a href="#" class="text-white">Email me</a></li>
	              </ul>
	            </div>
	          </div>
	        </div>
	      </div>
	      <div class="navbar navbar-dark bg-dark box-shadow">
	        <div class="container d-flex justify-content-between">
	          <a href="http://localhost:8080/farmacii/index.html" class="navbar-brand d-flex align-items-center">
				<img src="database.png" alt="Database Icon"  class="mr-2">
	            <strong>FARMACII DATABASE</strong>
	          </a>
	          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarHeader" aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
	            <span class="navbar-toggler-icon"></span>
	          </button>
	        </div>
	      </div>
	    </header>
    <%
            FarmaciiDaoImpl farmacieDaoImpl = new FarmaciiDaoImpl();
            List<Farmacii> listaFarmacii = new ArrayList();
            listaFarmacii = farmacieDaoImpl.afiseazaFarmacii();
            request.setAttribute("listaFarmacii", listaFarmacii);

        %>
   <h1 class="text-center">TABELA FARMACII</h1>
    <br>
    
    <div class="container">

        <div class="row">
            <div class="col-md-12">
                    <div class="text">
                    	<a href="index.html" class="btn btn-secondary"><b>Home</b></a>
                    </div>
                    <table class="table table-hover">
                        <thead>
                        	<tr>
                <th scope="col">IdAngajat:</th> 
                <th scope="col">nume:</th> 
                <th scope="col">prenume:</th> 
                <th scope="col">data_nasterii:</th> 
                <th scope="col">adresa:</th> 
                <th scope="col">telefon:</th> 
                <th scope="col">functie:</th> 
                <th scope="col">salariu:</th> 
                <th scope="col">idFarmacie:</th> 
            </tr>
            						</thead>
                        <tbody>
            <c:forEach var="angajati" items="${listaAngajati}">
                <tr>
                    <td>${angajati.idAngajat}</td>
                    <td>${angajati.nume}</td>
                    <td>${angajati.prenume}</td>
<td><fmt:formatDate value="${angajati.data_nasterii}" pattern="yyyy-MM-dd" /></td>
                    <td>${angajati.adresa}</td>
                    <td>${angajati.telefon}</td>
                    <td>${angajati.functie}</td>
                    <td>${angajati.salariu}</td>
                    <td>${angajati.farmacii.idFarmacie}</td>


                </tr>
            </c:forEach>
        </table>
        <form action="AngajatiController" method="POST">
            <p align="center">
                Modifica: <input type="checkbox" id="update"> Sterge: <input type="checkbox" id="delete" onclick="document.getElementById('nume').disabled = this.checked;
                        document.getElementById('prenume').disabled = this.checked;
                        document.getElementById('data_nasterii').disabled = this.checked;
                        document.getElementById('adresa').disabled = this.checked;
                        document.getElementById('telefon').disabled = this.checked;
                        document.getElementById('functie').disabled = this.checked;
                        document.getElementById('salariu').disabled = this.checked;
                        document.getElementById('idFarmacie').disabled = this.checked;"><br><br>
				idAngajat:
                <select name="idAngajat">
                    <c:forEach items="${listaAngajati}" var="angajati">
                        <option value="${angajati.idAngajat}">${angajati.idAngajat}, ${angajati.nume}, ${angajati.prenume}</option>
                    </c:forEach>
                </select>
                <br><br>
                idFarmacie:
                <select name="idFarmacie">
                    <c:forEach items="${listaFarmacii}" var="farmacii">
                        <option value="${farmacii.idFarmacie}">${farmacii.idFarmacie}, ${farmacii.denumire}, ${farmacii.telefon}</option>
                    </c:forEach>
                </select>
                <br><br>
                Modifica nume: <input id="nume" type="text" name="nume"><br><br>
                Modifica prenume: <input id="prenume" type="text" name="prenume"> <br><br>
                Modifica data_nasterii: <input id="data_nasterii" type="text" name="data_nasterii"> <br><br>
                Modifica adresa: <input id="adresa" type="text" name="adresa"><br><br>
                Modifica telefon: <input id="telefon" type="text" name="telefon"> <br><br>
                Modifica functie: <input id="functie" type="text" name="functie"><br><br>
                Modifica salariu: <input id="salariu" type="text" name="telefon"> <br><br>
				Modifica idFarmacie: <input id="idFarmacie" type="text" name="idFarmacie"> <br><br>  
                <button type="submit" id="modificaAngajat" class="btn btn-primary " name="modificaAngajat"> Modifica</button> <br> <br>
                <button type="submit" id="stergeAngajat" class="btn btn-primary " name="stergeAngajat"> Sterge </button>
            </p>
        </form>
          

                    <br>
            </div>
        </div>

    </div>
    <footer class="text-muted">
      <div class="container">
        <p class="float-right">
          <a href="#">Back to top</a>
        </p>
      </div>
    </footer>

</body>
</html>