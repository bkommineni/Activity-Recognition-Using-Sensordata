package com.emotionsense.demo.data;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import com.emotionsense.demo.data.loggers.MyDataLogger;
import com.ubhave.datahandler.loggertypes.AbstractDataLogger;
import com.ubhave.sensormanager.ESSensorManager;
import com.ubhave.sensormanager.config.SensorConfig;
import com.ubhave.sensormanager.sensors.SensorUtils;

public class MainActivity extends Activity
{
	private final static String LOG_TAG = "MainActivity";

	private AbstractDataLogger logger;
	private ESSensorManager sensorManager;
    private boolean isSensing = false;
	private SenseOnceThread[] pullThreads;

	// TODO: add push sensors you want to sense from here
	private final int[] pushSensors = {};
	
	 // TODO: add pull sensors you want to sense once from here
	private final int[] pullSensors = {SensorUtils.SENSOR_TYPE_ACCELEROMETER};

	@Override
	protected void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
        Button startStopWalk = (Button) findViewById(R.id.Walk);
        Button startStopRun  = (Button) findViewById(R.id.Run);

		try
		{
			// TODO: change this line of code to change the type of data logger
            logger = MyDataLogger.getInstance();
            //sensorManager = ESSensorManager.getSensorManager(this);
            SensorConfig sensorConfig = new SensorConfig();
            sensorConfig.setParameter("POST_SENSE_SLEEP_LENGTH_MILLIS", 120000L);
            sensorConfig.setParameter("MOTION_SAMPLING_DELAY", 1);
            sensorConfig.setParameter("LOW_PASS_ALPHA", 0.25F);
            sensorConfig.setParameter("MOTION_THRESHOLD", 25);
            sensorManager = ESSensorManager.getSensorManagerWithCustomConfig(this,sensorConfig);
            pullThreads = new SenseOnceThread[pullSensors.length];
            startStopWalk.setOnClickListener(new View.OnClickListener() {
                public void onClick(View view) {
                    if (isSensing)
                    {
                        //stopSensing
                        for (int i = 0; i < pullSensors.length; i++)
                        {
                            pullThreads[i] = new SenseOnceThread(new MainActivity(), sensorManager, logger, pullSensors[i]);
                            Log.d("debug",Integer.toString(pullSensors[i]));
                            System.out.println("pull sensors : " + Integer.toString(pullSensors[i]));
                            pullThreads[i].start();
                        }
                    }
                    else
                    {
                        //startSensing
                        Log.d("debug","starting sensing");
                        for (int i = 0; i < pullSensors.length; i++)
                        {
                            pullThreads[i] = new SenseOnceThread(new MainActivity(), sensorManager, logger, pullSensors[i]);
                            Log.d("debug",Integer.toString(pullSensors[i]));
                            System.out.println("pull sensors : " + Integer.toString(pullSensors[i]));
                            pullThreads[i].startSensing();
                        }
                    }
                    isSensing = !isSensing;
                }
            });

            startStopRun.setOnClickListener(new View.OnClickListener() {
                public void onClick(View view) {
                    if (isSensing)
                    {
                        //stopSensing
                        for (int i = 0; i < pullSensors.length; i++)
                        {
                            pullThreads[i] = new SenseOnceThread(new MainActivity(), sensorManager, logger, pullSensors[i]);
                            Log.d("debug",Integer.toString(pullSensors[i]));
                            System.out.println("pull sensors : " + Integer.toString(pullSensors[i]));
                            pullThreads[i].start();
                        }
                    }
                    else
                    {
                        //startSensing
                        for (int i = 0; i < pullSensors.length; i++)
                        {
                            pullThreads[i] = new SenseOnceThread(new MainActivity(), sensorManager, logger, pullSensors[i]);
                            Log.d("debug",Integer.toString(pullSensors[i]));
                            System.out.println("pull sensors : " + Integer.toString(pullSensors[i]));
                            pullThreads[i].startSensing();
                        }
                    }
                    isSensing = !isSensing;
                }
            });
		}
		catch (Exception e)
		{
			Toast.makeText(this, "" + e.getLocalizedMessage(), Toast.LENGTH_LONG).show();
			Log.d(LOG_TAG, e.getLocalizedMessage());
			e.printStackTrace();
		}
	}

	@Override
	protected void onDestroy() {
		super.onDestroy();
	}
}
