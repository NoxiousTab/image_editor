import streamlit as st
from editor.uploader import load_image
from editor.resize import resize_image
from editor.crop import crop_image
st.title("Basic Image Editor - Resize Module")
uploaded_file = st.file_uploader("Upload an image", type=[
                                 "jpg", "jpeg", "png", "bmp"])
if uploaded_file:
    try:
        image = load_image(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.success("Image uploaded and verified successfully.")
    except ValueError as e:
        st.error(str(e))
# --resize section--
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

# --crop section--
    st.header("Crop Image: ")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        left = st.number_input("Left", min_value=0,
                               max_value=image.width - 1, value=0)
    with c2:
        right = st.number_input("Right", min_value=1,
                                max_value=image.width, value=image.width)
    with c3:
        upper = st.number_input("Upper", min_value=0,
                                max_value=image.height - 1, value=0)
    with c4:
        lower = st.number_input("Lower", min_value=1,
                                max_value=image.height, value=image.height)

    if st.button("Crop Image"):
        try:
            cropped = crop_image(image, left, upper, right, lower)
            st.image(cropped, caption="Cropped Image", use_column_width=True)
            st.success("Image cropped successfully!")
        except ValueError as e:
            st.error(str(e))
