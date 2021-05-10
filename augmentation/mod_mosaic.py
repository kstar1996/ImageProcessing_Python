import numpy as np
from PIL import Image


def mosaic(im1, im2):
    # match to the bigger image
    height1 = im1.shape[0]
    height2 = im2.shape[0]

    if height1>height2:
        im1_slice = im1[:height2, :]
        im_mosa = np.concatenate((im1_slice, im2), axis=1)

        pil_mosaic = Image.fromarray(im_mosa)
        pil_mosaic.save('pil_mosaic.jpg')
    elif height1<height2:
        im2_slice = im2[:height1, :]
        im_mosa = np.concatenate((im1, im2_slice), axis=1)

        pil_mosaic = Image.fromarray(im_mosa)
        pil_mosaic.save('pil_mosaic.jpg')
    else:
        im_mosa = np.concatenate((im1, im2), axis=1)
        pil_mosaic = Image.fromarray(im_mosa)
        pil_mosaic.save('pil_mosaic.jpg')