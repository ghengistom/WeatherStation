var ids2;

var ds18b20 = require('ds18b20');
ds18b20.sensors(function(err, ids) {
	  console.log('This is the error msg ' + err);

	  console.log('\nThis is the sensor ids' + ids);
ids2 = ids;
});


ds18b20.temperature(ids2, function(err, value){
	console.log('Current temperature is', value);

});
