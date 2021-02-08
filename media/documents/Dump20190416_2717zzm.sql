CREATE DATABASE  IF NOT EXISTS `iscmdb1` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `iscmdb1`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: iscmdb1
-- ------------------------------------------------------
-- Server version	5.7.22-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account_access`
--

DROP TABLE IF EXISTS `account_access`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_access` (
  `accessid` varchar(5) NOT NULL,
  `accname` varchar(25) NOT NULL,
  `accdescription` varchar(100) NOT NULL,
  `created` datetime(6) NOT NULL,
  `createdby` varchar(20) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `updatedby` varchar(20) NOT NULL,
  PRIMARY KEY (`accessid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_access`
--

LOCK TABLES `account_access` WRITE;
/*!40000 ALTER TABLE `account_access` DISABLE KEYS */;
INSERT INTO `account_access` VALUES ('1','Commercial','Payment','2019-04-04 13:04:05.428127','','2019-04-04 13:04:05.428199',''),('2','HR','Human Resource','2019-04-04 13:04:37.163057','','2019-04-04 13:04:37.163185',''),('3','BA','Business Associate','2019-04-04 13:05:03.497393','','2019-04-04 13:05:03.497462',''),('4','MLLUSER','MllUser','2019-04-04 13:05:54.796345','','2019-04-04 13:05:54.796594',''),('5','MLLManager','Manager','2019-04-04 13:06:16.886171','','2019-04-04 13:06:16.886387',''),('6','SrManager','Senior Manager','2019-04-04 13:06:33.758926','','2019-04-04 13:06:33.759057','');
/*!40000 ALTER TABLE `account_access` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_ba`
--

DROP TABLE IF EXISTS `account_ba`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_ba` (
  `baid` varchar(10) NOT NULL,
  `bacode` varchar(5) NOT NULL,
  `baname` varchar(30) NOT NULL,
  `bacontactname` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `mobileno` varchar(15) NOT NULL,
  `status` varchar(50) NOT NULL,
  `created` datetime(6) NOT NULL,
  `createdby` varchar(20) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `updatedby` varchar(20) NOT NULL,
  PRIMARY KEY (`baid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_ba`
--

LOCK TABLES `account_ba` WRITE;
/*!40000 ALTER TABLE `account_ba` DISABLE KEYS */;
INSERT INTO `account_ba` VALUES ('1','BA1','','ba1Name','ba2@gmail.com','','1','2019-04-04 13:18:45.809576','','2019-04-04 13:18:45.809656',''),('2','BA2','','ba2Name','ba2@gmail.com','','1','2019-04-04 13:19:08.184414','','2019-04-04 13:19:08.184475',''),('3','BA3','','ba3Name','ba3@gmail.com','','1','2019-04-04 13:19:24.645031','','2019-04-04 13:19:24.645138',''),('4','BA4','','ba4Name','ba4@gmail.com','','1','2019-04-04 13:19:46.692406','','2019-04-04 13:19:46.692548',''),('5','BA5','','ba5Name','ba5@gmail.com','','1','2019-04-04 13:20:05.882089','','2019-04-04 13:20:05.882202','');
/*!40000 ALTER TABLE `account_ba` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_customer`
--

DROP TABLE IF EXISTS `account_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_customer` (
  `custid` varchar(10) NOT NULL,
  `custcode` varchar(5) NOT NULL,
  `custname` varchar(30) NOT NULL,
  `custcontactname` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `mobileno` varchar(15) NOT NULL,
  `status` varchar(50) NOT NULL,
  `created` datetime(6) NOT NULL,
  `createdby` varchar(20) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `updatedby` varchar(20) NOT NULL,
  PRIMARY KEY (`custid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_customer`
--

LOCK TABLES `account_customer` WRITE;
/*!40000 ALTER TABLE `account_customer` DISABLE KEYS */;
INSERT INTO `account_customer` VALUES ('1','AMZ','','Amazon Employee','at8286997248@gmail.com','','1','2019-04-04 13:08:31.002992','','2019-04-04 13:08:31.003074',''),('2','FLP','','Flipkart Employee','flipkart@gmail.com','','1','2019-04-04 13:08:59.612747','','2019-04-04 13:08:59.612811',''),('3','SWG','','Swiggy Employee','swiggy@gmail.com','','1','2019-04-04 13:09:34.248230','','2019-04-04 13:09:34.248396',''),('4','ZMT','','Zomato Employee','zomato@gmail.com','','1','2019-04-04 13:10:57.081155','','2019-04-04 13:10:57.081220',''),('5','UBE','','UberEats Employee','ubereats@gmail.com','','1','2019-04-04 13:11:30.753285','','2019-04-04 13:11:30.753354','');
/*!40000 ALTER TABLE `account_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_user`
--

DROP TABLE IF EXISTS `account_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_user` (
  `userid` varchar(15) NOT NULL,
  `firstname` varchar(15) NOT NULL,
  `lastname` varchar(15) NOT NULL,
  `mobileno` varchar(10) NOT NULL,
  `worklocation` varchar(20) NOT NULL,
  `status` varchar(5) NOT NULL,
  `version` varchar(10) NOT NULL,
  `password` varchar(15) NOT NULL,
  `created` datetime(6) NOT NULL,
  `createdby` varchar(20) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `updatedby` varchar(20) NOT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_user`
--

LOCK TABLES `account_user` WRITE;
/*!40000 ALTER TABLE `account_user` DISABLE KEYS */;
INSERT INTO `account_user` VALUES ('1','Deepak','Singh','90043','MUMBAI','','','123456','2019-04-04 12:59:20.249044','','2019-04-04 12:59:20.249208',''),('2','Sandeep','Chourey','5364789234','Indore','','','123456','2019-04-04 12:59:57.498833','','2019-04-04 12:59:57.498898',''),('3','Rahul','Divaker','23989242','Mulund','','','123456','2019-04-04 13:00:29.346595','','2019-04-04 13:00:29.346667',''),('4','Pravin','Singh','9472973492','Virar','','','123456','2019-04-04 13:01:27.289327','','2019-04-04 13:01:27.289393',''),('5','Mansi','Sawant','739274726','Dadar','','','123456','2019-04-04 13:03:28.052830','','2019-04-04 13:03:28.052922','');
/*!40000 ALTER TABLE `account_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_useraccess`
--

DROP TABLE IF EXISTS `account_useraccess`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_useraccess` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `createdby` varchar(20) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `updatedby` varchar(20) NOT NULL,
  `access_id` varchar(5) NOT NULL,
  `location_id` int(11) NOT NULL,
  `user_id` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_useraccess_access_id_ef308931_fk_account_access_accessid` (`access_id`),
  KEY `account_useraccess_location_id_9f536cd3_fk_location_` (`location_id`),
  KEY `account_useraccess_user_id_abb729d3_fk_account_user_userid` (`user_id`),
  CONSTRAINT `account_useraccess_access_id_ef308931_fk_account_access_accessid` FOREIGN KEY (`access_id`) REFERENCES `account_access` (`accessid`),
  CONSTRAINT `account_useraccess_location_id_9f536cd3_fk_location_` FOREIGN KEY (`location_id`) REFERENCES `location_operationlocation` (`oplocationid`),
  CONSTRAINT `account_useraccess_user_id_abb729d3_fk_account_user_userid` FOREIGN KEY (`user_id`) REFERENCES `account_user` (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_useraccess`
--

LOCK TABLES `account_useraccess` WRITE;
/*!40000 ALTER TABLE `account_useraccess` DISABLE KEYS */;
INSERT INTO `account_useraccess` VALUES (1,'2019-04-04 13:32:00.500502','','2019-04-04 13:32:00.500564','','1',1,'1'),(2,'2019-04-04 13:32:13.919105','','2019-04-04 13:32:13.919285','','2',1,'2'),(3,'2019-04-04 13:32:25.161928','','2019-04-04 13:32:25.162113','','5',1,'3'),(4,'2019-04-04 13:32:35.036868','','2019-04-04 13:32:35.036951','','6',1,'4');
/*!40000 ALTER TABLE `account_useraccess` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_userlocationcustomer`
--

DROP TABLE IF EXISTS `account_userlocationcustomer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_userlocationcustomer` (
  `ulcpkey` varchar(10) NOT NULL,
  `created` datetime(6) NOT NULL,
  `createdby` varchar(20) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `updatedby` varchar(20) NOT NULL,
  `customer_id` varchar(10) NOT NULL,
  `location_id` int(11) NOT NULL,
  `user_id` varchar(15) NOT NULL,
  PRIMARY KEY (`ulcpkey`),
  KEY `account_userlocation_customer_id_3f3acbe1_fk_account_c` (`customer_id`),
  KEY `account_userlocation_location_id_0f4fa417_fk_location_` (`location_id`),
  KEY `account_userlocation_user_id_71635d45_fk_account_u` (`user_id`),
  CONSTRAINT `account_userlocation_customer_id_3f3acbe1_fk_account_c` FOREIGN KEY (`customer_id`) REFERENCES `account_customer` (`custid`),
  CONSTRAINT `account_userlocation_location_id_0f4fa417_fk_location_` FOREIGN KEY (`location_id`) REFERENCES `location_operationlocation` (`oplocationid`),
  CONSTRAINT `account_userlocation_user_id_71635d45_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_user` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_userlocationcustomer`
--

LOCK TABLES `account_userlocationcustomer` WRITE;
/*!40000 ALTER TABLE `account_userlocationcustomer` DISABLE KEYS */;
INSERT INTO `account_userlocationcustomer` VALUES ('1','2019-04-04 13:35:26.397595','','2019-04-04 13:35:26.397678','','1',1,'1'),('2','2019-04-04 13:36:10.589249','','2019-04-04 13:36:10.589308','','2',1,'1'),('3','2019-04-04 13:36:20.712900','','2019-04-04 13:36:20.713004','','3',1,'1'),('4','2019-04-04 13:36:51.136178','','2019-04-04 13:36:51.136229','','1',5,'1'),('5','2019-04-04 13:37:02.376393','','2019-04-04 13:37:02.376494','','1',6,'1'),('6','2019-04-04 13:37:30.984930','','2019-04-04 13:37:30.985009','','1',4,'1');
/*!40000 ALTER TABLE `account_userlocationcustomer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add city',7,'add_city'),(26,'Can change city',7,'change_city'),(27,'Can delete city',7,'delete_city'),(28,'Can view city',7,'view_city'),(29,'Can add operation location',8,'add_operationlocation'),(30,'Can change operation location',8,'change_operationlocation'),(31,'Can delete operation location',8,'delete_operationlocation'),(32,'Can view operation location',8,'view_operationlocation'),(33,'Can add state',9,'add_state'),(34,'Can change state',9,'change_state'),(35,'Can delete state',9,'delete_state'),(36,'Can view state',9,'view_state'),(37,'Can add access',10,'add_access'),(38,'Can change access',10,'change_access'),(39,'Can delete access',10,'delete_access'),(40,'Can view access',10,'view_access'),(41,'Can add customer',11,'add_customer'),(42,'Can change customer',11,'change_customer'),(43,'Can delete customer',11,'delete_customer'),(44,'Can view customer',11,'view_customer'),(45,'Can add user',12,'add_user'),(46,'Can change user',12,'change_user'),(47,'Can delete user',12,'delete_user'),(48,'Can view user',12,'view_user'),(49,'Can add user access',13,'add_useraccess'),(50,'Can change user access',13,'change_useraccess'),(51,'Can delete user access',13,'delete_useraccess'),(52,'Can view user access',13,'view_useraccess'),(53,'Can add user location customer',14,'add_userlocationcustomer'),(54,'Can change user location customer',14,'change_userlocationcustomer'),(55,'Can delete user location customer',14,'delete_userlocationcustomer'),(56,'Can view user location customer',14,'view_userlocationcustomer'),(57,'Can add ba',15,'add_ba'),(58,'Can change ba',15,'change_ba'),(59,'Can delete ba',15,'delete_ba'),(60,'Can view ba',15,'view_ba'),(61,'Can add contract',16,'add_contract'),(62,'Can change contract',16,'change_contract'),(63,'Can delete contract',16,'delete_contract'),(64,'Can view contract',16,'view_contract'),(65,'Can add contract detail',17,'add_contractdetail'),(66,'Can change contract detail',17,'change_contractdetail'),(67,'Can delete contract detail',17,'delete_contractdetail'),(68,'Can view contract detail',17,'view_contractdetail'),(69,'Can add contract type',18,'add_contracttype'),(70,'Can change contract type',18,'change_contracttype'),(71,'Can delete contract type',18,'delete_contracttype'),(72,'Can view contract type',18,'view_contracttype'),(73,'Can add document',19,'add_document'),(74,'Can change document',19,'change_document'),(75,'Can delete document',19,'delete_document'),(76,'Can view document',19,'view_document'),(77,'Can add skill level',20,'add_skilllevel'),(78,'Can change skill level',20,'change_skilllevel'),(79,'Can delete skill level',20,'delete_skilllevel'),(80,'Can view skill level',20,'view_skilllevel'),(81,'Can add rate type',21,'add_ratetype'),(82,'Can change rate type',21,'change_ratetype'),(83,'Can delete rate type',21,'delete_ratetype'),(84,'Can view rate type',21,'view_ratetype'),(85,'Can add detail att capture',22,'add_detailattcapture'),(86,'Can change detail att capture',22,'change_detailattcapture'),(87,'Can delete detail att capture',22,'delete_detailattcapture'),(88,'Can view detail att capture',22,'view_detailattcapture');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contract_contract`
--

DROP TABLE IF EXISTS `contract_contract`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contract_contract` (
  `contractid` int(11) NOT NULL,
  `contractwith` varchar(5) NOT NULL,
  `cost` double NOT NULL,
  `oppourtunityid` varchar(20) DEFAULT NULL,
  `vertical` int(11) NOT NULL,
  `bonus` int(11) NOT NULL,
  `bonusduration` varchar(10) NOT NULL,
  `startdate` date NOT NULL,
  `enddate` date NOT NULL,
  `closedate` date NOT NULL,
  `extenddate` date NOT NULL,
  `approvedby` varchar(45) NOT NULL,
  `approvestatus` smallint(6) NOT NULL,
  `remark` varchar(200) NOT NULL,
  `created` datetime(6) NOT NULL,
  `createdby` varchar(20) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `updatedby` varchar(20) NOT NULL,
  `contracttype_id` int(11) NOT NULL,
  `locationcust_id` varchar(10) NOT NULL,
  `relatedcontract_id` int(11) DEFAULT NULL,
  `ba_id` varchar(10) DEFAULT NULL,
  `customer_id` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`contractid`),
  KEY `contract_contract_contracttype_id_15a3c7e3_fk_contract_` (`contracttype_id`),
  KEY `contract_contract_locationcust_id_6fb1a3a9_fk_account_u` (`locationcust_id`),
  KEY `contract_contract_relatedcontract_id_b1d9d0e6_fk_contract_` (`relatedcontract_id`),
  KEY `contract_contract_customer_id_01e9b7ca_fk_account_c` (`customer_id`),
  KEY `contract_contract_ba_id_680ba38e_fk_account_ba_baid` (`ba_id`),
  CONSTRAINT `contract_contract_ba_id_680ba38e_fk_account_ba_baid` FOREIGN KEY (`ba_id`) REFERENCES `account_ba` (`baid`),
  CONSTRAINT `contract_contract_contracttype_id_15a3c7e3_fk_contract_` FOREIGN KEY (`contracttype_id`) REFERENCES `contract_contracttype` (`contracttypeid`),
  CONSTRAINT `contract_contract_customer_id_01e9b7ca_fk_account_c` FOREIGN KEY (`customer_id`) REFERENCES `account_customer` (`custid`),
  CONSTRAINT `contract_contract_locationcust_id_6fb1a3a9_fk_account_u` FOREIGN KEY (`locationcust_id`) REFERENCES `account_userlocationcustomer` (`ulcpkey`),
  CONSTRAINT `contract_contract_relatedcontract_id_b1d9d0e6_fk_contract_` FOREIGN KEY (`relatedcontract_id`) REFERENCES `contract_contract` (`contractid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contract_contract`
--

LOCK TABLES `contract_contract` WRITE;
/*!40000 ALTER TABLE `contract_contract` DISABLE KEYS */;
INSERT INTO `contract_contract` VALUES (1,'0',8000000,'1',7,50000,'month','2019-01-01','2019-09-30','2019-03-23','2019-11-30','Deepak Singh',1,'Contract 1','2019-04-04 15:52:06.128620','','2019-04-05 08:28:33.110849','',1,'1',NULL,NULL,'1'),(2,'0',7000000,'1',7,50000,'month','2019-01-01','2019-09-30','2019-03-23','2019-11-30','Deepak Singh',1,'BA Contract 1','2019-04-04 15:53:09.635117','','2019-04-05 08:29:12.791122','',1,'1',1,'1',NULL),(3,'0',10000000,'2',7,100000,'month','2019-03-01','2019-04-04','2019-03-23','2019-11-30','Deepak Singh',1,'Customer Contract 3','2019-04-04 15:56:25.247365','','2019-04-04 15:56:25.247411','',2,'2',NULL,NULL,NULL),(4,'1',8000000,'2',7,100000,'month','2019-03-01','2019-04-04','2019-03-23','2019-11-30','Deepak Singh',1,'Customer Contract 3','2019-04-04 15:57:17.572229','','2019-04-04 15:57:17.572261','',2,'2',3,NULL,NULL),(5,'0',7999985,'3',7,100000,'month','2019-02-01','2019-08-31','2019-06-30','2019-12-31','Deepak Singh',1,'Customer Contract 5','2019-04-04 16:00:01.100269','','2019-04-04 16:00:01.100316','',3,'3',NULL,NULL,NULL),(12,'0',2000,'3214245245',2,23000,'quarter','2019-04-16','2019-04-16','2015-01-01','2015-01-01','NA',0,'Remarks','2019-04-16 05:51:38.212299','','2019-04-16 05:51:38.212299','',2,'5',NULL,NULL,'1'),(66,'0',455555,'77',66,45666,'month','2019-12-29','2017-10-30','2015-01-01','2015-01-01','sdgugj',77,'hkhfkhs','2019-04-16 05:50:38.496146','','2019-04-16 05:50:38.496146','',1,'1',NULL,NULL,'2');
/*!40000 ALTER TABLE `contract_contract` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contract_contractdetail`
--

DROP TABLE IF EXISTS `contract_contractdetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contract_contractdetail` (
  `contractdetid` int(11) NOT NULL,
  `requirequantity` int(11) NOT NULL,
  `startquantity` int(11) NOT NULL,
  `endquantity` int(11) NOT NULL,
  `uom` int(11) NOT NULL,
  `upperdev` double NOT NULL,
  `lowerdev` double NOT NULL,
  `ratetype_id` int(11) NOT NULL,
  `fixedcost` double NOT NULL,
  `margintype` varchar(5) NOT NULL,
  `marginvalue` double NOT NULL,
  `isapplicablecomrange` smallint(6) NOT NULL,
  `billingcycle` int(11) NOT NULL,
  `finalsubmissionflag` smallint(6) NOT NULL,
  `remark` varchar(200) NOT NULL,
  `created` datetime(6) NOT NULL,
  `createdby` varchar(20) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `updatedby` varchar(20) NOT NULL,
  `contacttype_id` int(11) NOT NULL,
  `contract_id` int(11) NOT NULL,
  `skilllevel_id` int(11) NOT NULL,
  PRIMARY KEY (`contractdetid`),
  KEY `contract_contractdet_contacttype_id_22f723fc_fk_contract_` (`contacttype_id`),
  KEY `contract_contractdet_contract_id_6d1b1bec_fk_contract_` (`contract_id`),
  KEY `contract_contractdet_skilllevel_id_65046bcb_fk_contract_` (`skilllevel_id`),
  KEY `contract_contractdetail_ratetype_id_0cc7166c` (`ratetype_id`),
  CONSTRAINT `contract_contractdet_contacttype_id_22f723fc_fk_contract_` FOREIGN KEY (`contacttype_id`) REFERENCES `contract_contracttype` (`contracttypeid`),
  CONSTRAINT `contract_contractdet_contract_id_6d1b1bec_fk_contract_` FOREIGN KEY (`contract_id`) REFERENCES `contract_contract` (`contractid`),
  CONSTRAINT `contract_contractdet_ratetype_id_0cc7166c_fk_contract_` FOREIGN KEY (`ratetype_id`) REFERENCES `contract_ratetype` (`ratetypeid`),
  CONSTRAINT `contract_contractdet_skilllevel_id_65046bcb_fk_contract_` FOREIGN KEY (`skilllevel_id`) REFERENCES `contract_skilllevel` (`skillid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contract_contractdetail`
--

LOCK TABLES `contract_contractdetail` WRITE;
/*!40000 ALTER TABLE `contract_contractdetail` DISABLE KEYS */;
INSERT INTO `contract_contractdetail` VALUES (1,10,0,0,10,0,0,1,100000,'0',0,1,0,0,'man power operation executive 10','2019-04-04 17:04:21.123156','','2019-04-04 17:04:21.123202','',1,1,1),(2,10,0,0,10,0,0,1,700000,'0',0,1,0,0,'man power operation executive 10','2019-04-04 17:07:16.320506','','2019-04-04 17:07:16.320557','',1,1,2);
/*!40000 ALTER TABLE `contract_contractdetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contract_contracttype`
--

DROP TABLE IF EXISTS `contract_contracttype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contract_contracttype` (
  `contracttypeid` int(11) NOT NULL,
  `cnttypename` varchar(30) NOT NULL,
  `cnttypecode` varchar(5) NOT NULL,
  `created` datetime(6) NOT NULL,
  `createdby` varchar(20) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `updatedby` varchar(20) NOT NULL,
  PRIMARY KEY (`contracttypeid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contract_contracttype`
--

LOCK TABLES `contract_contracttype` WRITE;
/*!40000 ALTER TABLE `contract_contracttype` DISABLE KEYS */;
INSERT INTO `contract_contracttype` VALUES (1,'ManPower','MNP','2019-04-04 13:41:27.605189','','2019-04-04 13:41:27.605302',''),(2,'Fixed Price','FXP','2019-04-04 13:41:46.523874','','2019-04-04 13:41:46.524036',''),(3,'OUTPUT based Pricing','OBPR','2019-04-04 13:42:18.404362','','2019-04-04 13:42:18.404562','');
/*!40000 ALTER TABLE `contract_contracttype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contract_detailattcapture`
--

DROP TABLE IF EXISTS `contract_detailattcapture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contract_detailattcapture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `skillcount` int(11) NOT NULL,
  `skillotcount` int(11) NOT NULL,
  `extrashift` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `createdby` varchar(20) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `updatedby` varchar(20) NOT NULL,
  `contractid_id` int(11) NOT NULL,
  `skillid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contract_detailattca_contractid_id_c553d04e_fk_contract_` (`contractid_id`),
  KEY `contract_detailattca_skillid_id_2a843897_fk_contract_` (`skillid_id`),
  CONSTRAINT `contract_detailattca_contractid_id_c553d04e_fk_contract_` FOREIGN KEY (`contractid_id`) REFERENCES `contract_contract` (`contractid`),
  CONSTRAINT `contract_detailattca_skillid_id_2a843897_fk_contract_` FOREIGN KEY (`skillid_id`) REFERENCES `contract_skilllevel` (`skillid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contract_detailattcapture`
--

LOCK TABLES `contract_detailattcapture` WRITE;
/*!40000 ALTER TABLE `contract_detailattcapture` DISABLE KEYS */;
/*!40000 ALTER TABLE `contract_detailattcapture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contract_document`
--

DROP TABLE IF EXISTS `contract_document`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contract_document` (
  `id` int(11) NOT NULL DEFAULT '0',
  `description` varchar(255) NOT NULL,
  `document` varchar(100) NOT NULL,
  `document1` varchar(100) NOT NULL,
  `document2` varchar(100) DEFAULT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `created` datetime(6) NOT NULL,
  `createdby` varchar(20) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `updatedby` varchar(20) NOT NULL,
  `contractid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contract_document`
--

LOCK TABLES `contract_document` WRITE;
/*!40000 ALTER TABLE `contract_document` DISABLE KEYS */;
/*!40000 ALTER TABLE `contract_document` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contract_ratetype`
--

DROP TABLE IF EXISTS `contract_ratetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contract_ratetype` (
  `ratetypeid` int(11) NOT NULL,
  `ratetypename` varchar(30) NOT NULL,
  `ratetypecode` varchar(5) NOT NULL,
  `created` datetime(6) NOT NULL,
  `createdby` varchar(20) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `updatedby` varchar(20) NOT NULL,
  `contracttypeid_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`ratetypeid`),
  KEY `contract_ratetype_contracttypeid_id_5f5ffd8d_fk_contract_` (`contracttypeid_id`),
  CONSTRAINT `contract_ratetype_contracttypeid_id_5f5ffd8d_fk_contract_` FOREIGN KEY (`contracttypeid_id`) REFERENCES `contract_contracttype` (`contracttypeid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contract_ratetype`
--

LOCK TABLES `contract_ratetype` WRITE;
/*!40000 ALTER TABLE `contract_ratetype` DISABLE KEYS */;
INSERT INTO `contract_ratetype` VALUES (1,'FLat rate ctr','FRCO','2019-04-04 13:44:27.527312','','2019-04-04 13:44:27.527360','',1),(2,'costRate','CTRT','2019-04-04 13:45:28.373726','','2019-04-04 13:45:28.373865','',1),(3,'LumSum','LUMS','2019-04-04 13:45:56.637495','','2019-04-04 13:45:56.637620','',2),(4,'SlabBasedOverlap','SBOV','2019-04-04 13:46:45.711221','','2019-04-04 13:46:45.711266','',3),(5,'SlabBasedFlat','SBFL','2019-04-04 13:47:03.672257','','2019-04-04 13:47:03.672356','',3);
/*!40000 ALTER TABLE `contract_ratetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contract_skilllevel`
--

DROP TABLE IF EXISTS `contract_skilllevel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contract_skilllevel` (
  `skillid` int(11) NOT NULL,
  `skillname` varchar(30) NOT NULL,
  `skillcode` varchar(5) NOT NULL,
  `skilllevel` varchar(2) NOT NULL,
  `created` datetime(6) NOT NULL,
  `createdby` varchar(20) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `updatedby` varchar(20) NOT NULL,
  PRIMARY KEY (`skillid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contract_skilllevel`
--

LOCK TABLES `contract_skilllevel` WRITE;
/*!40000 ALTER TABLE `contract_skilllevel` DISABLE KEYS */;
INSERT INTO `contract_skilllevel` VALUES (1,'Operation Executive','OPEX','9','2019-04-04 15:32:42.432722','','2019-04-04 15:32:42.432790',''),(2,'HRT Operator','HROP','8','2019-04-04 15:33:31.661548','','2019-04-04 15:33:31.661749',''),(3,'MHE Operator','MHOP','7','2019-04-04 15:34:07.163341','','2019-04-04 15:34:07.163547',''),(4,'FLT Operator','FLOP','6','2019-04-04 15:34:43.605464','','2019-04-04 15:34:43.605705',''),(5,'SMD CAsual','SMCS','5','2019-04-04 15:35:51.191846','','2019-04-04 15:35:51.191976','');
/*!40000 ALTER TABLE `contract_skilllevel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (10,'account','access'),(15,'account','ba'),(11,'account','customer'),(12,'account','user'),(13,'account','useraccess'),(14,'account','userlocationcustomer'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(16,'contract','contract'),(17,'contract','contractdetail'),(18,'contract','contracttype'),(22,'contract','detailattcapture'),(19,'contract','document'),(21,'contract','ratetype'),(20,'contract','skilllevel'),(7,'location','city'),(8,'location','operationlocation'),(9,'location','state'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'location','0001_initial','2019-04-04 11:20:09.413172'),(2,'account','0001_initial','2019-04-04 11:20:25.284467'),(3,'account','0002_ba','2019-04-04 11:20:26.065605'),(4,'contenttypes','0001_initial','2019-04-04 11:20:28.147078'),(5,'auth','0001_initial','2019-04-04 11:20:52.554697'),(6,'admin','0001_initial','2019-04-04 11:20:58.210524'),(7,'admin','0002_logentry_remove_auto_add','2019-04-04 11:20:58.375921'),(8,'admin','0003_logentry_add_action_flag_choices','2019-04-04 11:20:58.666719'),(9,'contenttypes','0002_remove_content_type_name','2019-04-04 11:21:02.641909'),(10,'auth','0002_alter_permission_name_max_length','2019-04-04 11:21:03.022186'),(11,'auth','0003_alter_user_email_max_length','2019-04-04 11:21:03.343121'),(12,'auth','0004_alter_user_username_opts','2019-04-04 11:21:03.523948'),(13,'auth','0005_alter_user_last_login_null','2019-04-04 11:21:05.026063'),(14,'auth','0006_require_contenttypes_0002','2019-04-04 11:21:05.137309'),(15,'auth','0007_alter_validators_add_error_messages','2019-04-04 11:21:05.245158'),(16,'auth','0008_alter_user_username_max_length','2019-04-04 11:21:05.587341'),(17,'auth','0009_alter_user_last_name_max_length','2019-04-04 11:21:05.861384'),(20,'sessions','0001_initial','2019-04-04 11:21:55.002682'),(28,'contract','0001_initial','2019-04-16 12:46:23.075719');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location_city`
--

DROP TABLE IF EXISTS `location_city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `location_city` (
  `cityid` int(11) NOT NULL,
  `citycode` varchar(5) NOT NULL,
  `cityname` varchar(25) NOT NULL,
  `created` datetime(6) NOT NULL,
  `createdby` varchar(20) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `updatedby` varchar(20) NOT NULL,
  `citystate_id` int(11) NOT NULL,
  PRIMARY KEY (`cityid`),
  KEY `location_city_citystate_id_852f8a01_fk_location_state_stateid` (`citystate_id`),
  CONSTRAINT `location_city_citystate_id_852f8a01_fk_location_state_stateid` FOREIGN KEY (`citystate_id`) REFERENCES `location_state` (`stateid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location_city`
--

LOCK TABLES `location_city` WRITE;
/*!40000 ALTER TABLE `location_city` DISABLE KEYS */;
INSERT INTO `location_city` VALUES (1,'MUM','Mumbai','2019-04-04 13:24:11.860334','','2019-04-04 13:24:11.860430','',1),(2,'NAG','Nagpur','2019-04-04 13:24:22.775655','','2019-04-04 13:24:22.775746','',1),(3,'PUN','PUNE','2019-04-04 13:24:40.530168','','2019-04-04 13:24:40.530328','',1),(4,'BANG','Banglore','2019-04-04 13:25:13.010653','','2019-04-04 13:25:13.010721','',4),(5,'TRL','TIRULA','2019-04-04 13:25:37.127696','','2019-04-04 13:25:37.127756','',4),(6,'AHM','AHMADABAD','2019-04-04 13:26:03.785205','','2019-04-04 13:26:03.785330','',2),(7,'GND','GANDHINAGAR','2019-04-04 13:26:23.737652','','2019-04-04 13:26:23.737703','',2);
/*!40000 ALTER TABLE `location_city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location_operationlocation`
--

DROP TABLE IF EXISTS `location_operationlocation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `location_operationlocation` (
  `oplocationid` int(11) NOT NULL,
  `oploccode` varchar(7) NOT NULL,
  `oploclat` double NOT NULL,
  `oploclong` double NOT NULL,
  `oplocaddress` longtext NOT NULL,
  `created` datetime(6) NOT NULL,
  `createdby` varchar(20) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `updatedby` varchar(20) NOT NULL,
  `oploccity_id` int(11) NOT NULL,
  PRIMARY KEY (`oplocationid`),
  UNIQUE KEY `oploccode` (`oploccode`),
  KEY `location_operationlo_oploccity_id_e8fb56a9_fk_location_` (`oploccity_id`),
  CONSTRAINT `location_operationlo_oploccity_id_e8fb56a9_fk_location_` FOREIGN KEY (`oploccity_id`) REFERENCES `location_city` (`cityid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location_operationlocation`
--

LOCK TABLES `location_operationlocation` WRITE;
/*!40000 ALTER TABLE `location_operationlocation` DISABLE KEYS */;
INSERT INTO `location_operationlocation` VALUES (1,'MLD',111111,22222,'Malad','2019-04-04 13:28:10.408126','','2019-04-04 13:28:10.408215','',1),(2,'GORE',111111,22222,'Goregaon','2019-04-04 13:28:31.915350','','2019-04-04 13:28:31.915472','',1),(3,'DDR',111111,22222,'DADAR','2019-04-04 13:28:53.852940','','2019-04-04 13:28:53.853034','',1),(4,'ELP',111111,22222,'BANG ELPHISTINE','2019-04-04 13:29:23.229922','','2019-04-04 13:29:23.229976','',4),(5,'BANG2',111111,22222,'BANGlore2 ELPHISTINE','2019-04-04 13:29:53.166755','','2019-04-04 13:29:53.166893','',4),(6,'AHM1',111111,22222,'AHmedabad 1','2019-04-04 13:30:27.151691','','2019-04-04 13:30:27.151733','',6),(7,'AHM2',111111,22222,'AHmedabad 2','2019-04-04 13:30:42.873993','','2019-04-04 13:30:42.874086','',6);
/*!40000 ALTER TABLE `location_operationlocation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location_state`
--

DROP TABLE IF EXISTS `location_state`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `location_state` (
  `stateid` int(11) NOT NULL,
  `statecode` varchar(5) NOT NULL,
  `statename` varchar(25) NOT NULL,
  `statecountry` varchar(30) NOT NULL,
  `created` datetime(6) NOT NULL,
  `createdby` varchar(20) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `updatedby` varchar(20) NOT NULL,
  PRIMARY KEY (`stateid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location_state`
--

LOCK TABLES `location_state` WRITE;
/*!40000 ALTER TABLE `location_state` DISABLE KEYS */;
INSERT INTO `location_state` VALUES (1,'MAH','MAHARASHTRA','India','2019-04-04 13:21:36.491972','','2019-04-04 13:21:36.492069',''),(2,'GUJ','GUJRAT','India','2019-04-04 13:22:00.620653','','2019-04-04 13:22:00.620721',''),(3,'MP','Madhay Pradesh','India','2019-04-04 13:22:31.512792','','2019-04-04 13:22:31.512851',''),(4,'KTK','KARNATKA','India','2019-04-04 13:22:56.755746','','2019-04-04 13:22:56.755878',''),(5,'KRL','KERLA','India','2019-04-04 13:23:39.763592','','2019-04-04 13:23:39.763645','');
/*!40000 ALTER TABLE `location_state` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-16 18:29:18
