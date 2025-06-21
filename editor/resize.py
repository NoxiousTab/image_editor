from PIL import Image

def resize_image(image: Image.Image, width: int = None, height: int = None) -> Image.Image:
    if width is None and height is None:
        raise ValueError("At least one of width or height must be provided.")
    original_width, original_height = image.size
    if width is None:
        ratio = height / float(original_height)
        width = int(original_width * ratio)
    elif height is None:
        ratio = width / float(original_width)
        height = int(original_height * ratio)
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers.")
    return image.resize((width, height), Image.Resampling.LANCZOS)
