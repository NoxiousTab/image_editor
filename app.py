import streamlit as st
from editor.uploader import load_image
from editor.resize import resize_image
from editor.crop import crop_image
from editor.rotate_flip import rotate_image, flip_image
from streamlit_drawable_canvas import st_canvas
from editor.doodle import overlay_doodle

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
# -- rotate/flip section --
    st.header("🔄 Rotate / Flip Image")

    col1, col2 = st.columns(2)

    with col1:
        angle = st.selectbox("Rotate", options=[None, 90, 180, 270], format_func=lambda x: "None" if x is None else f"{x}°")
        if angle:
            rotated = rotate_image(image, angle)
            st.image(rotated, caption=f"Rotated {angle}°", use_column_width=True)
            st.success("Image rotated successfully.")

    with col2:
        flip_mode = st.selectbox("Flip", options=["None", "horizontal", "vertical"])
        if flip_mode != "None":
            flipped = flip_image(image, flip_mode)
            st.image(flipped, caption=f"Flipped {flip_mode}", use_column_width=True)
            st.success(f"Image flipped {flip_mode}.")
# -- doodle section --
    st.header("✏️ Doodle on Image")

    # Set up canvas
    st.caption("Draw freely on the image using the canvas tool below.")
    canvas_result = st_canvas(
        fill_color="rgba(255, 0, 0, 0.5)",  # Semi-transparent red
        stroke_width=3,
        stroke_color="#000000",
        background_image=image.convert("RGBA"),
        update_streamlit=True,
        height=image.height,
        width=image.width,
        drawing_mode="freedraw",
        key="canvas"
    )

    # If doodles exist, overlay and show
    if canvas_result.image_data is not None:
        from PIL import Image as PILImage
        import numpy as np

        doodle_layer = PILImage.fromarray(canvas_result.image_data.astype("uint8"))
        combined = overlay_doodle(image, doodle_layer)
        st.image(combined, caption="Image with Doodle", use_column_width=True)

