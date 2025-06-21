from PIL import Image


def crop_image(image: Image.Image, left: int, upper: int, right: int, lower: int) -> Image.Image:
    if not isinstance(image, Image.Image):
        raise ValueError("Input must be a PIL Image object.")
    if left < 0 or upper < 0 or right > image.width or lower > image.height:
        raise ValueError("Crop coordinates are out of bounds.")
    if left >= right or upper >= lower:
        raise ValueError("Invalid crop box dimensions.")

    return image.crop((left, upper, right, lower))
