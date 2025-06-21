from PIL import Image

def overlay_doodle(base_image: Image.Image, doodle_image: Image.Image) -> Image.Image:
    """
    Combines the doodle (from canvas) on top of the base image.
    """
    if base_image.size != doodle_image.size:
        doodle_image = doodle_image.resize(base_image.size)
    return Image.alpha_composite(base_image.convert("RGBA"), doodle_image.convert("RGBA"))
