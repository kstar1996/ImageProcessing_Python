from augmentationlib.mod_invert import *


def test_invert():
   invert_pixel("https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg")
   invert_pixel("https://pngimg.com/uploads/mario/mario_PNG53.png")
   invert_pixel("../tests/images/graph.png")
   invert_pixel("../tests/images/quokka.jpg")


test_invert()