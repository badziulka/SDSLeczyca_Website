from PIL import Image
from photologue.image_processors import ThumbnailProcessor

class CustomThumbnailProcessor(ThumbnailProcessor):
    def process_image(self, image, width, height):
        image.thumbnail((width, height), Image.ANTIALIAS)
        return image
