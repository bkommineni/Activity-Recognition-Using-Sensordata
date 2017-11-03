var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
var fs = require('fs');

app.use(bodyParser.json({limit:'50mb'}));

Sensors = require('./models/sensors');
var db = mongoose.connection.openUri('mongodb://localhost/sensordb');

app.post('/',function(req,res){
    var sensor = req.body;
    console.log('Request recevied');
    Sensors.addSensor(sensor,function(err,sensors){
            if(err){
                throw err;
            }
    });
   res.send('Got JSON from Client and Storing into Database...');
});

app.listen(9998);
console.log('Running on port 9998...');
