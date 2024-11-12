import streamlit as st
from decode_qrcode_page import decode_qrcode
from generate_qrcode_page import generate_qrcode

st.set_page_config(
    page_title="QR Code Generator V2",
    page_icon="🎩"
)

options = ['Generate QR Code', 'Decode QR Code', 'About Me']
page_selection = st.sidebar.selectbox("Menu", options)

if page_selection == "Generate QR Code":
    generate_qrcode()
elif page_selection == "Decode QR Code":
    decode_qrcode()
elif page_selection == "About Me":
    st.write("Hi, my name is Jannik")