from PIL import Image


def invert_pixel(im, ext):
    im_i = 255 - im

    pil_invert = Image.fromarray(im_i)
    pil_invert.save('pil_invert'+ext)

