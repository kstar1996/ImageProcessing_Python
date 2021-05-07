from PIL import Image


def color_reduction(im, ext):
    # im_32 = im // 32 * 32
    im_128 = im // 128 * 128
    pil_reduction = Image.fromarray(im_128)
    pil_reduction.save('pil_reduction'+ext)
