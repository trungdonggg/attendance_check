const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const fs = require('fs');
const ejs = require('ejs')
// read config file
const configdata = fs.readFileSync('/home/long/attendance_check/conf/config.json','utf-8');
const config = JSON.parse(configdata);

const mysql = require('mysql');

// connect with mysql database
const connection = mysql.createConnection({
  host: config.host,
  user: config.user,
  password:config.password,
  database:config.database
});

app.use(bodyParser.urlencoded({ extended: true }));

app.set('view engine','ejs');

app.get('/',function(req,res){
  res.send('hey!');
});

// app.get('/employee', (req, res) => {

//   connection.query('SELECT * FROM tbl_employee', (err,rows) => {
//     if (err) throw err;
//     res.render('index',{tbl_employee: rows});
//   });
// });

app.listen(3000, () => {
  console.log('Server started on port 3000');
});

