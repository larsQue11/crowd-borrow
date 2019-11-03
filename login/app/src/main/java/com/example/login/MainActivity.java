package com.example.login;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.QueryDocumentSnapshot;
import com.google.firebase.firestore.QuerySnapshot;

public class MainActivity extends AppCompatActivity {

    String TAG = "MyLog: ";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Intent fromLogin = getIntent();
        Bundle bundle = fromLogin.getExtras();
        final String accountNumber = bundle.get("accountNumber").toString();



        Button button1 = findViewById(R.id.balance);
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), AccountActivity.class);
                intent.putExtra("accountNumber",accountNumber);
                startActivity(intent);
            }
        });

        Button button2 = findViewById(R.id.borrowing);
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), BorrowActivity.class);
                intent.putExtra("accountNumber",accountNumber);
                startActivity(intent);
            }
        });

        Button button3 = findViewById(R.id.lending);
        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), LendActivity.class);
                intent.putExtra("accountNumber",accountNumber);
                startActivity(intent);
            }
        });
    }
}
