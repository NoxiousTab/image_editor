import pytest
from editor.uploader import load_image
from pathlib import Path

def test_load_valid_image():
    test_path = Path("assets/test_image.jpg")
    with open(test_path, "rb") as f:
        image = load_image(f)
        assert image.size[0] > 0 and image.size[1] > 0

def test_load_invalid_image():
    from io import BytesIO
    fake_file = BytesIO(b"not an image")
    with pytest.raises(ValueError, match="Invalid image file"):
        load_image(fake_file)

def test_no_image_uploaded():
    with pytest.raises(ValueError, match="No file uploaded"):
        load_image(None)
