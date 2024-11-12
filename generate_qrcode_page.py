import os
import streamlit as st
import segno
import time

# definition that creates the qr code

def generate_qrcode(url, dark_colour):
    # if directory does not exist it creates the folder
    directory_path = 'images'
    os.makedirs(directory_path, exist_ok=True)

    qrcode = segno.make_qr(url)
    qrcode.to_pil(scale=10,
                  dark=dark_colour).save("images/qrcode_streamlit.png")


def generate_qrcode_page():
    # place an image
    # you can either download an image, or include the image file path

    st.image("images/waves.jpg")

    # place a title
    st.title("THE QR CODE GENERATOR")

    # place a text input box
    url = st.text_input("Enter the URL you want to encode:")

    # use a colour picker
    dark_colour = st.color_picker("Pick a Colour for the dark squares", "#8569a8")

    button = st.button("Click here to generate")


    if button and url:
       # with a spinner
        with st.spinner("Generate QR Code"):
            time.sleep(1.5)
        generate_qrcode(url, dark_colour)
        st.image("images/qrcode_streamlit.png",
                 caption="My Generated QR Code")
