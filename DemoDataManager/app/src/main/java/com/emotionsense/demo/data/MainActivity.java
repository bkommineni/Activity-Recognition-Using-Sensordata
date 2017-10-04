package com.emotionsense.demo.data;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.Socket;
import java.net.URL;
import java.net.URLEncoder;
import java.util.List;

import android.app.Activity;
import android.app.DownloadManager;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.VolleyLog;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.emotionsense.demo.data.loggers.AsyncEncryptedFiles;
import com.emotionsense.demo.data.loggers.AsyncWiFiOnlyEncryptedDatabase;
import com.emotionsense.demo.data.loggers.MyDataLogger;
import com.ubhave.datahandler.ESDataManager;
import com.ubhave.datahandler.except.DataHandlerException;
import com.ubhave.datahandler.loggertypes.AbstractDataLogger;
import com.ubhave.datahandler.transfer.DataUploadCallback;
import com.ubhave.sensormanager.ESSensorManager;
import com.ubhave.sensormanager.data.SensorData;
import com.ubhave.sensormanager.sensors.SensorUtils;

import org.json.JSONException;
import org.json.JSONObject;


public class MainActivity extends Activity implements DataUploadCallback
{
	private final static String LOG_TAG = "MainActivity";

	private AbstractDataLogger logger;
	private ESSensorManager sensorManager;
	private SubscribeThread[] subscribeThreads;
	private SenseOnceThread[] pullThreads;
	private HttpURLConnection conn = null;

	//ADD BY SURADA
	String server_url = "http://localhost:9999/";
	private String response = null;
	//Client client = new Client("http://localhost:9999/data",9999);

	// TODO: add push sensors you want to sense from here
	private final int[] pushSensors = {SensorUtils.SENSOR_TYPE_PROXIMITY,
			SensorUtils.SENSOR_TYPE_BATTERY,SensorUtils.SENSOR_TYPE_PHONE_STATE
	};
	
	 // TODO: add pull sensors you want to sense once from here
	private final int[] pullSensors = {SensorUtils.SENSOR_TYPE_ACCELEROMETER,
			 SensorUtils.SENSOR_TYPE_GYROSCOPE,
	         SensorUtils.SENSOR_TYPE_LOCATION,
	         SensorUtils.SENSOR_TYPE_MAGNETIC_FIELD,
			 SensorUtils.SENSOR_TYPE_STEP_COUNTER};

	@Override
	protected void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);

		String Url = "http://10.0.2.2:9999/";

		StringRequest stringRequest = new StringRequest(Request.Method.POST, Url,
				new Response.Listener<String>() {
					@Override
					public void onResponse(String response) {
						Toast.makeText(getApplicationContext(),response,Toast.LENGTH_LONG).show();


					}
				},
				new Response.ErrorListener() {
					@Override
					public void onErrorResponse(VolleyError error) {
						// Handle error
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
		//client.disconnect();
	}
}
