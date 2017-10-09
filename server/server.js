var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
var fs = require('fs');

Sensors = require('./models/sensors');
// Connect to Mongoose
//mongoose.connect('mongodb://localhost/backend');
var db = mongoose.connection.openUri('mongodb://localhost/activityAnalyzerDB');

app.get('/',function(req,res){
    var content = fs.readFileSync("../DemoDataManager/DataCollected/SensorDataJson/Accelerometer/1506055760997.json");
    var strLines = content.toString().split("\n");
    for (var i in strLines) {
      var sensor = JSON.parse(strLines[i]);
      Sensors.addSensor(sensor,function(err,sensors){
        if(err){
            throw err;
        }
      });
    }
    res.send('Add Data to Database ...');
});

app.get('/getsensors',function(req,res){
    res.send('Sensor Data from Database ...');
    Sensors.getSensors(function(err,sensors){
       if(err){
        throw err;
       }
       res.json(sensors);
    });
});


app.listen(27118);
console.log('Running on port 27118...');
