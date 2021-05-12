from PIL import Image
import numpy as np
import requests
from urllib.parse import urlparse
from os.path import splitext


def get_ext(url: str) -> np:
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    if ext == ".png":
        im_png = Image.open(requests.get(url, stream=True).raw)
        im_gray = im_png.convert(mode='L')
        im = np.array(im_gray.convert("RGB"))
    else:
        im_open = Image.open(requests.get(url, stream=True).raw)
        im = np.array(im_open.convert(mode='L'))
    return im


# Good for x-ray or scientific images
def histogram_eq(image_pass: str):

    parsed = (urlparse(image_pass))
    if parsed.scheme is '':
        # convert to grayscale
        im_gray = image_pass.convert(mode='L')
        im = np.array(Image.open(im_gray))
    else:
        im = get_ext(image_pass)

    fn = image_pass.split(".")[len(image_pass.split(".")) - 2]
    filename = fn.split("/")[len(fn.split("/")) - 1]

    # Step 1: Normalized cumulative histogram
    # flatten image array and calculate histogram via binning
    histogram_array = np.bincount(im.flatten(), minlength=256)
    # normalize
    num_pixels = np.sum(histogram_array)
    histogram_array = histogram_array / num_pixels
    # normalized cumulative histogram
    c_histogram_array = np.cumsum(histogram_array)

    # Step 2: Pixel mapping lookup table
    transform_map = np.floor(255 * c_histogram_array).astype(np.uint8)

    # Step 3: Transformation
    # flatten image array into 1D list
    img_list = list(im.flatten())
    # transform pixel values to equalize
    eq_img_list = [transform_map[p] for p in img_list]
    # reshape and write back into img_array
    eq_img_array = np.reshape(np.asarray(eq_img_list), im.shape)

    pil_histogram = Image.fromarray(eq_img_array, mode='L')
    pil_histogram.save(filename+'_blur.jpg')
