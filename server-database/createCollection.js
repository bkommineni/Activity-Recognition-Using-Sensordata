var MongoClient = require('mongodb').MongoClient
    , format = require('util').format;

MongoClient.connect('mongodb://127.0.0.1:27017/activityAnalyzerDB', function (err, db) {
    db.collection('Users', function (err, collection) {
        collection.insert({ user_id: 1, device_id: 'Steve', application_id: 'Jobs' });
        db.collection('Users').count(function (err, count) {
            if (err) throw err;

            console.log('Total Rows: ' + count);
        });
    });

    db.close();
});

