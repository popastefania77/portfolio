<%-- 
    Document   : tabela_Locatii
    Created on : Nov 22, 2016, 6:20:29 PM
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
    <title>Tabela LOCATII</title>
            <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script>
            $(document).ready(function () {
                $("#stergeLocatie").hide();
                $("#modificaLocatie").hide();

                $("#update").click(function () {
                    $("#modificaLocatie").show();
                    $("#stergeLocatie").hide();
                });
                $("#delete").click(function () {
                    $("#stergeLocatie").show();
                    $("#modificaLocatie").hide();
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
    <h1 class="text-center">TABELA LOCATII</h1>
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
				                <th scope="col">IdLocatie:</th>
				                <th scope="col">numar:</th>
				                <th scope="col">strada:</th>
				                <th scope="col">oras:</th>
				                <th scope="col">judet:</th>
				                <th scope="col">telefon:</th>
				                <th scope="col">idFarmacie:</th>
				            </tr>
            <c:forEach var="locatii" items="${listaLocatii}">
                <tr>
                    <td>${locatii.idLocatie}</td>
                    <td>${locatii.numar}</td>
                    <td>${locatii.strada}</td>
                    <td>${locatii.oras}</td>
                    <td>${locatii.judet}</td>
                    <td>${locatii.telefon}</td>
                    <td>${locatii.farmacii.idFarmacie}</td>


                </tr>
            </c:forEach>
        </table>
        						</thead>

        <form action="LocatiiController" method="POST">
            <p align="center">
                Modifica: <input type="checkbox" id="update"> Sterge: <input type="checkbox" id="delete" onclick="document.getElementById('numar').disabled = this.checked;
                        document.getElementById('strada').disabled = this.checked;
                        document.getElementById('oras').disabled = this.checked;
                        document.getElementById('judet').disabled = this.checked;
                        document.getElementById('telefon').disabled = this.checked;
                        document.getElementById('idFarmacie').disabled = this.checked;"><br><br>
				idLocatie:
                <select name="idLocatie">
                    <c:forEach items="${listaLocatii}" var="locatii">
                        <option value="${locatii.idLocatie}">${locatii.idLocatie}</option>
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
                Modifica numar: <input id="numar" type="text" name="numar"><br><br>
                Modifica strada: <input id="strada" type="text" name="strada"> <br><br>
                Modifica oras: <input id="oras" type="text" name="oras"> <br><br>
                Modifica judet: <input id="judet" type="text" name="judet"><br><br>
                Modifica telefon: <input id="telefon" type="text" name="telefon"> <br><br>
                Modifica idFarmacie: <input id="idFarmacie" type="text" name="idFarmacie"> <br><br>
                <button type="submit" id="modificaLocatie" class="btn btn-primary " name="modificaLocatie"> Modifica</button> <br> <br>
                <button type="submit" id="stergeLocatie" class="btn btn-primary " name="stergeLocatie"> Sterge </button>
            </p>
        </form>
      
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
