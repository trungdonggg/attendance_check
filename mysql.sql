use cs311;

CREATE TABLE tbl_employee(
  eid VARCHAR(10) NOT NULL PRIMARY KEY,
  name VARCHAR(40) NOT NULL,
  phone VARCHAR(13) NOT NULL,
  email VARCHAR(40) NOT NULL
);

CREATE TABLE tbl_job( 
jid VARCHAR(10) NOT NULL PRIMARY KEY, 
title VARCHAR(40) NOT NULL,
based_salary DECIMAL(14,3) NOT NULL,
from_hour TIME NOT NULL,
to_hour TIME NOT NULL,
late_coefficient FLOAT NOT NULL,
overtime_coefficient FLOAT NOT NULL
 );
 
 CREATE TABLE tbl_attendance(
  clock_in DATETIME  NOT NULL PRIMARY KEY ,
  clock_out DATETIME  NOT NULL,
  eid VARCHAR(10) NOT NULL,
  FOREIGN KEY (eid) REFERENCES tbl_employee(eid)
);

CREATE TABLE tbl_position(
    from_date DATE NOT NULL PRIMARY KEY ,
    eid VARCHAR(10) NOT NULL ,
    jid VARCHAR(10) NOT NULL,
    FOREIGN KEY (eid) REFERENCES tbl_employee(eid),
    FOREIGN KEY(jid) REFERENCES tbl_job(jid)
);
CREATE TABLE tbl_holiday(
 holiday_date DATE NOT NULL PRIMARY KEY,
 jid VARCHAR(10) NOT NULL,
 FOREIGN KEY (jid) REFERENCES tbl_job(jid)
);

CREATE TABLE tbl_payment(
eid VARCHAR(10) NOT NULL ,
salary DECIMAL(14,3) NOT NULL PRIMARY KEY,
month_year DATE NOT NULL,
FOREIGN KEY (eid) REFERENCES tbl_employee(eid)
);