import pytest
from editor.resize import resize_image
from PIL import Image
from pathlib import Path

@pytest.fixture
def sample_image():
    return Image.open(Path("assets/test_image.jpg"))

def test_resize_both_dimensions(sample_image):
    resized = resize_image(sample_image, width=100, height=50)
    assert resized.size == (100, 50)

def test_resize_only_width(sample_image):
    resized = resize_image(sample_image, width=100, height=None)
    expected_height = int(sample_image.height * (100 / sample_image.width))
    assert resized.size == (100, expected_height)

def test_resize_only_height(sample_image):
    resized = resize_image(sample_image, width=None, height=80)
    expected_width = int(sample_image.width * (80 / sample_image.height))
    assert resized.size == (expected_width, 80)

def test_invalid_dimensions(sample_image):
    with pytest.raises(ValueError):
        resize_image(sample_image, width=0, height=100)

    with pytest.raises(ValueError):
        resize_image(sample_image, width=None, height=None)
