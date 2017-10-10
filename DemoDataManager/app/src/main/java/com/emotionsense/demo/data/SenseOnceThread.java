package com.emotionsense.demo.data;

import android.app.Activity;
import android.util.Log;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.ubhave.dataformatter.json.JSONFormatter;
import com.ubhave.datahandler.loggertypes.AbstractDataLogger;
import com.ubhave.sensormanager.ESException;
import com.ubhave.sensormanager.ESSensorManager;
import com.ubhave.sensormanager.data.SensorData;
import com.ubhave.sensormanager.sensors.SensorUtils;

import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

import Utils.VolleyNetwork;

public class SenseOnceThread extends Thread
{
	private final int sensorType;
	private final Activity resultScreen;
	private final ESSensorManager sensorManager;
	private final AbstractDataLogger logger;

	public SenseOnceThread(final Activity resultScreen, final ESSensorManager sensorManager, AbstractDataLogger logger, int sensorType)
	{
		this.resultScreen = resultScreen;
		this.sensorManager = sensorManager;
		this.logger = logger;
		this.sensorType = sensorType;
	}

	private void toast(final String message)
	{
		resultScreen.runOnUiThread(new Runnable()
		{
			@Override
			public void run()
			{
				Toast.makeText(resultScreen, message, Toast.LENGTH_LONG).show();
			}
		});
	}

	@Override
	public void run()
	{
		try
		{
			SensorData data = sensorManager.getDataFromSensor(sensorType);
			Log.d("data",data.toString());
			if (data != null)
			{
				JSONObject jsonSensorData = logger.getJSONSensorData(data);
				sendFunction("http://10.1.50.224:3000/",jsonSensorData);
				System.out.println("json sensor data: " + jsonSensorData.toString());
				toast("Finished sensing.");
				Log.d("Test", "Finished sensing: "+SensorUtils.getSensorName(sensorType));
			}
			else
			{
				toast("Finished sensing: null data");
				Log.d("Test", "Finished sensing: null data");
			}
		}
		catch (ESException e)
		{
			toast(e.getLocalizedMessage());
		}
	}

	private void sendFunction(String url, JSONObject data)
	{
		JsonObjectRequest jsonObjectRequest = getJsonObjectRequest(url, data);
		VolleyNetwork.getInstance(resultScreen.getApplicationContext()).addToRequestQueue(jsonObjectRequest);
		Log.d("debug", "In the send Function");
	}

	// Change to JSONObjectRequest to send the JSON Request with the data that we have
	private JsonObjectRequest getJsonObjectRequest(String url, JSONObject data)
	{
		return new JsonObjectRequest
				(Request.Method.POST, url, data, new Response.Listener<JSONObject>() {

					@Override
					public void onResponse(JSONObject response) {
						Toast.makeText(resultScreen.getApplicationContext(), response.toString(), Toast.LENGTH_SHORT).show();
					}
				}, new Response.ErrorListener() {

					@Override
					public void onErrorResponse(VolleyError error) {
						// TODO Auto-generated method stub
					}
				});
	}

}
