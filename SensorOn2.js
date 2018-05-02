var ds18b20 = require('ds18b20');
ds18b20.sensors(function(err, ids) {
  // got sensor IDs ...
});

// ... async call
ds18b20.temperature('10-00080283a977', function(err, value) {
  console.log('Current temperature is', value);
});

// ... or sync call
console.log('Current temperature is' + ds18b20.temperatureSync('10-00080283a977'));

// default parser is the decimal one. You can use the hex one by setting an option
ds18b20.temperature('10-00080283a977', {parser: 'hex'}, function(err, value) {
  console.log('Current temperature is', value);
});

console.log('Current temperature is' + ds18b20.temperatureSync('10-00080283a977', {parser: 'hex'}));
