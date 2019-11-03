package com.example.login;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.QueryDocumentSnapshot;
import com.google.firebase.firestore.QuerySnapshot;

public class AccountActivity extends AppCompatActivity {

    String TAG = "MyLog: ";
    String stringOutput;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_account);

        Intent arrive = getIntent();
        Bundle bundle = arrive.getExtras();
        String accountNumber = bundle.get("accountNumber").toString();

        TextView output = findViewById(R.id.balanceOutput);

        FirebaseFirestore db = FirebaseFirestore.getInstance();
        CollectionReference acctsCollection = db.collection("crowd_borrow_accounts");


        try {
            acctsCollection.document(accountNumber).collection("currentBalance").get().addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
                @Override
                public void onComplete(@NonNull Task<QuerySnapshot> task) {
                    if (task.isSuccessful()) {

                        for (QueryDocumentSnapshot document : task.getResult()) {
                            Log.d(TAG, document.getId() + " => " + document.getData().get("amount"));
                            stringOutput = document.getData().get("amount").toString();
                        }

                    } else {
                        Log.w(TAG, "Error getting documents.", task.getException());
                    }
                }
            });
        } catch (Exception e) {
            Context context = getApplicationContext();
            Toast.makeText(context, "No account established", Toast.LENGTH_SHORT).show();
        }

        output.setText(stringOutput);
    }
}
