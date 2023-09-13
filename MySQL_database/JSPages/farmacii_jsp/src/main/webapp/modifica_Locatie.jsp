<%-- 
    Document   : modifica_Angajat
    Created on : Nov 14, 2016, 1:36:40 PM
    Author     : popas
--%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page language="java" import="java.lang.*,java.math.*,db.*,java.sql.*, java.io.*, java.util.*"%>
<!DOCTYPE html>
<html>
<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="/docs/4.0/assets/img/favicons/favicon.ico">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Tabela Locatii</title>
    
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
    <h1 class="text-center">MODIFICA TABELA LOCATII</h1>
    <br>

    <div class="container">

        <div class="row">
            <div class="col-md-12">
                <form action="" method="post">
                    <div class="text">
                    	<a href="index.html" class="btn btn-secondary"><b>Home</b></a>
                        <input type="submit" class="btn btn-primary " value="Adauga o noua locatie" formaction="nou_Locatie.jsp">
                        <input type="submit" class="btn btn-primary " value="Modifica linia marcata" formaction="m1_Locatie.jsp">
                        <input type="submit" class="btn btn-primary " value="Sterge liniile marcate" formaction="sterge_Locatie.jsp">
                    	
                    </div>
                    <table class="table table-hover">
                        <thead>
                        	<tr>
                        		<th scope="col">Mark</th>
 								<th scope="col">IdLocatie</th>
                                <th scope="col">Numar</th>
                                <th scope="col">Strada</th>
                                <th scope="col">Oras</th>
                                <th scope="col">Judet</th>
                                <th scope="col">Telefon</th>
                                <th scope="col">Farmacie</th>
                </tr>
                        </thead>
                        <tbody>
                <%
                    jb.connect();
                    ResultSet rs = jb.vedeTabela("locatii");
                    while (rs.next()){

                %>
                <tr>
                    <td><input type="checkbox" name="primarykey" value="<%= rs.getInt("idLocatie") %>"></td>
                    <td><%= rs.getString("idLocatie")%></td>
                    <td><%= rs.getString("numar")%></td>
                    <td><%= rs.getString("strada")%></td>
                    <td><%= rs.getString("oras")%></td>
					<td><%= rs.getString("judet")%></td>
					<td><%= rs.getString("telefon")%></td>
					<td><%= rs.getString("idFarmacie")%></td>
</tr>
                            <%
                                }
                                rs.close();
                                jb.disconnect();
                            %>
                        </tbody>
                    </table>
                    <br>
                </form>
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
