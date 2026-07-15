import streamlit as st
import numpy as np
import pandas as pd

st.title("Geocoding And Reverse Geocoding App")
option=st.radio("Select mode:",["Reverse Geocoding (Lat,Lon ➜ Address","Forward Geocoding(Address ➜ Lat,Lon)"]) # Helps to Select the required feature

from geopy.geocoders import Nominatim # A feature of geopy that has maps

geolocator=Nominatim(user_agent="geopy_operator")  # A name alloted to the geopy

if option== "Reverse Geocoding (Lat,Lon ➜ Address":
    lat=st.text_input("Enter Latitude")
    lon=st.text_input("Enter longitude")

    if st.button("Get address"):
        if lat and lon:
            try:
                lat= float(lat)
                lon= float(lon)
                location=geolocator.reverse((lat,lon))

                if location:
                    st.success(f'address found \n {location.address}')  # Displays the details if the given conditions are satisfied
                else:
                    st.warning("No address available for the latitude or langitude")
            except:
                    st.error("Please enter the correct latitude and longitude") # The code is executed after the try(if required)
        else:
             st.warning("Plaese enter both lat and lon")
else:
    address=st.text_input("Enter the address")

    if st.button("Get coordinates"):
        if address:
            location=geolocator.geocode(address)

            if location:
                st.success(f"Latitude: {location.latitude}")
                st.success(f"Longitude: {location.longitude}")

            else:
                st.error("No coordinates found")

        else:
            st.error("Enter an address to proceed")
