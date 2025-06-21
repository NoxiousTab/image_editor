import pytest
from PIL import Image
from editor.doodle import overlay_doodle
import numpy as np

def create_blank_image(size=(100, 100), color=(255, 255, 255, 0)):
    return Image.new("RGBA", size, color)

def test_overlay_same_size():
    base = create_blank_image()
    doodle = create_blank_image()
    result = overlay_doodle(base, doodle)
    assert isinstance(result, Image.Image)
    assert result.size == base.size

def test_overlay_different_size():
    base = create_blank_image((200, 200))
    doodle = create_blank_image((100, 100))
    result = overlay_doodle(base, doodle)
    assert result.size == base.size
