from augmentationlib.mod_gauss_blur import *


def test_blur():
   blur("https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg")
   blur("https://pngimg.com/uploads/mario/mario_PNG53.png")
   blur("../tests/images/graph.png")
   blur("../tests/images/quokka.jpg")


test_blur()