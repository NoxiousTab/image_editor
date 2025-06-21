import streamlit as st
from editor.uploader import load_image

st.title("Basic Image Editor - Upload Module")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "bmp"])

if uploaded_file:
    try:
        image = load_image(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.success("Image uploaded and verified successfully.")
    except ValueError as e:
        st.error(str(e))
