

var sensor = require('ds18x20');
var sensorid;


var myVar;

function myFunction() {
    setInterval(function(){
            
               sensor.get('28-000006e0e2ae', function (err, temp) {
      
               console.log('in sensor.get with sensorid = ', sensorid);
               console.log('this is sensor.get', temp);
               console.log('this is the error', err);
            })
    }, 3000);
    
}

    sensor.loadDriver(function (err) {
        if (err) console.log('something went wrong loading the driver:', err)
        else {
            console.log('driver is loaded');
            myFunction();
        }
    });


    sensor.isDriverLoaded(function (err, isLoaded) {
        console.log('this is sensor.isDriverLoaded', isLoaded);
    });

