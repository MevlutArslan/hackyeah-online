package com.example.shopsafe;


import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.Manifest;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.media.Image;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.util.Random;



public class MainActivity extends AppCompatActivity   {

    TextView usID;
    int usIDint;
    ImageView imageView;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);



        try {
            imageView = findViewById(R.id.imageView2);
            usID = findViewById(R.id.usID);


            SharedPreferences usIDsp = this.getSharedPreferences("com.example.shopsafe", Context.MODE_PRIVATE);

            usIDint = usIDsp.getInt("userID", 0);
            if (usIDint == 0) {
                usIDint = getID();
            }
            usIDsp.edit().putInt("userID", usIDint).apply();


            System.out.println(usIDint);
            usID.setText("User ID: " + usIDint);
            String qrurl = "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data="+usIDint;
            Picasso.get().load(qrurl).into(imageView);



        }catch (Exception e){e.printStackTrace();}
    }

    public void map(View view){

        Intent goToMap = new Intent(this,MapActivity.class);
        startActivity(goToMap);


    }

    public int getID()
    {
        int id;
        Random random = new Random();
        id = random.nextInt(10);
        return id + 1;
    }


    }


