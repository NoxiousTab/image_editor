from PIL import Image

def rotate_image(image: Image.Image, angle: int) -> Image.Image:
    if angle not in [90, 180, 270]:
        raise ValueError("Angle must be one of [90, 180, 270]")
    return image.rotate(angle, expand=True)

def flip_image(image: Image.Image, mode: str) -> Image.Image:
    if mode == "horizontal":
        return image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    elif mode == "vertical":
        return image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    else:
        raise ValueError("Mode must be 'horizontal' or 'vertical'")
