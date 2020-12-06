-- MySQL dump 10.14  Distrib 5.5.68-MariaDB, for Linux (x86_64)
--
-- Host: 165.132.105.42    Database: team1
-- ------------------------------------------------------
-- Server version	5.5.68-MariaDB

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
-- Current Database: `team1`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `team1` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;

USE `team1`;

--
-- Table structure for table `FICTION`
--

DROP TABLE IF EXISTS `FICTION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FICTION` (
  `index` bigint(20) DEFAULT NULL,
  `Name` text COLLATE utf8_unicode_ci,
  `Author` text COLLATE utf8_unicode_ci,
  `User Rating` double DEFAULT NULL,
  `Reviews` bigint(20) DEFAULT NULL,
  `Price` bigint(20) DEFAULT NULL,
  `Year` bigint(20) DEFAULT NULL,
  `Genre` text COLLATE utf8_unicode_ci,
  KEY `ix_FICTION_index` (`index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FICTION`
--

LOCK TABLES `FICTION` WRITE;
/*!40000 ALTER TABLE `FICTION` DISABLE KEYS */;
INSERT INTO `FICTION` VALUES (0,'Dead Reckoning (Sookie Stackhouse/True Blood, Book 11)','Charlaine Harris',4.2,2094,4,2011,'Fiction'),(1,'Goodnight Moon','Margaret Wise Brown',4.8,8837,5,2017,'Fiction'),(2,'Dog Man: A Tale of Two Kitties: From the Creator of Captain Underpants (Dog Man #3)','Dav Pilkey',4.9,4786,8,2017,'Fiction'),(3,'New Moon (The Twilight Saga)','Stephenie Meyer',4.6,5680,10,2009,'Fiction'),(4,'Thirteen Reasons Why','Jay Asher',4.5,7932,9,2017,'Fiction'),(5,'Wonder','R. J. Palacio',4.8,21625,9,2017,'Fiction'),(6,'The Fault in Our Stars','John Green',4.7,50482,7,2014,'Fiction'),(7,'Oh, the Places You\'ll Go!','Dr. Seuss',4.9,21834,8,2012,'Fiction'),(8,'A Game of Thrones / A Clash of Kings / A Storm of Swords / A Feast of Crows / A Dance with Dragons','George R. R. Martin',4.7,19735,30,2014,'Fiction'),(9,'The Going-To-Bed Book','Sandra Boynton',4.8,5249,5,2016,'Fiction');
/*!40000 ALTER TABLE `FICTION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `NON_FICTION`
--

DROP TABLE IF EXISTS `NON_FICTION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `NON_FICTION` (
  `BOOK_ID` int(11) NOT NULL AUTO_INCREMENT,
  `BOOK_NAME` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `AUTHOR` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `RATING` float NOT NULL,
  `REVIEWS` int(11) NOT NULL,
  `PRICE` float NOT NULL,
  `YEAR` date NOT NULL,
  `GENRE` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`BOOK_ID`),
  UNIQUE KEY `BOOK_NAME` (`BOOK_NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `NON_FICTION`
--

LOCK TABLES `NON_FICTION` WRITE;
/*!40000 ALTER TABLE `NON_FICTION` DISABLE KEYS */;
/*!40000 ALTER TABLE `NON_FICTION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_userprofile`
--

DROP TABLE IF EXISTS `accounts_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_userprofile` (
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `username` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `PW` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `birthdate` date NOT NULL,
  `phone` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `address` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `gender` varchar(6) COLLATE utf8_unicode_ci NOT NULL,
  `role` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_userprofile`
--

LOCK TABLES `accounts_userprofile` WRITE;
/*!40000 ALTER TABLE `accounts_userprofile` DISABLE KEYS */;
INSERT INTO `accounts_userprofile` VALUES ('pbkdf2_sha256$120000$YOUVHhtNT45v$rsfhHrkj82vwsuPGdHheHIGq/jai3wnzXXq10uIMmds=','2020-12-06 11:12:29',0,0,1,'2020-12-06 11:01:43',1,'ADMIN','ADMIN','admin','admin','sk981102@gmail.com','1998-11-02','01012343434','서울특별시 서대문구 연세로 50 연세대학교','M','A'),('pbkdf2_sha256$120000$tK1BbyYbHE4x$95AFUzXF5tnuZfNA5I6tTxoRLUjkYNdj/2G9EYgYu4M=','2020-12-06 11:12:14',0,0,1,'2020-12-06 11:02:33',2,'시연','김','rater1','rater1234','sk981102@gmail.com','2020-12-06','01012343434','서울특별시 서대문구 연세로 50 연세대학교','F','R'),('pbkdf2_sha256$120000$RkdPc1SFVdeG$rXznJTY825QmT+z3WDaPkaFGqIg6AjXkwiooNlxHU6A=','2020-12-06 11:11:31',0,0,1,'2020-12-06 11:03:10',3,'민주','기','submitter1','submitter123','na@naver.com','1998-12-06','01012343434','서울특별시 서대문구 연세로 50 연세대학교;','M','S');
/*!40000 ALTER TABLE `accounts_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_userprofile_groups`
--

DROP TABLE IF EXISTS `accounts_userprofile_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_userprofile_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_userprofile_gro_userprofile_id_group_id_36cd9fa6_uniq` (`userprofile_id`,`group_id`),
  KEY `accounts_userprofile_groups_group_id_74ae51cf_fk_auth_group_id` (`group_id`),
  CONSTRAINT `accounts_userprofile_groups_group_id_74ae51cf_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `accounts_userprofile_userprofile_id_b7fb6469_fk_accounts_` FOREIGN KEY (`userprofile_id`) REFERENCES `accounts_userprofile` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_userprofile_groups`
--

LOCK TABLES `accounts_userprofile_groups` WRITE;
/*!40000 ALTER TABLE `accounts_userprofile_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_userprofile_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_userprofile_user_permissions`
--

DROP TABLE IF EXISTS `accounts_userprofile_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_userprofile_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_userprofile_use_userprofile_id_permissio_22053107_uniq` (`userprofile_id`,`permission_id`),
  KEY `accounts_userprofile_permission_id_a9b2b32b_fk_auth_perm` (`permission_id`),
  CONSTRAINT `accounts_userprofile_permission_id_a9b2b32b_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `accounts_userprofile_userprofile_id_4acaf5a0_fk_accounts_` FOREIGN KEY (`userprofile_id`) REFERENCES `accounts_userprofile` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_userprofile_user_permissions`
--

LOCK TABLES `accounts_userprofile_user_permissions` WRITE;
/*!40000 ALTER TABLE `accounts_userprofile_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_userprofile_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `apply_task`
--

DROP TABLE IF EXISTS `apply_task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `apply_task` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `approved` int(11) NOT NULL,
  `submitter_id` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `apply_task_submitter_id_task_id_315bfc9c_uniq` (`submitter_id`,`task_id`),
  KEY `apply_task_task_id_466333df` (`task_id`),
  CONSTRAINT `apply_task_task_id_466333df_fk_task_task_id` FOREIGN KEY (`task_id`) REFERENCES `task` (`task_id`),
  CONSTRAINT `apply_task_submitter_id_1e8231a4_fk_submitter_user_id_id` FOREIGN KEY (`submitter_id`) REFERENCES `submitter` (`user_id_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apply_task`
--

LOCK TABLES `apply_task` WRITE;
/*!40000 ALTER TABLE `apply_task` DISABLE KEYS */;
INSERT INTO `apply_task` VALUES (1,1,3,1);
/*!40000 ALTER TABLE `apply_task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `assigned_task`
--

DROP TABLE IF EXISTS `assigned_task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `assigned_task` (
  `type_id` int(11) NOT NULL AUTO_INCREMENT,
  `rated` int(11) NOT NULL,
  `rater` int(11) NOT NULL,
  `raw_data_type` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`type_id`),
  KEY `assigned_task_rater_0399ffba` (`rater`),
  KEY `assigned_task_raw_data_type_6b2eb1bc` (`raw_data_type`),
  KEY `assigned_task_task_id_bf7fc6a9` (`task_id`),
  CONSTRAINT `assigned_task_task_id_bf7fc6a9_fk_task_task_id` FOREIGN KEY (`task_id`) REFERENCES `task` (`task_id`),
  CONSTRAINT `assigned_task_rater_0399ffba_fk_rater_user_id_id` FOREIGN KEY (`rater`) REFERENCES `rater` (`user_id_id`),
  CONSTRAINT `assigned_task_raw_data_type_6b2eb1bc_fk_raw_data_` FOREIGN KEY (`raw_data_type`) REFERENCES `raw_data_seq_file` (`seqnumber`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assigned_task`
--

LOCK TABLES `assigned_task` WRITE;
/*!40000 ALTER TABLE `assigned_task` DISABLE KEYS */;
INSERT INTO `assigned_task` VALUES (1,1,2,1,1),(2,1,2,2,1);
/*!40000 ALTER TABLE `assigned_task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
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
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_userprofile'),(22,'Can change user',6,'change_userprofile'),(23,'Can delete user',6,'delete_userprofile'),(24,'Can view user',6,'view_userprofile'),(25,'Can add assigned task',7,'add_assignedtask'),(26,'Can change assigned task',7,'change_assignedtask'),(27,'Can delete assigned task',7,'delete_assignedtask'),(28,'Can view assigned task',7,'view_assignedtask'),(29,'Can add rater',8,'add_rater'),(30,'Can change rater',8,'change_rater'),(31,'Can delete rater',8,'delete_rater'),(32,'Can view rater',8,'view_rater'),(33,'Can add submitter',9,'add_submitter'),(34,'Can change submitter',9,'change_submitter'),(35,'Can delete submitter',9,'delete_submitter'),(36,'Can view submitter',9,'view_submitter'),(37,'Can add apply task',10,'add_applytask'),(38,'Can change apply task',10,'change_applytask'),(39,'Can delete apply task',10,'delete_applytask'),(40,'Can view apply task',10,'view_applytask'),(41,'Can add task',11,'add_task'),(42,'Can change task',11,'change_task'),(43,'Can delete task',11,'delete_task'),(44,'Can view task',11,'view_task'),(45,'Can add task data table',12,'add_taskdatatable'),(46,'Can change task data table',12,'change_taskdatatable'),(47,'Can delete task data table',12,'delete_taskdatatable'),(48,'Can view task data table',12,'view_taskdatatable'),(49,'Can add task data table schema',13,'add_taskdatatableschema'),(50,'Can change task data table schema',13,'change_taskdatatableschema'),(51,'Can delete task data table schema',13,'delete_taskdatatableschema'),(52,'Can view task data table schema',13,'view_taskdatatableschema'),(53,'Can add task schema',14,'add_taskschema'),(54,'Can change task schema',14,'change_taskschema'),(55,'Can delete task schema',14,'delete_taskschema'),(56,'Can view task schema',14,'view_taskschema'),(57,'Can add raw data seq file',15,'add_rawdataseqfile'),(58,'Can change raw data seq file',15,'change_rawdataseqfile'),(59,'Can delete raw data seq file',15,'delete_rawdataseqfile'),(60,'Can view raw data seq file',15,'view_rawdataseqfile'),(61,'Can add raw data type',16,'add_rawdatatype'),(62,'Can change raw data type',16,'change_rawdatatype'),(63,'Can delete raw data type',16,'delete_rawdatatype'),(64,'Can view raw data type',16,'view_rawdatatype'),(65,'Can add raw data type schema',17,'add_rawdatatypeschema'),(66,'Can change raw data type schema',17,'change_rawdatatypeschema'),(67,'Can delete raw data type schema',17,'delete_rawdatatypeschema'),(68,'Can view raw data type schema',17,'view_rawdatatypeschema'),(69,'Can add raw data type request',18,'add_rawdatatyperequest'),(70,'Can change raw data type request',18,'change_rawdatatyperequest'),(71,'Can delete raw data type request',18,'delete_rawdatatyperequest'),(72,'Can view raw data type request',18,'view_rawdatatyperequest'),(73,'Can add parsed data',19,'add_parseddata'),(74,'Can change parsed data',19,'change_parseddata'),(75,'Can delete parsed data',19,'delete_parseddata'),(76,'Can view parsed data',19,'view_parseddata'),(77,'Can add download',20,'add_download'),(78,'Can change download',20,'change_download'),(79,'Can delete download',20,'delete_download'),(80,'Can view download',20,'view_download'),(81,'Can add my admin',21,'add_myadmin'),(82,'Can change my admin',21,'change_myadmin'),(83,'Can delete my admin',21,'delete_myadmin'),(84,'Can view my admin',21,'view_myadmin'),(85,'Can add task create',22,'add_taskcreate'),(86,'Can change task create',22,'change_taskcreate'),(87,'Can delete task create',22,'delete_taskcreate'),(88,'Can view task create',22,'view_taskcreate');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_accounts_` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_` FOREIGN KEY (`user_id`) REFERENCES `accounts_userprofile` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
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
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (6,'accounts','userprofile'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(20,'my_admin','download'),(21,'my_admin','myadmin'),(22,'my_admin','taskcreate'),(19,'parsed_data','parseddata'),(7,'rater','assignedtask'),(8,'rater','rater'),(15,'raw_data','rawdataseqfile'),(16,'raw_data','rawdatatype'),(18,'raw_data','rawdatatyperequest'),(17,'raw_data','rawdatatypeschema'),(5,'sessions','session'),(9,'submitter','submitter'),(10,'task','applytask'),(11,'task','task'),(12,'task','taskdatatable'),(13,'task','taskdatatableschema'),(14,'task','taskschema');
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
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-12-06 10:58:31'),(2,'contenttypes','0002_remove_content_type_name','2020-12-06 10:58:31'),(3,'auth','0001_initial','2020-12-06 10:58:32'),(4,'auth','0002_alter_permission_name_max_length','2020-12-06 10:58:32'),(5,'auth','0003_alter_user_email_max_length','2020-12-06 10:58:32'),(6,'auth','0004_alter_user_username_opts','2020-12-06 10:58:32'),(7,'auth','0005_alter_user_last_login_null','2020-12-06 10:58:32'),(8,'auth','0006_require_contenttypes_0002','2020-12-06 10:58:32'),(9,'auth','0007_alter_validators_add_error_messages','2020-12-06 10:58:32'),(10,'auth','0008_alter_user_username_max_length','2020-12-06 10:58:32'),(11,'auth','0009_alter_user_last_name_max_length','2020-12-06 10:58:32'),(12,'accounts','0001_initial','2020-12-06 10:58:32'),(13,'admin','0001_initial','2020-12-06 10:58:33'),(14,'admin','0002_logentry_remove_auto_add','2020-12-06 10:58:33'),(15,'admin','0003_logentry_add_action_flag_choices','2020-12-06 10:58:33'),(16,'my_admin','0001_initial','2020-12-06 10:58:33'),(17,'submitter','0001_initial','2020-12-06 10:58:33'),(18,'task','0001_initial','2020-12-06 10:58:34'),(19,'raw_data','0001_initial','2020-12-06 10:58:35'),(20,'rater','0001_initial','2020-12-06 10:58:36'),(21,'parsed_data','0001_initial','2020-12-06 10:58:36'),(22,'task','0002_auto_20201206_1429','2020-12-06 10:58:36'),(23,'raw_data','0002_auto_20201206_1429','2020-12-06 10:58:37'),(24,'raw_data','0003_rawdatatyperequest','2020-12-06 10:58:37'),(25,'sessions','0001_initial','2020-12-06 10:58:37');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('jss2titmyffh6rkf4ibvrqx5rwg5k9t6','NGYzZmEyYTYyMmVjOWQ5MTJkNzBlZTkwNjU5M2NlNjg2ODc5OWE2Zjp7InRhc2tpZCI6IjEifQ==','2020-12-20 11:06:13'),('udsm259ykehlq0yja81jc52drskd6e0x','YWFlMTEyMDFjZTUxNDVkMGU0ZDliMzQzNjNkNzU1NzEyYWY2MGU4Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiYTk1NjlkYWI2ZWFjMzdiMzM1NzUzMTA1MzRmM2FkMmRjYjFjNGY3IiwidGFza2lkIjoiMSJ9','2020-12-20 11:12:31'),('wn85cdhnxhs4pvgmlqelkt9myxngyjj5','NTAwOTNiMDUzMDk1MWI2YzFmYWY5OGJhMWZkNjY2MGFkNjZmNjFmZDp7InRhc2tpZCI6IjEiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYmE5NTY5ZGFiNmVhYzM3YjMzNTc1MzEwNTM0ZjNhZDJkY2IxYzRmNyJ9','2020-12-20 11:06:56');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `my_admin`
--

DROP TABLE IF EXISTS `my_admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `my_admin` (
  `user_id_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id_id`),
  CONSTRAINT `my_admin_user_id_id_6fe69992_fk_accounts_userprofile_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `accounts_userprofile` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `my_admin`
--

LOCK TABLES `my_admin` WRITE;
/*!40000 ALTER TABLE `my_admin` DISABLE KEYS */;
INSERT INTO `my_admin` VALUES (1);
/*!40000 ALTER TABLE `my_admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `my_admin_download`
--

DROP TABLE IF EXISTS `my_admin_download`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `my_admin_download` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Path` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `my_admin_download`
--

LOCK TABLES `my_admin_download` WRITE;
/*!40000 ALTER TABLE `my_admin_download` DISABLE KEYS */;
/*!40000 ALTER TABLE `my_admin_download` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `my_admin_taskcreate`
--

DROP TABLE IF EXISTS `my_admin_taskcreate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `my_admin_taskcreate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `Comment` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `mincycle` int(11) NOT NULL,
  `TaskDataTableName` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `TaskDataTableScheme` varchar(10000) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Name` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `my_admin_taskcreate`
--

LOCK TABLES `my_admin_taskcreate` WRITE;
/*!40000 ALTER TABLE `my_admin_taskcreate` DISABLE KEYS */;
/*!40000 ALTER TABLE `my_admin_taskcreate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parsed_data`
--

DROP TABLE IF EXISTS `parsed_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parsed_data` (
  `parsed_id` int(11) NOT NULL AUTO_INCREMENT,
  `total_tuple_num` int(11) DEFAULT NULL,
  `duplicate_tuple_num` int(11) DEFAULT NULL,
  `column_null_ratio` double DEFAULT NULL,
  `quantity_score` int(11) DEFAULT NULL,
  `quality_score` int(10) unsigned DEFAULT NULL,
  `evaluated` int(11) NOT NULL,
  `pass` int(11) NOT NULL,
  `rater_id` int(11) NOT NULL,
  `raw_data_seq_file` int(11) NOT NULL,
  `submitter_id` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`parsed_id`),
  KEY `parsed_data_rater_id_0a6fa9d0_fk_rater_user_id_id` (`rater_id`),
  KEY `parsed_data_raw_data_seq_file_1d9f2aa2_fk_raw_data_` (`raw_data_seq_file`),
  KEY `parsed_data_submitter_id_6a43be03_fk_submitter_user_id_id` (`submitter_id`),
  KEY `parsed_data_task_id_3dd1dd5f_fk_task_task_id` (`task_id`),
  CONSTRAINT `parsed_data_task_id_3dd1dd5f_fk_task_task_id` FOREIGN KEY (`task_id`) REFERENCES `task` (`task_id`),
  CONSTRAINT `parsed_data_rater_id_0a6fa9d0_fk_rater_user_id_id` FOREIGN KEY (`rater_id`) REFERENCES `rater` (`user_id_id`),
  CONSTRAINT `parsed_data_raw_data_seq_file_1d9f2aa2_fk_raw_data_` FOREIGN KEY (`raw_data_seq_file`) REFERENCES `raw_data_seq_file` (`seqnumber`),
  CONSTRAINT `parsed_data_submitter_id_6a43be03_fk_submitter_user_id_id` FOREIGN KEY (`submitter_id`) REFERENCES `submitter` (`user_id_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parsed_data`
--

LOCK TABLES `parsed_data` WRITE;
/*!40000 ALTER TABLE `parsed_data` DISABLE KEYS */;
INSERT INTO `parsed_data` VALUES (1,10,0,0,10,9,1,1,2,1,3,1),(2,10,0,0,10,10,1,1,2,2,3,1);
/*!40000 ALTER TABLE `parsed_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rater`
--

DROP TABLE IF EXISTS `rater`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rater` (
  `user_id_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id_id`),
  CONSTRAINT `rater_user_id_id_2f03e2ca_fk_accounts_userprofile_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `accounts_userprofile` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rater`
--

LOCK TABLES `rater` WRITE;
/*!40000 ALTER TABLE `rater` DISABLE KEYS */;
INSERT INTO `rater` VALUES (2);
/*!40000 ALTER TABLE `rater` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `raw_data_seq_file`
--

DROP TABLE IF EXISTS `raw_data_seq_file`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `raw_data_seq_file` (
  `file` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `seqnumber` int(11) NOT NULL AUTO_INCREMENT,
  `term_start` date DEFAULT NULL,
  `term_end` date DEFAULT NULL,
  `round` int(11) NOT NULL,
  `raw_data_type` int(11) NOT NULL,
  `submitter_id` int(11) NOT NULL,
  PRIMARY KEY (`seqnumber`),
  KEY `raw_data_seq_file_raw_data_type_b661c55f` (`raw_data_type`),
  KEY `raw_data_seq_file_submitter_id_d186c8cc` (`submitter_id`),
  CONSTRAINT `raw_data_seq_file_submitter_id_d186c8cc_fk_submitter_user_id_id` FOREIGN KEY (`submitter_id`) REFERENCES `submitter` (`user_id_id`),
  CONSTRAINT `raw_data_seq_file_raw_data_type_b661c55f_fk_raw_data_` FOREIGN KEY (`raw_data_type`) REFERENCES `raw_data_type` (`type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `raw_data_seq_file`
--

LOCK TABLES `raw_data_seq_file` WRITE;
/*!40000 ALTER TABLE `raw_data_seq_file` DISABLE KEYS */;
INSERT INTO `raw_data_seq_file` VALUES ('fiction_correct_Nii2O6p.csv',1,'2020-12-01','2020-12-06',1,1,3),('fiction_correct_BTVkLRm.csv',2,'2020-12-02','2020-12-06',2,1,3);
/*!40000 ALTER TABLE `raw_data_seq_file` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `raw_data_type`
--

DROP TABLE IF EXISTS `raw_data_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `raw_data_type` (
  `type_id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `admin_id` int(11) NOT NULL,
  `task` int(11) NOT NULL,
  PRIMARY KEY (`type_id`),
  UNIQUE KEY `type_name` (`type_name`),
  KEY `raw_data_type_admin_id_15d098de_fk_my_admin_user_id_id` (`admin_id`),
  KEY `raw_data_type_task_63a5e496_fk_task_task_id` (`task`),
  CONSTRAINT `raw_data_type_task_63a5e496_fk_task_task_id` FOREIGN KEY (`task`) REFERENCES `task` (`task_id`),
  CONSTRAINT `raw_data_type_admin_id_15d098de_fk_my_admin_user_id_id` FOREIGN KEY (`admin_id`) REFERENCES `my_admin` (`user_id_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `raw_data_type`
--

LOCK TABLES `raw_data_type` WRITE;
/*!40000 ALTER TABLE `raw_data_type` DISABLE KEYS */;
INSERT INTO `raw_data_type` VALUES (1,'FICTION',1,1),(2,'NON_FICTION',1,2);
/*!40000 ALTER TABLE `raw_data_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `raw_data_type_request`
--

DROP TABLE IF EXISTS `raw_data_type_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `raw_data_type_request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `task` int(11) NOT NULL,
  PRIMARY KEY (`request_id`),
  KEY `raw_data_type_request_task_2711d12a_fk_task_task_id` (`task`),
  CONSTRAINT `raw_data_type_request_task_2711d12a_fk_task_task_id` FOREIGN KEY (`task`) REFERENCES `task` (`task_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `raw_data_type_request`
--

LOCK TABLES `raw_data_type_request` WRITE;
/*!40000 ALTER TABLE `raw_data_type_request` DISABLE KEYS */;
/*!40000 ALTER TABLE `raw_data_type_request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `raw_data_type_schema`
--

DROP TABLE IF EXISTS `raw_data_type_schema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `raw_data_type_schema` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `field_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `field_type` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `null_value` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `mapping_field_id` int(11) NOT NULL,
  `type_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `raw_data_type_schema_type_id_id_3b4bc605_fk_raw_data_` (`type_id_id`),
  KEY `raw_data_type_schema_mapping_field_id_ccf59384_fk_task_data` (`mapping_field_id`),
  CONSTRAINT `raw_data_type_schema_mapping_field_id_ccf59384_fk_task_data` FOREIGN KEY (`mapping_field_id`) REFERENCES `task_data_table_schema` (`field_id`),
  CONSTRAINT `raw_data_type_schema_type_id_id_3b4bc605_fk_raw_data_` FOREIGN KEY (`type_id_id`) REFERENCES `raw_data_type` (`type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `raw_data_type_schema`
--

LOCK TABLES `raw_data_type_schema` WRITE;
/*!40000 ALTER TABLE `raw_data_type_schema` DISABLE KEYS */;
INSERT INTO `raw_data_type_schema` VALUES (1,'sold_out','boolean','N',1,1),(2,'seller','char','Y',2,2);
/*!40000 ALTER TABLE `raw_data_type_schema` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `submitter`
--

DROP TABLE IF EXISTS `submitter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `submitter` (
  `user_id_id` int(11) NOT NULL,
  `score` double NOT NULL,
  PRIMARY KEY (`user_id_id`),
  CONSTRAINT `submitter_user_id_id_c69091a7_fk_accounts_userprofile_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `accounts_userprofile` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `submitter`
--

LOCK TABLES `submitter` WRITE;
/*!40000 ALTER TABLE `submitter` DISABLE KEYS */;
INSERT INTO `submitter` VALUES (3,9.75);
/*!40000 ALTER TABLE `submitter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task`
--

DROP TABLE IF EXISTS `task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `task` (
  `task_id` int(11) NOT NULL AUTO_INCREMENT,
  `task_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `description` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `mincycle` int(11) NOT NULL,
  `pass_standard` int(11) NOT NULL,
  `admin` int(11) NOT NULL,
  PRIMARY KEY (`task_id`),
  UNIQUE KEY `task_name` (`task_name`),
  KEY `task_admin_deda9711` (`admin`),
  CONSTRAINT `task_admin_deda9711_fk_my_admin_user_id_id` FOREIGN KEY (`admin`) REFERENCES `my_admin` (`user_id_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task`
--

LOCK TABLES `task` WRITE;
/*!40000 ALTER TABLE `task` DISABLE KEYS */;
INSERT INTO `task` VALUES (1,' Amazon Top 50 Bestselling Books_FICTION','Dataset on Amazon\'s Top 50 bestselling books from 2009 to 2019! FICTION only',5,5,1),(2,'Amazon Top 50 Bestselling Books_NONFICTION','Dataset on Amazon\'s Top 50 bestselling books from 2009 to 2019. Non-fiction',4,5,1);
/*!40000 ALTER TABLE `task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task_data_table_schema`
--

DROP TABLE IF EXISTS `task_data_table_schema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `task_data_table_schema` (
  `field_id` int(11) NOT NULL AUTO_INCREMENT,
  `field_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `field_type` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `null_valid` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `task_id_id` int(11) NOT NULL,
  PRIMARY KEY (`field_id`),
  UNIQUE KEY `field_name` (`field_name`),
  KEY `task_data_table_schema_task_id_id_980b3ab4` (`task_id_id`),
  CONSTRAINT `task_data_table_schema_task_id_id_980b3ab4_fk_task_task_id` FOREIGN KEY (`task_id_id`) REFERENCES `task` (`task_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task_data_table_schema`
--

LOCK TABLES `task_data_table_schema` WRITE;
/*!40000 ALTER TABLE `task_data_table_schema` DISABLE KEYS */;
INSERT INTO `task_data_table_schema` VALUES (1,'sold_out','boolean','N',1),(2,'seller','char','Y',2);
/*!40000 ALTER TABLE `task_data_table_schema` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task_schema`
--

DROP TABLE IF EXISTS `task_schema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `task_schema` (
  `task_id_id` int(11) NOT NULL,
  `TaskDataTableName` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `TaskDataTableScheme` varchar(10000) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`task_id_id`),
  CONSTRAINT `task_schema_task_id_id_ef7a2219_fk_task_task_id` FOREIGN KEY (`task_id_id`) REFERENCES `task` (`task_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task_schema`
--

LOCK TABLES `task_schema` WRITE;
/*!40000 ALTER TABLE `task_schema` DISABLE KEYS */;
INSERT INTO `task_schema` VALUES (1,'FICTION','CREATE TABLE FICTION(    BOOK_ID INT NOT NULL AUTO_INCREMENT,    BOOK_NAME VARCHAR(100) NOT NULL,    AUTHOR VARCHAR(100) NOT NULL,    RATING FLOAT NOT NULL,    REVIEWS INT NOT NULL,    PRICE FLOAT NOT NULL,    YEAR DATE NOT NULL,    GENRE VARCHAR(10) NOT NULL,    CHECK (RATING>=0 & RATING <=5),    PRIMARY KEY(BOOK_ID), UNIQUE (BOOK_NAME) )'),(2,'NON_FICTION','CREATE TABLE NON_FICTION(    BOOK_ID INT NOT NULL AUTO_INCREMENT,    BOOK_NAME VARCHAR(100) NOT NULL,    AUTHOR VARCHAR(100) NOT NULL,    RATING FLOAT NOT NULL,    REVIEWS INT NOT NULL,    PRICE FLOAT NOT NULL,    YEAR DATE NOT NULL,    GENRE VARCHAR(10) NOT NULL,    CHECK (RATING>=0 & RATING <=5),    PRIMARY KEY(BOOK_ID), UNIQUE (BOOK_NAME) )');
/*!40000 ALTER TABLE `task_schema` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task_taskdatatable`
--

DROP TABLE IF EXISTS `task_taskdatatable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `task_taskdatatable` (
  `Name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `Scheme` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task_taskdatatable`
--

LOCK TABLES `task_taskdatatable` WRITE;
/*!40000 ALTER TABLE `task_taskdatatable` DISABLE KEYS */;
/*!40000 ALTER TABLE `task_taskdatatable` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-06 20:16:52
