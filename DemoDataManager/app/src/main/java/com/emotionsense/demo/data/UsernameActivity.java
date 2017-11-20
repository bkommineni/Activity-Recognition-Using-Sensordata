package com.emotionsense.demo.data;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;


public class UsernameActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_username);
//        final String username = String.valueOf(editText.getText());
        final Button button = (Button) findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Code here executes on main thread after user presses button
                Intent intent = new Intent(getApplicationContext(), MainActivity.class);
                EditText editText = (EditText) findViewById(R.id.editText);
                String username = editText.getText().toString();
                if(TextUtils.isEmpty(username)) {
                    editText.setError("Username cannot be empty");
                    return;
                }
                Log.d("Username", username);
                intent.putExtra("USERNAME", username);
                startActivity(intent);            }
        });
    }
}
