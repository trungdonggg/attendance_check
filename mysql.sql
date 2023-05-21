CREATE SCHEMA `Attendance_Check_Databases` ;
use Attendance_Check_Databases;

CREATE TABLE `tbl_employee` (
  `eid` varchar(10) NOT NULL,
  `name` varchar(40) NOT NULL,
  `phone` varchar(13) NOT NULL,
  `email` varchar(40) NOT NULL,
  PRIMARY KEY (`eid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
  `clock_in` datetime NOT NULL,
  `clock_out` datetime DEFAULT NULL,
  `eid` varchar(10) NOT NULL,
  PRIMARY KEY (`clock_in`,`eid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `tbl_position` (
  `from_date` date NOT NULL,
  `eid` varchar(10) NOT NULL,
  `jid` varchar(10) NOT NULL,
  PRIMARY KEY (`from_date`,`eid`,`jid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `tbl_holiday` (
  `holiday_date` date NOT NULL,
  `jid` varchar(10) NOT NULL,
  PRIMARY KEY (`holiday_date`,`jid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE tbl_payment(
eid VARCHAR(10) NOT NULL ,
salary DECIMAL(14,3) NOT NULL PRIMARY KEY,
month_year DATE NOT NULL,
FOREIGN KEY (eid) REFERENCES tbl_employee(eid)
);