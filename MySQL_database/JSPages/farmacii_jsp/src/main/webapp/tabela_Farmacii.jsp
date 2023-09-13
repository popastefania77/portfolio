<%-- 
    Document   : tabela_Farmacii
    Created on : Nov 14, 2016, 1:03:20 PM
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
    <title>Tabela FARMACII</title>
    
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
								<th scope="col">IdFarmacie</th>
                                <th scope="col">Denumire</th>
                                <th scope="col">Telefon</th>
                                <th scope="col">Sediu</th>                

                			</tr>
						</thead>
                        <tbody>
			                <%
			                    jb.connect();
			                    ResultSet rs = jb.vedeTabela("farmacii");
			                    while (rs.next()) {
			                %>
			                <tr>
			                    <td><%= rs.getString("idFarmacie")%></td>			                
			                    <td><%= rs.getString("denumire")%></td>
			                    <td><%= rs.getString("telefon")%></td>
			                    <td><%= rs.getString("sediu")%></td>
			                </tr>
			                    <%
			                        }
			                    	rs.close();
			                    	jb.disconnect();
			                    %>
                        </tbody>
                    </table>
                    <br>
            </div>
        </div>

    </div>
    <footer class="text-muted">
      <div class="container">
        <p class="float-right">
          <a href="">Back to top</a>
        </p>
      </div>
    </footer>

</body>
</html>
