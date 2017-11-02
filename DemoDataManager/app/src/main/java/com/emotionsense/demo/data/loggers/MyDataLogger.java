package com.emotionsense.demo.data.loggers;

import android.content.Context;
import android.provider.Settings;
import com.ubhave.datahandler.config.DataStorageConfig;
import com.ubhave.datahandler.except.DataHandlerException;
import com.ubhave.datahandler.loggertypes.AbstractDataLogger;
import com.ubhave.datahandler.loggertypes.AbstractStoreOnlyLogger;
import com.ubhave.sensormanager.ESException;

import java.util.ArrayList;

import static com.emotionsense.demo.data.DemoApplication.getContext;

/**
 * Created by bharu on 9/21/17.
 */

public class MyDataLogger  extends AbstractStoreOnlyLogger {

    private static MyDataLogger instance;

    public static AbstractDataLogger getInstance() throws ESException, DataHandlerException
    {
        if (instance == null)
        {
            instance = new MyDataLogger(getContext());
        }
        return instance;
    }

    protected MyDataLogger(Context context) throws DataHandlerException, ESException {
        super(context, DataStorageConfig.STORAGE_TYPE_FILES);
    }

    @Override
    protected String getUniqueUserId() {
        return "user-id";
    }

    @Override
    protected String getDeviceId() {
        return Settings.Secure.getString(getContext().getContentResolver(),
                Settings.Secure.ANDROID_ID);
    }

    @Override
    protected boolean shouldPrintLogMessages() {
        return true;
    }

    @Override
    protected String getEncryptionPassword() {
        return null;
    }

    @Override
    protected String getFileStorageName() {
        return "SensorData";
    }
}
