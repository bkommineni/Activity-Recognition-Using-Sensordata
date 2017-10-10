var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
var fs = require('fs');

app.use(bodyParser.json());

Sensors = require('./models/sensors');
var db = mongoose.connection.openUri('mongodb://localhost/sensordb');

app.post('/',function(req,res){
    var sensor = req.body;
    Sensors.addSensor(sensor,function(err,sensors){
            if(err){
                throw err;
            }
    });
   res.send('Got JSON from Client and Storing into Database...');
});

app.listen(3000);
console.log('Running on port 3000...');
