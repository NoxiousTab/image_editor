import pytest
from PIL import Image
from editor.crop import crop_image
from pathlib import Path

@pytest.fixture
def sample_image():
    return Image.open(Path("assets/test_image.jpg"))

def test_valid_crop(sample_image):
    cropped = crop_image(sample_image, 10, 10, 50, 50)
    assert cropped.size == (40, 40)

def test_invalid_coordinates(sample_image):
    with pytest.raises(ValueError):
        crop_image(sample_image, 50, 10, 10, 50)  # left > right

    with pytest.raises(ValueError):
        crop_image(sample_image, -10, 0, 100, 100)  # negative left

    with pytest.raises(ValueError):
        crop_image(sample_image, 0, 0, sample_image.width + 10, sample_image.height)  # right > width
