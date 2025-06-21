import pytest
from PIL import Image
from editor.rotate_flip import rotate_image, flip_image
from pathlib import Path

@pytest.fixture
def sample_image():
    return Image.open(Path("assets/test_image.jpg"))

def test_rotate_valid_angles(sample_image):
    for angle in [90, 180, 270]:
        rotated = rotate_image(sample_image, angle)
        assert isinstance(rotated, Image.Image)

def test_rotate_invalid_angle(sample_image):
    with pytest.raises(ValueError):
        rotate_image(sample_image, 45)

def test_flip_horizontal(sample_image):
    flipped = flip_image(sample_image, "horizontal")
    assert isinstance(flipped, Image.Image)

def test_flip_vertical(sample_image):
    flipped = flip_image(sample_image, "vertical")
    assert isinstance(flipped, Image.Image)

def test_flip_invalid_mode(sample_image):
    with pytest.raises(ValueError):
        flip_image(sample_image, "diagonal")
