
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
time_from TIME NOT NULL,
time_to TIME NOT NULL,
late_coefficient FLOAT NOT NULL,
overtime_coefficient FLOAT NOT NULL
 );
CREATE TABLE tbl_attendance(
  time_from DATETIME  NOT NULL PRIMARY KEY ,
  time_to DATETIME  NOT NULL,
  em_id VARCHAR(10) NOT NULL,
FOREIGN KEY (em_id) REFERENCES tbl_employee(em_id)

);

CREATE TABLE tbl_position(
    fromDate DATE NOT NULL PRIMARY KEY ,
    em_id VARCHAR(10) NOT NULL ,
    j_id VARCHAR(10) NOT NULL,
    FOREIGN KEY (em_id) REFERENCES tbl_employee(em_id),
    FOREIGN KEY(j_id) REFERENCES tbl_job(j_id)
);
CREATE TABLE tbl_holiday(
 holiday_date DATE NOT NULL PRIMARY KEY,
 j_id VARCHAR(10) NOT NULL,
FOREIGN KEY (j_id) REFERENCES tbl_job(j_id)
);

CREATE TABLE tbl_payment(
e_id VARCHAR(10) NOT NULL ,
salary DECIMAL(14,3) NOT NULL PRIMARY KEY,
month_year DATE NOT NULL PRIMARY KEY,
FOREIGN KEY (e_id) REFERENCES tbl_employee(e_id)
);