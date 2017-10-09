var mongoose = require('mongoose');
var fs = require("fs");

//sensors schema
var sensorsSchema = mongoose.Schema({
    userid:{
        type : String
    },
    deviceid:{
        type : String
    },
    senseStartTime:{
        type : String
    },
    senseStartTimeMillis:{
        type : Number
    },
    dataType:{
        type : String
    },
    xAxis:{
       type : Array
    },
    yAxis:{
         type : Array
    },
    zAxis:{
         type : Array
    },
    sensorTimeStamps:{
         type : Array
    },
    sampleLengthMillis:{
        type : Number
    }
}, { versionKey: false });

var sensors
= module.exports
= mongoose.model('sensors', sensorsSchema);

// get sensors data from mongoDB
module.exports.getSensors = function(callback,limit){
    sensors.find(callback).limit(limit);
}

//add sensors data to MongoDB
module.exports.addSensor = function(sensor,callback){
    sensors.create(sensor,callback);
}



