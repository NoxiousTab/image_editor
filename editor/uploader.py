from PIL import Image
import io

def load_image(uploaded_file):
    if uploaded_file is None:
        raise ValueError("No file uploaded.")
    try:
        image = Image.open(uploaded_file)
        image.verify()
        uploaded_file.seek(0)
        return Image.open(uploaded_file)
    except Exception as e:
        raise ValueError(f"Invalid image file: {e}")
