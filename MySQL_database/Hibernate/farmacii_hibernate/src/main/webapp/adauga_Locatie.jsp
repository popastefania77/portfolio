<%-- 
    Document   : adauga_Locatie
    Created on : Nov 22, 2016, 6:19:27 PM
    Author     : popas
--%>
<%@page import="DAOImpl.FarmaciiDaoImpl"%>
<%@page import="pojo.Farmacii"%>
<%@page import="java.util.ArrayList"%>
<%@page import="java.util.List"%>
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
    <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
    <title>Tabela Locatii</title>
    
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
	    <div class="d-flex justify-content-center align-items-center" style="min-height: 100vh;">
	    <div class="text-center">
    
<%
        FarmaciiDaoImpl farmacieDaoImpl = new FarmaciiDaoImpl();
        List<Farmacii> listaFarmacii = new ArrayList();
        listaFarmacii = farmacieDaoImpl.afiseazaFarmacii();
        request.setAttribute("listaFarmacii", listaFarmacii);
%>

        <div id="add">
            <h1> Adauga locatie </h1>
            <form action="LocatiiController" method="GET">
                <table>
                    <tr>
                        <td> numar Locatie: </td>
                        <td><input type="text" name="numar"></td>
                    </tr>
                    <tr>
                        <td> strada Locatie: </td>
                        <td><input type="text" name="strada"></td>
                    </tr>
                    <tr>
                        <td> oras Locatie: </td>
                        <td><input type="text" name="oras"></td>
                    </tr>
                    <tr>
                        <td> judet Locatie: </td>
                        <td><input type="text" name="judet"></td>
                    </tr>
                    <tr>
                        <td> Telefon Locatie: </td>
                        <td><input type="text" name="telefon"></td>
                    </tr>

                  </table>
                  
		                <br><br>
		                Farmacie:
		                <select name="idFarmacie">
		                    <c:forEach items="${listaFarmacii}" var="farmacii">
		                        <option value="${farmacii.idFarmacie}">${farmacii.idFarmacie}, ${farmacii.denumire}, ${farmacii.sediu}</option>
		                    </c:forEach>
		                </select>
	                	<br><br>

			<input type="submit" class="btn btn-primary" name="adaugaLocatie" value="Adauga locatie">

   
                
            </form>
        </div>

        <form action="LocatiiController" method="POST">
            <input type="submit" class="btn btn-secondary" name="afiseazaLocatii" value="Afiseaza locatii">
        	<a href="index.html" class="btn btn-secondary"><b>Home</b></a>
        </form>

    </body>
</html>
