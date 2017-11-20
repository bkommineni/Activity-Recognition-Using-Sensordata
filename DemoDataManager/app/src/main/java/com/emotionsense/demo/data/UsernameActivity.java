package com.emotionsense.demo.data;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.widget.EditText;

/**
 * Created by Anjani Bajaj on 11/19/2017.
 *
 */

public class UsernameActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_username);
    }

    public void onSubmitClicked(View view) {
        Intent intent = new Intent(getApplicationContext(), MainActivity.class);
        EditText editText = (EditText) findViewById(R.id.editText);
        String username = editText.getText().toString();
        if(TextUtils.isEmpty(username)) {
            editText.setError("Username cannot be empty");
            return;
        }
        Log.d("UserId", username);
        intent.putExtra("USERID", username);
        startActivity(intent);
    }
}
