var express = require('express');
var bodyParser = require('body-parser');
var app = express();
app.use(bodyParser.json());

app.post('/', function(req, res){
    console.log('POST /');
    console.dir(req.body);
    res.writeHead(200, {'Content-Type': 'application/json'});
    res.end('thanks');
});

app.listen(3000);
