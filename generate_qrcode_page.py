import streamlit as st
import segno
import time

def generate_qrcode():
    url = st.text_input("Enter the URL you want to encode:")

    def generate_qrcode(url):
        qrcode = segno.make_qr(url)
        qrcode.save("images/qrcode_streamlit.png",
                    scale=5)

    if url:
        with st.spinner("Generate QR Code"):
            time.sleep(3)
        generate_qrcode(url)
        st.image("images/qrcode_streamlit.png")

    st.markdown("Made by Jannik Stahl")