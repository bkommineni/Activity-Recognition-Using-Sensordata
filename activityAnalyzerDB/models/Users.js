var mongoose = require('mongoose');

//Users schema
var usersSchema = mongoose.Schema({
    user_id : {
        type : Number
    },

});

var Users = module.exports = mongoose.model('Users', usersSchema);



module.exports.getUsers = function(callback){
    Users.find(callback);
}

