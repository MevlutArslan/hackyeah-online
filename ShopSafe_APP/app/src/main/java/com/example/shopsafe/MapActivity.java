package com.example.shopsafe;

import androidx.annotation.NonNull;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.fragment.app.FragmentActivity;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.widget.Toast;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.FirebaseApp;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.GeoPoint;
import com.google.firebase.firestore.QueryDocumentSnapshot;
import com.google.firebase.firestore.QuerySnapshot;

import java.util.ArrayList;

public class MapActivity extends FragmentActivity implements OnMapReadyCallback, GoogleMap.OnMarkerClickListener {

    ArrayList<Store> stores = new ArrayList<Store>();
    public GoogleMap mMap;
    String storeName;




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_map);
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);



        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
                requestPermissions(new String[]{Manifest.permission.ACCESS_FINE_LOCATION,Manifest.permission.ACCESS_FINE_LOCATION,Manifest.permission.INTERNET}
                        ,10);
            }
        }





    }


    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;
        FirebaseApp.initializeApp(this);
        final FirebaseFirestore db = FirebaseFirestore.getInstance();
        CollectionReference dbRef = db.collection("Stores");




        dbRef.get().addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
            @Override
            public void onComplete(@NonNull Task<QuerySnapshot> task) {
                if(task.isSuccessful()) {
                    for (QueryDocumentSnapshot document : task.getResult()) {
                        String documentId = (String) document.getId();
                        System.out.println(documentId);
                        String storeName = (String) document.getData().get("storename");
                        String openH = (String) document.getData().get("openingHour");
                        String closeH = (String) document.getData().get("closingHour");
                        GeoPoint geo = (GeoPoint) document.getData().get("location");
                        long noOC = (long) document.getData().get("numberOfCashiers");
                        long noOE = (long) document.getData().get("numberOfEmployees");

                        stores.add(new Store(documentId,storeName,openH,closeH,geo,noOC,noOE));

                    }

                }


                for (int i = 0; i<stores.size();i++){
                double lat = stores.get(i).geoPoint.getLatitude();
                double lng = stores.get(i).geoPoint.getLongitude();
                String storename = stores.get(i).storeName;
                LatLng latLng = new LatLng(lat,lng);
                Marker marker = mMap.addMarker(new MarkerOptions().position(latLng).title(storename));
                marker.setTag(stores.get(i));
            }
        }
        });

        mMap.setOnMarkerClickListener(this);
    }


    @Override
    public boolean onMarkerClick(Marker marker) {

        Store store = (Store)marker.getTag();
        Intent intent = new Intent(this,StoreDetails.class);
        storeName = marker.getTitle();
        intent.putExtra("storeid",storeName);
        intent.putExtra("ophr",store.openingHour);
        intent.putExtra("clshr",store.ClosingHour);
        intent.putExtra("noOC",store.noOfCashiers);
        intent.putExtra("noOE",store.noOfEmployees);
        intent.putExtra("storeId",store.storeId);




        startActivity(intent);




        return false;
    }


}

        class Store{
        String storeName;
        String openingHour;
        String ClosingHour;
        GeoPoint geoPoint;
        long noOfCashiers;
        long noOfEmployees;
        String storeId;




        public Store(String storeId, String storeName, String openingHour, String closingHour, GeoPoint geoPoint, long noOfCashiers, long noOfEmployees) {
            this.storeName = storeName;
            this.openingHour = openingHour;
            ClosingHour = closingHour;
            this.geoPoint = geoPoint;
            this.noOfCashiers = noOfCashiers;
            this.noOfEmployees = noOfEmployees;
            this.storeId = storeId;

        }

            @Override
            public String toString() {
                return "Store{" +
                        "storeName='" + storeName + '\'' +
                        ", openingHour='" + openingHour + '\'' +
                        ", ClosingHour='" + ClosingHour + '\'' +
                        ", geoPoint=" + geoPoint +
                        ", noOfCashiers=" + noOfCashiers +
                        ", noOfEmployees=" + noOfEmployees + '\'' +
                        '}';
            }
        }

