var fs = require("fs");
var content = fs.readFileSync("../DemoDataManager/DataCollected/SensorDataJson/Accelerometer/1506055760997.json");
//console.log("Output Content: \n"+ content);

var igor = content['userid'];
console.log(igor);
//var jsonStr = JSON.stringify(content);;//console.log("Userid:", jsonContent);
