var myArgs = process.argv.slice(2);
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://127.0.0.1:27017/sensordb";
switch (myArgs[0]) {

        case 'show':
                MongoClient.connect(url, function(err, db) {
                db.collection("sensors").find({}).toArray(function(err, result) {
                if (err) throw err;
                        console.log(result);
                        console.log("Number of data : %d", result.length);
                        db.close();
                });
                });
        break;
        case 'delete':
            MongoClient.connect(url, function(err, db) {
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
        break;

}
