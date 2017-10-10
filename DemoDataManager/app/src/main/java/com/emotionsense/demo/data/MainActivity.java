package com.emotionsense.demo.data;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.emotionsense.demo.data.loggers.MyDataLogger;
import com.ubhave.datahandler.loggertypes.AbstractDataLogger;
import com.ubhave.sensormanager.ESSensorManager;
import com.ubhave.sensormanager.config.SensorConfig;
import com.ubhave.sensormanager.sensors.SensorUtils;

import org.json.JSONObject;

import Utils.VolleyNetwork;

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

		try
		{
			// TODO: change this line of code to change the type of data logger
            logger = MyDataLogger.getInstance();
            SensorConfig sensorConfig = new SensorConfig();
            sensorConfig.setParameter("POST_SENSE_SLEEP_LENGTH_MILLIS", 120000L);
            sensorConfig.setParameter("MOTION_SAMPLING_DELAY", 1);
            sensorConfig.setParameter("LOW_PASS_ALPHA", 0.25F);
            sensorConfig.setParameter("MOTION_THRESHOLD", 25);
            sensorManager = ESSensorManager.getSensorManagerWithCustomConfig(this,sensorConfig);
            pullThreads = new SenseOnceThread[pullSensors.length];
		}
		catch (Exception e)
		{
			Toast.makeText(this, "" + e.getLocalizedMessage(), Toast.LENGTH_LONG).show();
			Log.d(LOG_TAG, e.getLocalizedMessage());
			e.printStackTrace();
		}
	}

	public void onWalkClick(final View view) throws Exception
    {
        if (isSensing)
        {
            //stopSensing
            for (int i = 0; i < pullSensors.length; i++)
            {
                pullThreads[i] = new SenseOnceThread(this, sensorManager, logger, pullSensors[i]);
                Log.d("debug",Integer.toString(pullSensors[i]));
                System.out.println("pull sensors : " + Integer.toString(pullSensors[i]));
                JSONObject jsonSensorData = pullThreads[i].call();
                jsonSensorData.put("label","walking");
                sendFunction("http://10.0.0.37:3000/",jsonSensorData);
            }
        }
        else
        {
            //startSensing
            Log.d("debug","starting sensing");
            for (int i = 0; i < pullSensors.length; i++)
            {
                pullThreads[i] = new SenseOnceThread(this, sensorManager, logger, pullSensors[i]);
                Log.d("debug",Integer.toString(pullSensors[i]));
                System.out.println("pull sensors : " + Integer.toString(pullSensors[i]));
                pullThreads[i].startSensing();
            }
        }
        isSensing = !isSensing;
    }

    public void onRunClick(final View view) throws Exception
    {
        if (isSensing)
        {
            //stopSensing
            for (int i = 0; i < pullSensors.length; i++)
            {
                pullThreads[i] = new SenseOnceThread(this, sensorManager, logger, pullSensors[i]);
                Log.d("debug",Integer.toString(pullSensors[i]));
                System.out.println("pull sensors : " + Integer.toString(pullSensors[i]));
                JSONObject jsonSensorData = pullThreads[i].call();
                jsonSensorData.put("label","running");
                sendFunction("http://10.0.0.37:3000/",jsonSensorData);
            }
        }
        else
        {
            //startSensing
            for (int i = 0; i < pullSensors.length; i++)
            {
                pullThreads[i] = new SenseOnceThread(this, sensorManager, logger, pullSensors[i]);
                Log.d("debug",Integer.toString(pullSensors[i]));
                System.out.println("pull sensors : " + Integer.toString(pullSensors[i]));
                pullThreads[i].startSensing();
            }
        }
        isSensing = !isSensing;
    }

    private void sendFunction(String url, JSONObject data)
    {
        JsonObjectRequest jsonObjectRequest = getJsonObjectRequest(url, data);
        VolleyNetwork.getInstance(this.getApplicationContext()).addToRequestQueue(jsonObjectRequest);
        Log.d("debug", "In the send Function");
    }

    // Change to JSONObjectRequest to send the JSON Request with the data that we have
    private JsonObjectRequest getJsonObjectRequest(String url, JSONObject data)
    {
        return new JsonObjectRequest
                (Request.Method.POST, url, data, new Response.Listener<JSONObject>() {

                    @Override
                    public void onResponse(JSONObject response) {
                        Toast.makeText(getApplicationContext(), response.toString(), Toast.LENGTH_SHORT).show();
                    }
                }, new Response.ErrorListener() {

                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // TODO Auto-generated method stub
                    }
                });
    }

	@Override
	protected void onDestroy() {
		super.onDestroy();
	}
}
