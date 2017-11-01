package com.emotionsense.demo.data;

import android.app.Activity;
import android.util.Log;
import android.widget.Toast;

import com.ubhave.datahandler.loggertypes.AbstractDataLogger;
import com.ubhave.sensormanager.ESException;
import com.ubhave.sensormanager.ESSensorManager;
import com.ubhave.sensormanager.data.SensorData;
import com.ubhave.sensormanager.sensors.SensorUtils;

import org.json.JSONObject;
import java.util.concurrent.Callable;

public class SenseOnceThread implements Callable<JSONObject>
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

	public void startSensing()
	{
		try
		{
			sensorManager.startSensingData(sensorType);
		}
		catch (ESException e)
		{
			toast(e.getLocalizedMessage());
			e.printStackTrace();
		}
	}

	@Override
	public JSONObject call()
	{
		JSONObject jsonSensorData = null;
		try
		{
			SensorData data = sensorManager.stopSensingData(sensorType);
			Log.d("data",data.toString());
			if (data != null)
			{
				jsonSensorData = logger.getJSONSensorData(data);
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
		return jsonSensorData;
	}
}
