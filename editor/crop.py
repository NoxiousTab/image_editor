from PIL import Image

def crop_image(image: Image.Image, left: int, upper: int, right: int, lower: int) -> Image.Image:
    width, height = image.size
    if not (0 <= left < right <= width) or not (0 <= upper < lower <= height):
        raise ValueError("Invalid crop coordinates.")
    return image.crop((left, upper, right, lower))

