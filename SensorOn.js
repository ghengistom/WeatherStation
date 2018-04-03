var ids2=28-000006e0e2ae;

var ds18b20 = require('ds18b20');
ds18b20.sensors(function(err, ids) {
	  console.log('This is the error msg ' + err);

	  console.log('\nThis is the sensor ids' + ids);

});

console.log('above temperature function');
ds18b20.temperature(ids2, function(err, value){
	console.log('Current temperature is', value);

});


ds18b20.temperature(ids2, {parser: 'hex'}, function(err, value) {
  console.log('Current temperature is', value);

});


console.log('Current temperature is' + ds18b20.temperatureSync(ids2, {parser: 'hex'}));
