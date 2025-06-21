import streamlit as st
from editor.uploader import load_image
from editor.resize import resize_image

st.title("Basic Image Editor - Resize Module")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "bmp"])
if uploaded_file:
    try:
        image = load_image(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.success("Image uploaded and verified successfully.")
    except ValueError as e:
        st.error(str(e))
    st.header("Resize Image: ")
    col1, col2 = st.columns(2)
    with col1:
        new_width = st.number_input("Width", min_value=1, value=image.width)
    with col2:
        new_height = st.number_input("Height", min_value=1, value=image.height)

    if st.button("Resize Image"):
        try:
            resized = resize_image(image, new_width, new_height)
            st.image(resized, caption="Resized Image", use_column_width=True)
            st.success("Image resized successfully!")
        except ValueError as e:
            st.error(str(e))

