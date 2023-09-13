CREATE DATABASE  IF NOT EXISTS `farmacii` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `farmacii`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: farmacii
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `angajati`
--

DROP TABLE IF EXISTS `angajati`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `angajati` (
  `idAngajat` int NOT NULL AUTO_INCREMENT,
  `nume` varchar(10) DEFAULT NULL,
  `prenume` varchar(10) DEFAULT NULL,
  `data_nasterii` date DEFAULT NULL,
  `adresa` varchar(45) DEFAULT NULL,
  `telefon` varchar(10) DEFAULT NULL,
  `functie` varchar(20) DEFAULT NULL,
  `salariu` float DEFAULT NULL,
  `idFarmacie` int DEFAULT NULL,
  PRIMARY KEY (`idAngajat`),
  KEY `idFarmacie` (`idFarmacie`),
  CONSTRAINT `angajati_ibfk_1` FOREIGN KEY (`idFarmacie`) REFERENCES `farmacii` (`idFarmacie`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `angajati`
--

LOCK TABLES `angajati` WRITE;
/*!40000 ALTER TABLE `angajati` DISABLE KEYS */;
INSERT INTO `angajati` VALUES (1,'Popescu','Elena','1985-05-17','Bucuresti','0756231458','Manager de Farmacie',5000,1),(2,'Marinescu','Ion','1990-10-12','Bucuresti','0778563215','Farmacist',4000,1),(45,'test','test','2020-12-12','test','test','test',5200,22);
/*!40000 ALTER TABLE `angajati` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `farmacii`
--

DROP TABLE IF EXISTS `farmacii`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farmacii` (
  `idFarmacie` int NOT NULL AUTO_INCREMENT,
  `denumire` varchar(10) DEFAULT NULL,
  `telefon` varchar(10) DEFAULT NULL,
  `sediu` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`idFarmacie`),
  UNIQUE KEY `denumire` (`denumire`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farmacii`
--

LOCK TABLES `farmacii` WRITE;
/*!40000 ALTER TABLE `farmacii` DISABLE KEYS */;
INSERT INTO `farmacii` VALUES (1,'Catena','0725252327','Bucuresti'),(2,'HelpNet','0728972326','Bucuresti'),(3,'DrMax','0756478921','Bucuresti'),(7,'test','test','tes'),(14,'Farmaline','0774521597','Bucuresti'),(15,'SENSIBLU','0773331597','SINAIA'),(20,'abc','test','dada'),(22,'farmacie','test','dada');
/*!40000 ALTER TABLE `farmacii` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locatii`
--

DROP TABLE IF EXISTS `locatii`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locatii` (
  `idLocatie` int NOT NULL AUTO_INCREMENT,
  `numar` varchar(5) DEFAULT NULL,
  `strada` varchar(20) DEFAULT NULL,
  `oras` varchar(10) DEFAULT NULL,
  `judet` varchar(10) DEFAULT NULL,
  `telefon` varchar(10) DEFAULT NULL,
  `idFarmacie` int DEFAULT NULL,
  PRIMARY KEY (`idLocatie`),
  KEY `idFarmacie` (`idFarmacie`),
  CONSTRAINT `locatii_ibfk_1` FOREIGN KEY (`idFarmacie`) REFERENCES `farmacii` (`idFarmacie`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locatii`
--

LOCK TABLES `locatii` WRITE;
/*!40000 ALTER TABLE `locatii` DISABLE KEYS */;
INSERT INTO `locatii` VALUES (2,'','','','','',1),(3,'103','Mihai Eminescu','Targoviste','Dambovita','0756987256',1),(4,'245','George Enescu','Sinaia','Prahova','0753148967',1),(7,'12','George Enescu','Targoviste','dambovita','0734567899',3),(8,'562','Theodor Pallady','București','Bucuresti','0734564782',2),(9,'21','Unirii','Ploiesti','Prahova','0734512532',7),(11,'34','Virtutii','Comarnic','Prahova','0774521597',1),(12,'24','Luminii','Brasov','Brasov','0725252456',14);
/*!40000 ALTER TABLE `locatii` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-29  7:06:18
