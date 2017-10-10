package com.emotionsense.demo.data;

import java.net.HttpURLConnection;
import java.util.List;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.emotionsense.demo.data.loggers.MyDataLogger;
import com.ubhave.datahandler.ESDataManager;
import com.ubhave.datahandler.except.DataHandlerException;
import com.ubhave.datahandler.loggertypes.AbstractDataLogger;
import com.ubhave.datahandler.transfer.DataUploadCallback;
import com.ubhave.sensormanager.ESSensorManager;
import com.ubhave.sensormanager.data.SensorData;
import com.ubhave.sensormanager.sensors.SensorUtils;

import Utils.VolleyNetwork;

public class MainActivity extends Activity implements DataUploadCallback
{
	private final static String LOG_TAG = "MainActivity";

	private AbstractDataLogger logger;
	private ESSensorManager sensorManager;
	
	private SubscribeThread[] subscribeThreads;
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
			sensorManager = ESSensorManager.getSensorManager(this);
//			// Example of starting some sensing in onCreate()
//			// Collect a single sample from the listed pull sensors
			pullThreads = new SenseOnceThread[pullSensors.length];
			for (int i = 0; i < pullSensors.length; i++)
			{
				pullThreads[i] = new SenseOnceThread(this, sensorManager, logger, pullSensors[i]);
				Log.d("debug",Integer.toString(pullSensors[i]));
				System.out.println("pull sensors : " + Integer.toString(pullSensors[i]));
				pullThreads[i].start();
			}
		}
		catch (Exception e)
		{
			Toast.makeText(this, "" + e.getLocalizedMessage(), Toast.LENGTH_LONG).show();
			Log.d(LOG_TAG, e.getLocalizedMessage());
			e.printStackTrace();
		}
		// VolleyNetwork instance to connect to the server.
		sendFunction("http://10.1.50.224:3000/");
	}

	private void sendFunction(String url)
    {
		StringRequest stringRequest = getStringRequest(url);
		VolleyNetwork.getInstance(getApplicationContext()).addToRequestQueue(stringRequest);
	}

	// Change to JSONObjectRequest to send the JSON Request with the data that we have
	private StringRequest getStringRequest(String url)
    {
		return new StringRequest(Request.Method.POST, url,
				new Response.Listener<String>() {
					@Override
					public void onResponse(String response) {
						Toast.makeText(getApplicationContext(), response, Toast.LENGTH_LONG).show();
					}
				}, new Response.ErrorListener() {
			@Override
			public void onErrorResponse(VolleyError error) {
				Toast.makeText(getApplicationContext(),"Connection Error: Cannot reach the server!", Toast.LENGTH_LONG).show();
			}
		});
	}

	@Override
	public void onResume()
	{
		super.onResume();
		
		// Example of starting some sensing in onResume()
		// Collect a single sample from the listed push sensors
		subscribeThreads = new SubscribeThread[pushSensors.length];
		for (int i = 0; i < pushSensors.length; i++)
		{
			subscribeThreads[i] = new SubscribeThread(this, sensorManager, logger, pushSensors[i]);
			subscribeThreads[i].start();
		}
	}

	@Override
	public void onPause()
	{
		super.onPause();
		
		// Don't forget to stop sensing when the app pauses
		for (SubscribeThread thread : subscribeThreads)
		{
			thread.stopSensing();
		}
	}

	public void onSearchClicked(final View view)
	{
		// Counts the number of sensor events from the last 60 seconds
		try
		{
			long startTime = System.currentTimeMillis() - (1000L * 60);
			ESDataManager dataManager = logger.getDataManager();
			
			for (int pushSensor : pushSensors)
			{
				List<SensorData> recentData = dataManager.getRecentSensorData(pushSensor, startTime);
				Toast.makeText(this, "Recent "+SensorUtils.getSensorName(pushSensor)+": " + recentData.size(), Toast.LENGTH_LONG).show();
			}
			
			for (int pushSensor : pullSensors)
			{
				List<SensorData> recentData = dataManager.getRecentSensorData(pushSensor, startTime);
				Toast.makeText(this, "Recent "+SensorUtils.getSensorName(pushSensor)+": " + recentData.size(), Toast.LENGTH_LONG).show();
			}

		}
		catch (Exception e)
		{
			Toast.makeText(this, "Error retrieving sensor data", Toast.LENGTH_LONG).show();
			Log.d(LOG_TAG, e.getLocalizedMessage());
			e.printStackTrace();
		}
	}

	public void onFlushClicked(final View view)
	{
		// Tries to POST all of the stored sensor data to the server
		try
		{
			ESDataManager dataManager = logger.getDataManager();
			dataManager.postAllStoredData(this);
		}
		catch (DataHandlerException e)
		{
			Toast.makeText(this, "Exception: "+e.getLocalizedMessage(), Toast.LENGTH_LONG).show();
			Log.d(LOG_TAG, ""+e.getLocalizedMessage());
		}
	}

	@Override
	public void onDataUploaded()
	{
		runOnUiThread(new Runnable()
		{

			@Override
			public void run()
			{
				// Callback method: the data has been successfully posted
				Toast.makeText(MainActivity.this, "Data transferred.", Toast.LENGTH_LONG).show();
			}
		});
	}
	
	@Override
	public void onDataUploadFailed()
	{
		runOnUiThread(new Runnable()
		{

			@Override
			public void run()
			{
				// Callback method: the data has not been successfully posted
				Toast.makeText(MainActivity.this, "Error transferring data", Toast.LENGTH_LONG).show();
			}
		});
	}

	@Override
	protected void onDestroy() {
		super.onDestroy();
	}
}
