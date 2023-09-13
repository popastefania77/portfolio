<%-- 
    Document   : m1_Farmacie
    Created on : Nov 14, 2016, 1:39:35 PM
    Author     : popas
--%>

<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page language="java" import="java.lang.*,java.math.*,db.*,java.sql.*, java.io.*, java.util.*"%>
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
    
    <link href="https://getbootstrap.com/docs/4.0/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <!-- Link to Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link href="farmacii.css" rel="stylesheet">
    <script src="bootstrap-scripts.js"></script>
</head>
<jsp:useBean id="jb" scope="session" class="db.JavaBean" />
<jsp:setProperty name="jb" property="*" />
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
        String[] s = request.getParameterValues("primarykey");
		if (s == null){
		%>
            <p class="text-danger" style="font-size: 24px;">Nu ați selectat nicio linie!</p>         
    	<%
        } else if (s.length > 1) {
        %>
            <p class="text-danger" style="font-size: 24px;">Ați selectat prea multe linii. Selectati doar una!</p> 
    	<%
        } else {
        	%>
        <h1 align="center">Tabela Farmacii</h1>
        <%
            jb.connect();
            int aux = java.lang.Integer.parseInt(request.getParameter("primarykey"));
            ResultSet rs = jb.intoarceLinieDupaId("farmacii", "idFarmacie", aux);
            rs.first();
            String Denumire = rs.getString("Denumire");
            String Telefon = rs.getString("Telefon");
            String Sediu = rs.getString("Sediu");
            rs.close();
            jb.disconnect();
        %>
        <form action="m2_Farmacie.jsp" method="post">
            <table>
                <tr>
                    <td align="right">IdFarmacie:</td>
                    <td> <input type="text" name="idFarmacie" size="30" value="<%= aux%>" readonly/></td>
                </tr>
                <tr>
                    <td align="right">Denumire:</td>
                    <td> <input type="text" name="Denumire" size="30" value="<%= Denumire%>"/></td>
                </tr>
                <tr>
                    <td align="right">Telefon:</td>
                    <td> <input type="text" name="Telefon" size="30" value="<%= Telefon%>"/></td>
                </tr>
                <tr>
                    <td align="right">Sediu:</td>
                    <td> <input type="text" name="Sediu" size="30" value="<%= Sediu%>"/></td>
                </tr>
            </table>
            <br>
                <input type="submit" class="btn btn-primary "  value="Modifica linia">
        </form>
        <%
      }
         %>

	            	<a href="http://localhost:8080/farmacii/modifica_Farmacie.jsp" class="btn btn-secondary"><b>MODIFICA TABELA FARMACII</b></a>
	            	<a href="index.html" class="btn btn-secondary"><b>Home</b></a>
	</div>
	</div>
    </body>
</html>