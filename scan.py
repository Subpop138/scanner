import streamlit as st
from aspose.barcode import barcoderecognition
import pyvin


enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)
    



reader = barcoderecognition.BarCodeReader('picture', barcoderecognition.DecodeType.CODE39)
recognized_results = reader.read_bar_codes()
for barcode in recognized_results:
    print(barcode.code_text)


vin_number = (barcode.code_text) 
vehicle = pyvin.VIN(vin_number)

print ("make = " + (vehicle.Make)) 
print ("model = " + (vehicle.Model)) 
print ("year = " + (vehicle.ModelYear)) 
