from augmentation.mod_color_reduction import *
from augmentation.mod_gamma_brighter import *
from augmentation.mod_gamma_darker import *
from augmentation.mod_invert import *
from augmentation.mod_mosaic import *
from augmentation.mod_trimming import *
from urllib.parse import urlparse
from os.path import splitext


def get_ext(url):
    """Return the filename extension from url, or ''."""
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    return ext  # or ext[1:] if you don't want the leading '.'

# converting png to jpg
# rgb_im = im.convert("RGB")

# read an image file as ndarray
url1_jpg = "https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg"
im1_jpg = np.array(Image.open(requests.get(url1_jpg, stream=True).raw))
# getting extension of image

url2_jpg = "https://upload.wikimedia.org/wikipedia/commons/a/a5/Red_Kitten_01.jpg"
im2_jpg = np.array(Image.open(requests.get(url2_jpg, stream=True).raw))

url1_png = "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png"
im1_png = Image.open(requests.get(url1_png, stream=True).raw)
im1_convert_jpg = np.array(im1_png.convert("RGB"))

invert_pixel(im1_convert_jpg)
color_reduction(im1_convert_jpg)
mosaic(im1_jpg, im2_jpg)
gamma_correction_brighter(im1_jpg)
gamma_correction_darker(im1_jpg)
trimming(im1_jpg, 0, 500, 0, 2000)











