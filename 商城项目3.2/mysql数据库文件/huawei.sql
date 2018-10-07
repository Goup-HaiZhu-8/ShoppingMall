-- MySQL dump 10.13  Distrib 5.7.23, for Win64 (x86_64)
--
-- Host: localhost    Database: HUAWEI
-- ------------------------------------------------------
-- Server version	5.7.23-log

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
-- Table structure for table `brand`
--

DROP TABLE IF EXISTS `brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `brand` (
  `brand_id` int(5) NOT NULL,
  `bname` char(20) DEFAULT NULL,
  PRIMARY KEY (`brand_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brand`
--

LOCK TABLES `brand` WRITE;
/*!40000 ALTER TABLE `brand` DISABLE KEYS */;
INSERT INTO `brand` VALUES (1,'Apple'),(2,'Vivo'),(3,'HUAWAI'),(4,'MeiZu'),(5,'XiaoMi'),(6,'RongYao');
/*!40000 ALTER TABLE `brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL,
  `email` varchar(128) DEFAULT NULL,
  `nickname` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_customer_nickname` (`nickname`),
  UNIQUE KEY `ix_customer_email` (`email`),
  UNIQUE KEY `ix_customer_user_name` (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods`
--

DROP TABLE IF EXISTS `goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods` (
  `gid` int(5) NOT NULL,
  `gname` char(30) DEFAULT NULL,
  `screen_size` float(3,2) DEFAULT NULL,
  `bettery` int(11) DEFAULT NULL,
  `camera` int(6) DEFAULT NULL,
  `ROM` int(4) DEFAULT NULL,
  `RAM` int(4) DEFAULT NULL,
  `price` float(7,2) DEFAULT NULL,
  `color` char(45) DEFAULT NULL,
  `storage` int(5) DEFAULT NULL,
  PRIMARY KEY (`gid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods`
--

LOCK TABLES `goods` WRITE;
/*!40000 ALTER TABLE `goods` DISABLE KEYS */;
INSERT INTO `goods` VALUES (1,'HUAWEI nova 3i',6.30,3340,2400,128,4,1999.00,'亮黑色 蓝楹紫\r',NULL),(2,'HUAWEI nova 3i',6.30,3340,2400,64,6,2199.00,'亮黑色 蓝楹紫\r',NULL),(3,'HUAWEI nova 3',6.30,3750,2400,64,6,2799.00,'亮黑色 蓝楹紫 浅艾蓝 樱草金 相思红\r',NULL),(4,'HUAWEI nova 3',6.30,3750,2400,128,6,2999.00,'亮黑色 蓝楹紫 浅艾蓝 樱草金 相思红\r',NULL),(5,'华为畅享 8e 青春',5.45,3020,1300,32,2,799.00,'黑色 金色 蓝色\r',NULL),(6,'HUAWEI Mate RS 保时捷设计',6.00,4000,4000,256,6,9999.00,'炫黑 瑞红\r',NULL),(7,'HUAWEI Mate RS 保时捷设计',6.00,4000,4000,512,6,12999.00,'炫黑 瑞红\r',NULL),(8,'华为畅享8e',5.70,3000,1300,32,3,999.00,'黑色 金色 蓝色 粉色\r',NULL),(9,'华为畅享8 Plus',5.93,4000,1600,128,4,1699.00,'黑色 金色 蓝色 粉色\r',NULL),(10,'华为畅享8 Plus',5.93,4000,1600,64,4,1499.00,'黑色 金色 蓝色 粉色\r',NULL),(11,'华为畅享8',5.99,3000,1300,64,4,1299.00,'黑色 金色 蓝色 粉色\r',NULL),(12,'HUAWEI P20 Pro',6.10,4000,4000,128,6,4988.00,'亮黑色 宝石蓝 樱粉红 极光色 极光闪耀 珠光贝母 金棕色 雅黑色\r',NULL),(13,'HUAWEI P20 Pro',6.10,4000,4000,64,6,4488.00,'亮黑色 宝石蓝 樱粉红 极光色 极光闪耀 珠光贝母 金棕色 雅黑色\r',NULL),(14,'HUAWEI P20 Pro',6.10,4000,4000,64,6,4488.00,'亮黑色 宝石蓝 樱粉红 极光色 极光闪耀 珠光贝母 金棕色 雅黑色\r',NULL),(15,'HUAWEI P20',5.80,3400,2400,64,6,3388.00,'亮黑色 宝石蓝 樱粉金 极光色 极光闪耀 珠光贝母\r',NULL),(16,'HUAWEI P20',5.80,3400,2400,128,6,3888.00,'亮黑色 宝石蓝 樱粉金 极光色 极光闪耀 珠光贝母\r',NULL),(17,'HUAWEI nova 3e',5.84,3000,2400,128,4,2199.00,'幻夜黑 克莱因蓝 樱语粉 铂光金\r',NULL),(18,'HUAWEI nova 3e',5.84,3000,2400,64,4,1999.00,'幻夜黑 克莱因蓝 樱语粉 铂光金\r',NULL),(19,'HUAWEI MLA-AL10',5.50,3340,1600,64,4,2399.00,'香槟金\r',NULL),(20,'HUAWEI nova 2s',6.00,3340,2000,64,6,2599.00,'浅艾蓝 银钻灰 曜石黑 樱粉金\r',NULL),(21,'HUAWEI nova 2s',6.00,3340,2000,128,6,2799.00,'浅艾蓝 银钻灰 曜石黑 樱粉金\r',NULL),(22,'HUAWEI Mate 10 保时捷设计',6.00,4000,1200,256,6,8999.00,'钻石黑\r',NULL),(23,'HUAWEI Mate 10 Pro',6.00,4000,1200,128,6,3999.00,'摩卡金 银钻灰 宝石蓝 樱粉红\r',NULL),(24,'HUAWEI Mate 10 Pro',6.00,4000,1200,64,6,3599.00,'摩卡金 银钻灰 宝石蓝 樱粉红\r',NULL),(25,'HUAWEI Mate 10（Ascend Mate）',5.90,4000,1200,128,6,3999.00,'摩卡金 香槟金 亮黑色 樱粉红\r',NULL),(26,'HUAWEI 麦芒6',5.90,3340,1600,64,4,2199.00,'曜石黑 极光蓝\r',NULL);
/*!40000 ALTER TABLE `goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoppingcar`
--

DROP TABLE IF EXISTS `shoppingcar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shoppingcar` (
  `uid` int(5) DEFAULT NULL,
  `gid` int(5) NOT NULL,
  `amount` int(4) DEFAULT NULL,
  KEY `user_goods` (`uid`),
  KEY `sc_gid` (`gid`),
  CONSTRAINT `sc_gid` FOREIGN KEY (`gid`) REFERENCES `goods` (`gid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `user_goods` FOREIGN KEY (`uid`) REFERENCES `customer` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoppingcar`
--

LOCK TABLES `shoppingcar` WRITE;
/*!40000 ALTER TABLE `shoppingcar` DISABLE KEYS */;
INSERT INTO `shoppingcar` VALUES (NULL,1,1),(NULL,2,1);
/*!40000 ALTER TABLE `shoppingcar` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-24 13:57:28
