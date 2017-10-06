var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var mongoose = require('mongoose');

Sensors = require('./models/sensors');
Users = require('./models/Users')
// Connect to Mongoose
//mongoose.connect('mongodb://localhost/backend');
var db = mongoose.connection.openUri('mongodb://localhost/activityAnalyzerDB');

app.get('/',function(req,res){
    res.send('Use1');
});

app.get('/api/sensors',function(req,res){
    Sensors.getSensors(function(err,sensors){
       if(err){
        throw err;
       }
       res.json(sensors);
    });
});

app.get('/api/Users',function(req,res){
    Users.getUsers(function(err,Users){
       if(err){
        throw err;
       }
       res.json(Users);
    });

});
app.listen(27118);
console.log('Running on port 27118...');
