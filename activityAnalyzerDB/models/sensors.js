var mongoose = require('mongoose');

//sensors schema

var sensorsSchema = mongoose.Schema({
    userid:{
        type : String
    }
});

var sensors
= module.exports
= mongoose.model('sensors', sensorsSchema);

// get sensors data from mongoDB
module.exports.getSensors = function(callback){
    sensors.find(callback);
}

