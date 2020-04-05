package com.example.shopsafe;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.provider.Settings;
import android.view.View;
import android.widget.TextView;

import java.net.URL;

public class StoreDetails extends AppCompatActivity {

    TextView strID;
    TextView details;
    TextView qno;
    String storeId;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_store_details);
        strID = findViewById(R.id.storeID);
        details = findViewById(R.id.details);
        Intent intent = getIntent();
        String storeID = intent.getStringExtra("storeid");
        String ophr = intent.getStringExtra("ophr");
        String clshr = intent.getStringExtra("clshr");
        long noOC = intent.getLongExtra("noOC",0);
        long noOE = intent.getLongExtra("noOE",0);
        storeId = intent.getStringExtra("storeId");
        System.out.println(storeId);
        strID.setText(storeID);
        details.setText("Opening Hour: "+ ophr + "\n "+"Closing Hour: "+clshr+"\n"+"Number Of Cashier x"+noOC+ "\n" +"Number Of Employees: "+noOE+"\n"+"Last time Sanitized: 12:38  "+"\n"+"Number Of People Inside: 7");
    }

public void getQueue(View view){

    String url = "http://127.0.0.1:5000/addToQue/";
    String storeid = storeId ;
    String personId = Settings.Secure.getString(getContentResolver(),Settings.Secure.ANDROID_ID);
    String finalUrl = url += storeid + "/" + personId;

    //call api and return result
    String qrCodeUrl = "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=";
    String finalQrUrl = qrCodeUrl += "/" + personId;

    }
public void shiftQue(View view){
        String url = "http://127.0.0.1:5000/shiftQue/";
        String storeid = storeId ;
        String personId = Settings.Secure.getString(getContentResolver(),Settings.Secure.ANDROID_ID);
        String finalUrl = url += storeid + "/" + personId;

}
public void getQueueNo(View view){
        qno = findViewById(R.id.queueno);
        int queueNo = 0 ;//buraya queue numarasini yazalim

        qno.setText("Your Queue number is: "+ queueNo);


}



}
