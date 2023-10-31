CREATE DATABASE  IF NOT EXISTS `faceattendace` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `faceattendace`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: faceattendace
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `diem_danh`
--

DROP TABLE IF EXISTS `diem_danh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `diem_danh` (
  `MSSV` varchar(10) NOT NULL,
  PRIMARY KEY (`MSSV`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diem_danh`
--

LOCK TABLES `diem_danh` WRITE;
/*!40000 ALTER TABLE `diem_danh` DISABLE KEYS */;
INSERT INTO `diem_danh` VALUES ('0'),('1'),('10'),('100'),('11'),('12'),('13'),('14'),('15'),('16'),('17'),('18'),('19'),('2'),('20'),('21'),('2111818'),('2111846'),('2111863'),('2112727'),('2115208'),('22'),('23'),('24'),('25'),('26'),('27'),('28'),('29'),('3'),('30'),('31'),('32'),('33'),('34'),('35'),('36'),('37'),('38'),('39'),('4'),('40'),('41'),('42'),('43'),('44'),('45'),('46'),('47'),('48'),('49'),('5'),('50'),('51'),('52'),('53'),('54'),('55'),('56'),('57'),('58'),('59'),('6'),('60'),('61'),('62'),('63'),('64'),('65'),('66'),('67'),('68'),('69'),('7'),('70'),('71'),('72'),('73'),('74'),('75'),('76'),('77'),('78'),('79'),('8'),('80'),('81'),('82'),('83'),('84'),('85'),('86'),('87'),('88'),('89'),('9'),('90'),('91'),('92'),('93'),('94'),('95'),('96'),('97'),('98'),('99');
/*!40000 ALTER TABLE `diem_danh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `thong_tin_sv`
--

DROP TABLE IF EXISTS `thong_tin_sv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `thong_tin_sv` (
  `MSSV` varchar(10) NOT NULL,
  `Ho` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Ten` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `LinkAnh` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`MSSV`),
  UNIQUE KEY `LinkAnh_UNIQUE` (`LinkAnh`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `thong_tin_sv`
--

LOCK TABLES `thong_tin_sv` WRITE;
/*!40000 ALTER TABLE `thong_tin_sv` DISABLE KEYS */;
INSERT INTO `thong_tin_sv` VALUES ('1','Họ 1','Tên 1','1.png'),('10','Họ 10','Tên 10','10.png'),('100','Họ 100','Tên 100','100.png'),('11','Họ 11','Tên 11','11.png'),('12','Họ 12','Tên 12','12.png'),('13','Họ 13','Tên 13','13.png'),('14','Họ 14','Tên 14','14.png'),('15','Họ 15','Tên 15','15.png'),('16','Họ 16','Tên 16','16.png'),('17','Họ 17','Tên 17','17.png'),('18','Họ 18','Tên 18','18.png'),('19','Họ 19','Tên 19','19.png'),('2','Họ 2','Tên 2','2.png'),('20','Họ 20','Tên 20','20.png'),('21','Họ 21','Tên 21','21.png'),,('22','Họ 22','Tên 22','22.png'),('23','Họ 23','Tên 23','23.png'),('24','Họ 24','Tên 24','24.png'),('25','Họ 25','Tên 25','25.png'),('26','Họ 26','Tên 26','26.png'),('27','Họ 27','Tên 27','27.png'),('28','Họ 28','Tên 28','28.png'),('29','Họ 29','Tên 29','29.png'),('3','Họ 3','Tên 3','3.png'),('30','Họ 30','Tên 30','30.png'),('31','Họ 31','Tên 31','31.png'),('32','Họ 32','Tên 32','32.png'),('33','Họ 33','Tên 33','33.png'),('34','Họ 34','Tên 34','34.png'),('35','Họ 35','Tên 35','35.png'),('36','Họ 36','Tên 36','36.png'),('37','Họ 37','Tên 37','37.png'),('38','Họ 38','Tên 38','38.png'),('39','Họ 39','Tên 39','39.png'),('4','Họ 4','Tên 4','4.png'),('40','Họ 40','Tên 40','40.png'),('41','Họ 41','Tên 41','41.png'),('42','Họ 42','Tên 42','42.png'),('43','Họ 43','Tên 43','43.png'),('44','Họ 44','Tên 44','44.png'),('45','Họ 45','Tên 45','45.png'),('46','Họ 46','Tên 46','46.png'),('47','Họ 47','Tên 47','47.png'),('48','Họ 48','Tên 48','48.png'),('49','Họ 49','Tên 49','49.png'),('5','Họ 5','Tên 5','5.png'),('50','Họ 50','Tên 50','50.png'),('51','Họ 51','Tên 51','51.png'),('52','Họ 52','Tên 52','52.png'),('53','Họ 53','Tên 53','53.png'),('54','Họ 54','Tên 54','54.png'),('55','Họ 55','Tên 55','55.png'),('56','Họ 56','Tên 56','56.png'),('57','Họ 57','Tên 57','57.png'),('58','Họ 58','Tên 58','58.png'),('59','Họ 59','Tên 59','59.png'),('6','Họ 6','Tên 6','6.png'),('60','Họ 60','Tên 60','60.png'),('61','Họ 61','Tên 61','61.png'),('62','Họ 62','Tên 62','62.png'),('63','Họ 63','Tên 63','63.png'),('64','Họ 64','Tên 64','64.png'),('65','Họ 65','Tên 65','65.png'),('66','Họ 66','Tên 66','66.png'),('67','Họ 67','Tên 67','67.png'),('68','Họ 68','Tên 68','68.png'),('69','Họ 69','Tên 69','69.png'),('7','Họ 7','Tên 7','7.png'),('70','Họ 70','Tên 70','70.png'),('71','Họ 71','Tên 71','71.png'),('72','Họ 72','Tên 72','72.png'),('73','Họ 73','Tên 73','73.png'),('74','Họ 74','Tên 74','74.png'),('75','Họ 75','Tên 75','75.png'),('76','Họ 76','Tên 76','76.png'),('77','Họ 77','Tên 77','77.png'),('78','Họ 78','Tên 78','78.png'),('79','Họ 79','Tên 79','79.png'),('8','Họ 8','Tên 8','8.png'),('80','Họ 80','Tên 80','80.png'),('81','Họ 81','Tên 81','81.png'),('82','Họ 82','Tên 82','82.png'),('83','Họ 83','Tên 83','83.png'),('84','Họ 84','Tên 84','84.png'),('85','Họ 85','Tên 85','85.png'),('86','Họ 86','Tên 86','86.png'),('87','Họ 87','Tên 87','87.png'),('88','Họ 88','Tên 88','88.png'),('89','Họ 89','Tên 89','89.png'),('9','Họ 9','Tên 9','9.png'),('90','Họ 90','Tên 90','90.png'),('91','Họ 91','Tên 91','91.png'),('92','Họ 92','Tên 92','92.png'),('93','Họ 93','Tên 93','93.png'),('94','Họ 94','Tên 94','94.png'),('95','Họ 95','Tên 95','95.png'),('96','Họ 96','Tên 96','96.png'),('97','Họ 97','Tên 97','97.png'),('98','Họ 98','Tên 98','98.png'),('99','Họ 99','Tên 99','99.png');
/*!40000 ALTER TABLE `thong_tin_sv` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-31 19:35:06
