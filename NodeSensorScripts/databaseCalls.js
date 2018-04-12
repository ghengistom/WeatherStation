//const sqlite3 = require('sqlite3').verbose();
var sqlite3 = require('sqlite3').verbose();
var date = new Date();
const getTemp = require('./ds18x20.js');

var time1;
var temp1;

function insertToDB(time1, temp1){

    let db = new sqlite3.Database('/home/pi/TempSensor/weatherdatabase.db');

    var temp1 = getTemp.getTempOnInterval();


    // insert one row into the langs table
    db.run(`INSERT INTO timetemp(time1, temp1) VALUES(?,?)`, [ date , temp1 ], function(err) {
    if (err) {
        return console.log(err.message);
    }
    // get the last insert id
    console.log(`A row has been inserted with rowid ${this.lastID}`);
    });

    // close the database connection
    db.close();


}
