from PIL import Image


def color_image(image: Image.Image, color: str) -> Image.Image:
    if not isinstance(image, Image.Image):
        raise ValueError("Input must be a PIL Image object.")

    allowed_colors = ['red', 'green', 'blue', 'black', 'white']
    if color.lower() not in allowed_colors:
        raise ValueError(f"Color must be one of: {', '.join(allowed_colors)}")

    colored_image = Image.new('RGB', image.size, color=color.lower())

    blended_image = Image.blend(image.convert('RGB'), colored_image, alpha=0.5)

    return blended_image
