from io import BytesIO
from PIL import Image
from django.core.files import File


def compress(image):
    im = Image.open(image)
    basewidth = 900
    width_percent = (basewidth / float(im.size[0]))
    height_size = int(((im.size[1]) * float(width_percent)))
    im = im.resize( (basewidth, height_size), Image.ANTIALIAS)
    # create a BytesIO object
    im_io = BytesIO()
    # save image to BytesIO object
    im.save(im_io, 'JPEG', quality=70)
    # create a django-friendly Files object
    new_image = File(im_io, name=image.name)
    return new_image