var MongoClient = require('mongodb').MongoClient
    , format = require('util').format;

MongoClient.connect('mongodb://127.0.0.1:27017/activityAnalyzerDB', function (err, db) {
  db.collection('Users', function (err, collection) {
          collection.find().toArray(function(err, items) {
             if(err) throw err;
             console.log(items);
         });

     });
     db.collection('sensors', function (err, collection) {
               collection.find().toArray(function(err, items) {
                  if(err) throw err;
                  console.log(items);
              });

          });
    db.close();
});

