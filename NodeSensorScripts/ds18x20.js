

var sensor = require('ds18x20');
var sensorid;


var myVar;

function myFunction() {
    myVar = setInterval(getTemp(), 3000);
}





function getTemp() {



console.log('inside funct');



console.log('inside while loop');


//setTimeout(sensor.loadDriver, 1000);


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




sensor.list(function (err, listOfDeviceIds) {

    console.log('this is sensor.list' , listOfDeviceIds);
    sensorid = listOfDeviceIds;
    console.log('Sensorid = ' , sensorid);

    sensor.get(sensorid, function(err, temp) {
       console.log('this is sensor.get inside sensor.list' , temp)});



});




sensor.getAll(function (err, tempObj) {
    console.log('this is sensor.getAll' , tempObj);
    console.log('this is the error' , err);
});





//sensor.get('28-00000574c791', function (err, temp) {
sensor.get('28-000006e0e2ae' , function(err, temp) {


    console.log('in sensor.get with sensorid = ', sensorid);
    console.log('this is sensor.get', temp);
    console.log('this is the error' , err);
});







}





