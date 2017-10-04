for filename in
DemoDataManager/DataCollected/SensorDataJson/Accelerometer;
do mongoimport -d activityAnalyzerDB -c $filename;  done