CREATE SCHEMA `Attendance_Check_Databases` ;
use Attendance_Check_Databases;

CREATE TABLE `tbl_employee` (
  `eid` varchar(10) NOT NULL,
  `name` varchar(40) NOT NULL,
  `phone` varchar(13) NOT NULL,
  `email` varchar(40) NOT NULL,
  PRIMARY KEY (`eid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
insert into tbl_employee(eid,name,phone,email) value ('c01','David','02116468414','adaadsad@gmail.com');
insert into tbl_employee(eid,name,phone,email) value ('c02','Ken','02116468412','asadsad@gmail.com');
insert into tbl_employee(eid,name,phone,email) value ('c03','Tom','02116468415','edasdsadsad@gmail.com');
insert into tbl_employee(eid,name,phone,email) value ('c04','Lucy','02116468464','adas312adsad@gmail.com');
insert into tbl_employee(eid,name,phone,email) value ('c05','Annette','02116448414','adasdswewe@gmail.com');
insert into tbl_employee(eid,name,phone,email) value ('c06','Sinbad','021164611414','ada312adsad@gmail.com');
insert into tbl_employee(eid,name,phone,email) value ('c07','Merve','02116468434','adaqeqeadsad@gmail.com');

CREATE TABLE `tbl_job` (
  `jid` varchar(10) NOT NULL,
  `title` varchar(40) NOT NULL,
  `based_salary` float NOT NULL,
  `from_hour` time NOT NULL,
  `to_hour` time NOT NULL,
  `late_coefficient` float NOT NULL,
  `overtime_coefficient` float NOT NULL,
  PRIMARY KEY (`jid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
CREATE TABLE `tbl_attendance` (
  `eid` varchar(10) NOT NULL,
  `dayy` date NOT NULL,
  `clock_in` time NOT NULL,
  `clock_out` time DEFAULT NULL,
  `paid` float DEFAULT NULL,
  PRIMARY KEY (`eid`,`dayy`,`clock_in`),
  CONSTRAINT `fk_tbl_attendance_1` FOREIGN KEY (`eid`) REFERENCES `tbl_employee` (`eid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `tbl_position` (
  `from_date` date NOT NULL,
  `eid` varchar(10) NOT NULL,
  `jid` varchar(10) NOT NULL,
  PRIMARY KEY (`from_date`,`eid`,`jid`),
  KEY `eid_idx` (`eid`),
  KEY `jid_idx` (`jid`),
  CONSTRAINT `fk_eid` FOREIGN KEY (`eid`) REFERENCES `tbl_employee` (`eid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_jid` FOREIGN KEY (`jid`) REFERENCES `tbl_job` (`jid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `tbl_holiday` (
  `jid` varchar(10) NOT NULL,
  `holiday_month` int NOT NULL,
  `holiday_date` int NOT NULL,
  PRIMARY KEY (`jid`,`holiday_month`,`holiday_date`),
  CONSTRAINT `jid` FOREIGN KEY (`jid`) REFERENCES `tbl_job` (`jid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `tbl_payment` (
  `eid` varchar(10) NOT NULL,
  `salary` float DEFAULT NULL,
  `monthh` int NOT NULL,
  `yearr` int NOT NULL,
  PRIMARY KEY (`eid`,`monthh`,`yearr`),
  CONSTRAINT `tbl_payment_ibfk_1` FOREIGN KEY (`eid`) REFERENCES `tbl_employee` (`eid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;