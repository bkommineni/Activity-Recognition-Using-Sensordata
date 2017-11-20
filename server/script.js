ar myArgs = process.argv.slice(2);
var fs = require('fs');
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://127.0.0.1:27017/sensordb";
var query_data_userid;
//console.log(myArgs.length);
if(myArgs.length > 1){
    query_data_userid = {userid : myArgs[1]};
}
else {
    query_data_userid = {};
}
MongoClient.connect(url, function(err, db) {
    switch (myArgs[0]) {
        case 'show':
            db.collection("sensors").find(query_data_userid).toArray(function(err, result) {
                if (err) throw err;
                console.log(result);
                db.close();
            });
            break;
        case 'drop':
            db.listCollections({name: "sensors"}).next(function(err, collinfo) {
                if (collinfo) {
                    db.dropCollection("sensors",function(err, result) {
                        if (err) throw err;
                        console.log(result);
                        console.log("Collection deleted");
                        db.close();
                    });
                }
                else {
                        console.log("Collection does not exist!");
                        db.close();
                }
        });
break;
case 'delete':
db.collection("sensors").find(query_data_userid).toArray(function(err, result) {
    if(result){
        db.collection('sensors').remove(query_data_userid, function(err, result) {
            if (err) throw console.log(err);
            console.log('Delete all records of %s', query_data_userid.userid);
            db.close();
        });
    }else {
        console.log("%s data do not exist!", query_data_userid.userid);
        db.close();
    }
});
    break;
        case 'count':
            db.collection("sensors").find(query_data_userid).toArray(function(err, result) {
                if (err) throw err;
                console.log("Number of data : %d", result.length);
                db.close();
            });
            break;
        case 'export':
            db.collection("sensors").find({}).toArray(function(err, result) {
                if (err) throw err;
                fs.writeFile ("data.json", JSON.stringify(result), function(err) {
                    if (err) throw err;
                    console.log('complete');
                    db.close();
                });
            });
            break;
        default:
            console.log('BYE!');
            db.close();
            break;
    }
});