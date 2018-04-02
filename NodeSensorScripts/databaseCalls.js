const sqlite3 = require('sqlite3').verbose();
var d = new Date();
const getTemp = require('./ds18x20.js');



function insertToDB(){

    let db = new sqlite3.Database('/home/pi/TempSensor/weatherdatabase.db');

    var temp = getTemp.getTempOnInterval();


    // insert one row into the langs table
    db.run(`INSERT INTO time(name) VALUES(?)`, [ d , temp ], function(err) {
    if (err) {
        return console.log(err.message);
    }
    // get the last insert id
    console.log(`A row has been inserted with rowid ${this.lastID}`);
    });

    // close the database connection
    db.close();


}

