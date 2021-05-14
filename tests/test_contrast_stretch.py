from augmentationlib.mod_contrast_stretch import *


def test_contrast_stretch():
   contrast_stretch("https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg")
   contrast_stretch("https://pngimg.com/uploads/mario/mario_PNG53.png")
   contrast_stretch("../tests/images/graph.png")
   contrast_stretch("../tests/images/quokka.jpg")


test_contrast_stretch()