

var sensor = require('ds18x20');
var sensorid;


var myVar;

function getTempOnInterval() {
    setInterval(function(){
            
            sensor.get('28-000006e0e2ae', function (err, temp) {          
              
               if(!err)
               {
                   console.log('The sensor id is:  =  ', sensorid);
                   console.log('The temperature is: ', temp, ' degree celcius.');
                   return temp;
     
               }
               else{
                   console.log('Error for sensor.get is : ', err);
               }
               
            })
    }, 60000);
    
}
   

    sensor.loadDriver(function (err) {
        if (err) console.log('something went wrong loading the driver: ', err)
        else {
            console.log('driver is loaded');
            getTempOnInterval();
        }
    });


    // sensor.list(function (err, listOfDeviceIds) {

    //     console.log('this is sensor.list', listOfDeviceIds);
    //     sensorid = listOfDeviceIds;
    //     console.log('Sensorid = ', sensorid);

    //     sensor.get(sensorid, function (err, temp) {
    //         console.log('this is sensor.get inside sensor.list', temp)
    //     });
    // });

    // sensor.getAll(function (err, tempObj) {
    //     console.log('this is sensor.getAll', tempObj);
    //     console.log('this is the error', err);
    // });

