from augmentation.mod_color_reduction import *
from augmentation.mod_gamma_brighter import *
from augmentation.mod_gamma_darker import *
from augmentation.mod_invert import *
from augmentation.mod_mosaic import *
from augmentation.mod_trimming import *

# read an image file as ndarray
url1 = "https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg"
url2 = "https://upload.wikimedia.org/wikipedia/commons/a/a5/Red_Kitten_01.jpg"
im1 = np.array(Image.open(requests.get(url1, stream=True).raw))
im2 = np.array(Image.open(requests.get(url2, stream=True).raw))


invert_pixel(im1)
color_reduction(im1)
mosaic(im1, im2)
gamma_correction_brighter(im1)
gamma_correction_darker(im1)
trimming(im1, 0, 500, 0, 2000)











