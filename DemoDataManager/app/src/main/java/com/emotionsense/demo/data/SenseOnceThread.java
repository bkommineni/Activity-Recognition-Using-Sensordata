package com.emotionsense.demo.data;

import android.app.Activity;
import android.util.Log;
import android.widget.Toast;

import com.ubhave.datahandler.loggertypes.AbstractDataLogger;
import com.ubhave.sensormanager.ESException;
import com.ubhave.sensormanager.ESSensorManager;
import com.ubhave.sensormanager.data.SensorData;
import com.ubhave.sensormanager.sensors.SensorUtils;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class SenseOnceThread extends Thread
{
	private final int sensorType;
	private final Activity resultScreen;
	private final ESSensorManager sensorManager;
	private final AbstractDataLogger logger;
	//private Client clientSocket = null;
	private HttpURLConnection conn = null;
	
	public SenseOnceThread(final Activity resultScreen, final ESSensorManager sensorManager, AbstractDataLogger logger, int sensorType,
							HttpURLConnection conn)
	{
		this.resultScreen = resultScreen;
		this.sensorManager = sensorManager;
		this.logger = logger;
		this.sensorType = sensorType;
		this.conn = conn;
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
			//clientSocket.send("hi server!!!");
			try {
				conn.setDoOutput(true);
				conn.setRequestMethod("POST");
				conn.setRequestProperty("Content-Type", "application/json");

				String input = data.toString();

				OutputStream os = conn.getOutputStream();
				os.write(input.getBytes());
				os.flush();

				if (conn.getResponseCode() != HttpURLConnection.HTTP_CREATED) {
					throw new RuntimeException("Failed : HTTP error code : "
							+ conn.getResponseCode());
				}

				BufferedReader br = new BufferedReader(new InputStreamReader(
						(conn.getInputStream())));

				String output;
				System.out.println("Output from Server .... \n");
				while ((output = br.readLine()) != null) {
					System.out.println(output);
				}
			}
			catch (Exception e)
			{
				e.printStackTrace();
			}
			Log.d("data",data.toString());
			if (data != null)
			{
				logger.logSensorData(data);
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
}
