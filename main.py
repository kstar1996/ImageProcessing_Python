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


# read an image file as ndarray
url1_jpg = "https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg"
im1_jpg = np.array(Image.open(requests.get(url1_jpg, stream=True).raw))
# getting extension of image
ext1_jpg = get_ext(url1_jpg)

url2_jpg = "https://upload.wikimedia.org/wikipedia/commons/a/a5/Red_Kitten_01.jpg"
im2_jpg = np.array(Image.open(requests.get(url2_jpg, stream=True).raw))
ext2_jpg = get_ext(url2_jpg)

url1_png = "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png"
im1_png = np.array(Image.open(requests.get(url1_png, stream=True).raw))
ext1_png = get_ext(url1_png)

invert_pixel(im1_png, ext1_png)
color_reduction(im1_png, ext1_png)
mosaic(im1_jpg, im2_jpg, ext1_jpg)
gamma_correction_brighter(im1_jpg, ext1_jpg)
gamma_correction_darker(im1_jpg, ext1_jpg)
trimming(im1_jpg, ext1_jpg, 0, 500, 0, 2000)











