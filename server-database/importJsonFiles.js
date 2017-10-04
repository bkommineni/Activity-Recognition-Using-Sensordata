colls=(DemoDataManager/DataCollected/SensorDataJson/Accelerometer)

for c in ${colls[@]}
do
  mongoimport -d mydb -c $c.json
done