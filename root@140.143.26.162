-- MySQL dump 10.16  Distrib 10.2.15-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: carbrand
-- ------------------------------------------------------
-- Server version	10.2.15-MariaDB

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add country',7,'add_country'),(20,'Can change country',7,'change_country'),(21,'Can delete country',7,'delete_country'),(22,'Can add car brand',8,'add_carbrand'),(23,'Can change car brand',8,'change_carbrand'),(24,'Can delete car brand',8,'delete_carbrand'),(25,'Can add series',9,'add_series'),(26,'Can change series',9,'change_series'),(27,'Can delete series',9,'delete_series');
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
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carbrand_carbrand`
--

DROP TABLE IF EXISTS `carbrand_carbrand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `carbrand_carbrand` (
  `carbrand_id` int(11) NOT NULL,
  `name_cn` varchar(64) NOT NULL,
  `name_en` varchar(128) DEFAULT NULL,
  `img` varchar(1024) DEFAULT NULL,
  `introduction` longtext DEFAULT NULL,
  `website` varchar(512) DEFAULT NULL,
  `ranking` int(11) NOT NULL,
  `level` varchar(32) DEFAULT NULL,
  `country_id` int(11) NOT NULL,
  PRIMARY KEY (`carbrand_id`),
  KEY `carbrand_carbrand_country_id_7963dabd_fk_carbrand_` (`country_id`),
  CONSTRAINT `carbrand_carbrand_country_id_7963dabd_fk_carbrand_` FOREIGN KEY (`country_id`) REFERENCES `carbrand_country` (`country_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carbrand_carbrand`
--

LOCK TABLES `carbrand_carbrand` WRITE;
/*!40000 ALTER TABLE `carbrand_carbrand` DISABLE KEYS */;
INSERT INTO `carbrand_carbrand` VALUES (100001,'大众',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/dazhong.png',NULL,NULL,1,NULL,1000),(100002,'奥迪',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/aodi.png',NULL,NULL,7,NULL,1000),(100003,'宝马',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/baoma.png',NULL,NULL,9,NULL,1000),(100004,'奔驰',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/benchi.png',NULL,NULL,13,NULL,1000),(100005,'保时捷',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/baoshijie.png',NULL,NULL,49,NULL,1000),(100006,'宝沃',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/baowo.png',NULL,NULL,63,NULL,1000),(100007,'smart',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/smart.png',NULL,NULL,80,NULL,1000),(100008,'迈巴赫',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/maibahe.png',NULL,NULL,106,NULL,1000),(100009,'巴博斯',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/babosi.png',NULL,NULL,109,NULL,1000),(100010,'欧宝',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/oubao.png',NULL,NULL,114,NULL,1000),(100011,'ALPINA',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/ALPINA.png',NULL,NULL,129,NULL,1000),(100012,'卡尔森',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/kaersen.png',NULL,NULL,140,NULL,1000),(100013,'威兹曼',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/weiziman.png',NULL,NULL,151,NULL,1000),(100014,'如虎',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/ruhu.png',NULL,NULL,152,NULL,1000),(100015,'泰卡特',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/taikate.png',NULL,NULL,155,NULL,1000),(200001,'丰田',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/fengtian.png',NULL,NULL,2,NULL,2000),(200002,'本田',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/bentian.png',NULL,NULL,4,NULL,2000),(200003,'日产',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/dongfengrichan.png',NULL,NULL,8,NULL,2000),(200004,'马自达',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/mazida.png',NULL,NULL,20,NULL,2000),(200005,'铃木',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/lingmu.png',NULL,NULL,24,NULL,2000),(200006,'三菱',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/sanling.png',NULL,NULL,31,NULL,2000),(200007,'斯巴鲁',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/sibalu.png',NULL,NULL,48,NULL,2000),(200008,'英菲尼迪',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/yingfeinidi.png',NULL,NULL,51,NULL,2000),(200009,'五十铃',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/wushiling.png',NULL,NULL,70,NULL,2000),(200010,'讴歌',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/ouge.png',NULL,NULL,76,NULL,2000),(200011,'Scion',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/Scion.png',NULL,NULL,111,NULL,2000),(200012,'大发',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/dafa.png',NULL,NULL,124,NULL,2000),(200013,'雷克萨斯',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/leikesasi.png',NULL,NULL,40,NULL,2000),(300001,'长安汽车',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/changanqiche.png',NULL,NULL,3,NULL,3000),(300002,'宝骏',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/baojun.png',NULL,NULL,10,NULL,3000),(300003,'哈弗',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/hafu.png',NULL,NULL,15,NULL,3000),(300004,'奇瑞',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/qirui.png',NULL,NULL,17,NULL,3000),(300005,'比亚迪',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/biyadi.png',NULL,NULL,18,NULL,3000),(300006,'广汽传媒',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/guangqichuanmei.png',NULL,NULL,19,NULL,3000),(300007,'荣威',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/rongwei.png',NULL,NULL,23,NULL,3000),(300008,'名爵',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/mingjue.png',NULL,NULL,27,NULL,3000),(300009,'众泰',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/zhongtai.png',NULL,NULL,28,NULL,3000),(300010,'东风风光',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/dongfengfengguang.png',NULL,NULL,32,NULL,3000),(300011,'五菱汽车',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/wulingqiche.png',NULL,NULL,33,NULL,3000),(300012,'东南',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/dongnanqiche.png',NULL,NULL,34,NULL,3000),(300013,'东风风神',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/dongfengfengguang.png',NULL,NULL,36,NULL,3000),(300014,'启辰',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/qichen.png',NULL,NULL,37,NULL,3000),(300015,'奔腾',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/yiqi.png',NULL,NULL,38,NULL,3000),(300016,'WEY',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/wey.png',NULL,NULL,39,NULL,3000),(300018,'江淮',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/jianghuai.png',NULL,NULL,41,NULL,3000),(300019,'长安商用',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/changanshangyong.png',NULL,NULL,42,NULL,3000),(300020,'东风风行',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/dongfengfengguang.png',NULL,NULL,43,NULL,3000),(300021,'海马',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/haima.png',NULL,NULL,44,NULL,3000),(300022,'长城',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/changcheng.png',NULL,NULL,45,NULL,3000),(300023,'一汽',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/yiqi.png',NULL,NULL,46,NULL,3000),(300024,'中华',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/zhonghua.png',NULL,NULL,47,NULL,3000),(300025,'北汽银翔',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/beiqiyinxiang.png',NULL,NULL,54,NULL,3000),(300026,'猎豹汽车',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/liebaoqiche.png',NULL,NULL,55,NULL,3000),(300027,'LYNK&CO',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/lynkco.png',NULL,NULL,56,NULL,3000),(300028,'陆风',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/lufeng.png',NULL,NULL,57,NULL,3000),(300029,'北汽绅宝',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/beiqishenbao.png',NULL,NULL,58,NULL,3000),(300030,'上汽大通',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/shangqidatong.png',NULL,NULL,59,NULL,3000),(300031,'北京',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/beiqishenbao.png',NULL,NULL,60,NULL,3000),(300032,'金杯',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/jinbei.png',NULL,NULL,65,NULL,3000),(300033,'力帆',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/lifan.png',NULL,NULL,66,NULL,3000),(300034,'纳智捷',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/nazhijie.png',NULL,NULL,67,NULL,3000),(300035,'观致',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/guangzhi.png',NULL,NULL,68,NULL,3000),(300036,'比速汽车',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/bisuqiche.png',NULL,NULL,69,NULL,3000),(300037,'江铃驭胜',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/jianglingyusheng.png',NULL,NULL,72,NULL,3000),(300038,'汉腾汽车',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/hantengqiche.png',NULL,NULL,73,NULL,3000),(300039,'华泰汽车',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/huataiqiche.png',NULL,NULL,74,NULL,3000),(300040,'北汽威旺',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/beiqiweiwang.png',NULL,NULL,75,NULL,3000),(300041,'北汽新能源',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/beiqishenbao.png',NULL,NULL,77,NULL,3000),(300042,'福田',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/futian.png',NULL,NULL,81,NULL,3000),(300043,'红旗',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/hongqi.png',NULL,NULL,82,NULL,3000),(300044,'东风',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/dongfengfengguang.png',NULL,NULL,84,NULL,3000),(300045,'黄海',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/huanghai.png',NULL,NULL,85,NULL,3000),(300046,'江铃',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/jiangling.png',NULL,NULL,89,NULL,3000),(300047,'野马汽车',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/yemaqiche.png',NULL,NULL,90,NULL,3000),(300048,'昌河',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/changhe.png',NULL,NULL,91,NULL,3000),(300049,'开瑞',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/kairui.png',NULL,NULL,92,NULL,3000),(300050,'凯翼',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/kaiyi.png',NULL,NULL,93,NULL,3000),(300051,'东风小康',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/dongfengfengguang.png',NULL,NULL,94,NULL,3000),(300052,'莲花汽车',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/lianhuaqiche.png',NULL,NULL,95,NULL,3000),(300053,'理念',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/linian.png',NULL,NULL,98,NULL,3000),(300054,'东风风度',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/dongfengfengguang.png',NULL,NULL,99,NULL,3000),(300055,'知豆',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/zhidou.png',NULL,NULL,100,NULL,3000),(300056,'雷丁',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/leiding.png',NULL,NULL,101,NULL,3000),(300057,'双龙',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/shuanglong.png',NULL,NULL,102,NULL,3000),(300058,'北汽制造',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/beiqizhizao.png',NULL,NULL,103,NULL,3000),(300059,'广汽吉奥',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/guangqijiao.png',NULL,NULL,104,NULL,3000),(300060,'哈飞',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/hafei.png',NULL,NULL,105,NULL,3000),(300061,'瑞麒',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/ruiqi.png',NULL,NULL,107,NULL,3000),(300062,'中兴汽车',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/zhongxingqiche.png',NULL,NULL,110,NULL,3000),(300063,'双环汽车',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/shuanghuan.png',NULL,NULL,112,NULL,3000),(300064,'上海华普',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/shanghaihuapu.png',NULL,NULL,115,NULL,3000),(300065,'福迪',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/fudi.png',NULL,NULL,116,NULL,3000),(300066,'SWM斯威汽车',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/siweiqiche.png',NULL,NULL,117,NULL,3000),(300067,'威麟',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/weiling.png',NULL,NULL,120,NULL,3000),(300068,'欧朗',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/yiqi.png',NULL,NULL,121,NULL,3000),(300069,'英致',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/yingzhi.png',NULL,NULL,123,NULL,3000),(300070,'江铃轻汽',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/jianglingqingqi.png',NULL,NULL,125,NULL,3000),(300071,'蔚来',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/weilai.png',NULL,NULL,130,NULL,3000),(300072,'腾势',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/tengshi.png',NULL,NULL,131,NULL,3000),(300073,'君马汽车',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/junmaqiche.png',NULL,NULL,132,NULL,3000),(300074,'华晨华颂',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/huachenhuasong.png',NULL,NULL,134,NULL,3000),(300075,'海格',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/haige.png',NULL,NULL,135,NULL,3000),(300076,'九龙',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/jiulong.png',NULL,NULL,136,NULL,3000),(300077,'金龙',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/jinlong.png',NULL,NULL,137,NULL,3000),(300078,'永源',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/yongyuan.png',NULL,NULL,138,NULL,3000),(300079,'福汽新龙马',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/fuqixinlongma.png',NULL,NULL,142,NULL,3000),(300080,'卡威',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/kawei.png',NULL,NULL,143,NULL,3000),(300081,'路特斯',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/lutesi.png',NULL,NULL,144,NULL,3000),(300082,'芝诺',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/zhinuo.png',NULL,NULL,145,NULL,3000),(300083,'金旅',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/jinlv.png',NULL,NULL,146,NULL,3000),(300084,'云度新能源',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/yundu.png',NULL,NULL,148,NULL,3000),(300085,'长江汽车',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/changjiang.png',NULL,NULL,156,NULL,3000),(300086,'恒天',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/hengtian.png',NULL,NULL,157,NULL,3000),(300087,'光冈',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/guanggang.png',NULL,NULL,158,NULL,3000),(300088,'康迪',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/kangdi.png',NULL,NULL,160,NULL,3000),(300089,'吉利汽车',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/jiliqiche.png',NULL,NULL,6,NULL,3000),(400001,'别克',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/bieke.png',NULL,NULL,5,NULL,4000),(400002,'福特',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/fute.png',NULL,NULL,12,NULL,4000),(400003,'雪佛兰',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/xuefulan.png',NULL,NULL,16,NULL,4000),(400004,'凯迪拉克',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/kaidilake.png',NULL,NULL,25,NULL,4000),(400005,'Jeep',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/jeep.png',NULL,NULL,30,NULL,4000),(400006,'林肯',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/linken.png',NULL,NULL,52,NULL,4000),(400007,'道奇',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/daoqi.png',NULL,NULL,79,NULL,4000),(400008,'特斯拉',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/tesila.png',NULL,NULL,96,NULL,4000),(400009,'克莱斯勒',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/kelaisile.png',NULL,NULL,97,NULL,4000),(400010,'悍马',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/hanma.png',NULL,NULL,108,NULL,4000),(400011,'GMC',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/gmc.png',NULL,NULL,119,NULL,4000),(400012,'LOCAL MOTORS',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/LOCAL-MOTORS.png',NULL,NULL,150,NULL,4000),(400013,'赛麟',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/sailing.png',NULL,NULL,153,NULL,4000),(500001,'现代',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/xiandai.png',NULL,NULL,11,NULL,5000),(500002,'起亚',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/qiya.png',NULL,NULL,14,NULL,5000),(500003,'SPIRRA',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/SPIRRA.png',NULL,NULL,133,NULL,5000),(600001,'斯柯达',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/sikeda.png',NULL,NULL,21,NULL,6000),(700001,'标致',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/biaozhi.png',NULL,NULL,22,NULL,7000),(700002,'雪铁龙',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/xuetielong.png',NULL,NULL,26,NULL,7000),(700003,'雷诺',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/leinuo.png',NULL,NULL,53,NULL,7000),(700004,'DS',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/ds.png',NULL,NULL,62,NULL,7000),(700005,'布加迪',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/bujiadi.png',NULL,NULL,113,NULL,7000),(800001,'沃尔沃',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/woerwo.png',NULL,NULL,29,NULL,8000),(800002,'科尼赛克',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/kenisaike.png',NULL,NULL,122,NULL,8000),(800003,'萨博',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/sabo.png',NULL,NULL,147,NULL,8000),(900001,'路虎',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/luhu.png',NULL,NULL,35,NULL,9000),(900002,'捷豹',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/jiebao.png',NULL,NULL,50,NULL,9000),(900003,'MINI',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/mini.png',NULL,NULL,64,NULL,9000),(900004,'阿斯顿·马丁',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/asidunmading.png',NULL,NULL,78,NULL,9000),(900005,'宾利',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/binli.png',NULL,NULL,83,NULL,9000),(900006,'劳斯莱斯',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/laosilaisi.png',NULL,NULL,86,NULL,9000),(900007,'迈凯伦',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/maikailun.png',NULL,NULL,118,NULL,9000),(900008,'沃克斯豪尔',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/wokesihaoer.png',NULL,NULL,127,NULL,9000),(900009,'摩根',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/mogen.png',NULL,NULL,154,NULL,9000),(1000001,'菲亚特',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/feiyate.png',NULL,NULL,61,NULL,10000),(1000002,'玛莎拉蒂',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/masaladi.png',NULL,NULL,71,NULL,10000),(1000003,'法拉利',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/falali.png',NULL,NULL,87,NULL,10000),(1000004,'兰博基尼',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/lanbojini.png',NULL,NULL,88,NULL,10000),(1000005,'依维柯',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/yiweike.png',NULL,NULL,128,NULL,10000),(1000006,'帕加尼',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/pajiani.png',NULL,NULL,149,NULL,10000),(1000007,'阿尔法·罗密欧',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/aerfaluomiou.png',NULL,NULL,159,NULL,10000),(1100001,'世爵',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/shijue.png',NULL,NULL,139,NULL,11000),(2000001,'西雅特',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/xiyate.png',NULL,NULL,126,NULL,20000),(2000002,'凯佰赫',NULL,'http://7xj5et.com1.z0.glb.clouddn.com/chepaidaquan/kaibaihe.png',NULL,NULL,141,NULL,20000);
/*!40000 ALTER TABLE `carbrand_carbrand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carbrand_country`
--

DROP TABLE IF EXISTS `carbrand_country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `carbrand_country` (
  `country_id` int(11) NOT NULL,
  `country_name_cn` varchar(128) DEFAULT NULL,
  `country_name_en` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`country_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carbrand_country`
--

LOCK TABLES `carbrand_country` WRITE;
/*!40000 ALTER TABLE `carbrand_country` DISABLE KEYS */;
INSERT INTO `carbrand_country` VALUES (1000,'德国',NULL),(2000,'日本',NULL),(3000,'中国',NULL),(4000,'美国',NULL),(5000,'韩国',NULL),(6000,'捷克',NULL),(7000,'法国',NULL),(8000,'瑞典',NULL),(9000,'英国',NULL),(10000,'意大利',NULL),(11000,'荷兰',NULL),(20000,'其他',NULL);
/*!40000 ALTER TABLE `carbrand_country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carbrand_series`
--

DROP TABLE IF EXISTS `carbrand_series`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `carbrand_series` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `image_url` varchar(1024) DEFAULT NULL,
  `guidence_price` varchar(128) NOT NULL,
  `carbrand_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `carbrand_series_carbrand_id_33e2a912_fk_carbrand_` (`carbrand_id`),
  CONSTRAINT `carbrand_series_carbrand_id_33e2a912_fk_carbrand_` FOREIGN KEY (`carbrand_id`) REFERENCES `carbrand_carbrand` (`carbrand_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carbrand_series`
--

LOCK TABLES `carbrand_series` WRITE;
/*!40000 ALTER TABLE `carbrand_series` DISABLE KEYS */;
/*!40000 ALTER TABLE `carbrand_series` ENABLE KEYS */;
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
  `object_id` longtext DEFAULT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(8,'carbrand','carbrand'),(7,'carbrand','country'),(9,'carbrand','series'),(5,'contenttypes','contenttype'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-06-29 03:02:14.076950'),(2,'auth','0001_initial','2018-06-29 03:02:19.463282'),(3,'admin','0001_initial','2018-06-29 03:02:20.660680'),(4,'admin','0002_logentry_remove_auto_add','2018-06-29 03:02:20.724704'),(5,'contenttypes','0002_remove_content_type_name','2018-06-29 03:02:21.307091'),(6,'auth','0002_alter_permission_name_max_length','2018-06-29 03:02:21.984926'),(7,'auth','0003_alter_user_email_max_length','2018-06-29 03:02:22.902878'),(8,'auth','0004_alter_user_username_opts','2018-06-29 03:02:22.972733'),(9,'auth','0005_alter_user_last_login_null','2018-06-29 03:02:23.246283'),(10,'auth','0006_require_contenttypes_0002','2018-06-29 03:02:23.280191'),(11,'auth','0007_alter_validators_add_error_messages','2018-06-29 03:02:23.333568'),(12,'auth','0008_alter_user_username_max_length','2018-06-29 03:02:23.905441'),(13,'carbrand','0001_initial','2018-06-29 03:02:25.658041'),(14,'sessions','0001_initial','2018-06-29 03:02:26.108256');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-07 12:36:35
