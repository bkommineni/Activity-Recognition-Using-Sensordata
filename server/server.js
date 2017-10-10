var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
var fs = require('fs');

app.use(bodyParser.json());

Sensors = require('./models/sensors');
var db = mongoose.connection.openUri('mongodb://localhost/activityAnalyzerDB');

//app.get('/',function(req,res){
//    var content = fs.readFileSync("../DemoDataManager/DataCollected/SensorDataJson/Accelerometer/1506055760997.json");
//    var strLines = content.toString().split("\n");
//    for (var i in strLines) {
//      var sensor = JSON.parse(strLines[i]);
//      Sensors.addSensor(sensor,function(err,sensors){
//        if(err){
//            throw err;
//        }
//      });
//    }
//    res.send('Add Data to Database ...');
//});

app.post('/',function(req,res){
    var sensor = req.body;
    Sensors.addSensor(sensor,function(err,sensors){
            if(err){
                throw err;
            }
    });
   res.send('Got JSON from Client and Storing into Database...');
});

app.listen(27118);
console.log('Running on port 27118...');
