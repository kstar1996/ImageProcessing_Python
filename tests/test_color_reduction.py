from augmentationlib.mod_color_reduction import *


def test_color_reduction():
   color_reduction("https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg")
   color_reduction("https://pngimg.com/uploads/mario/mario_PNG53.png")
   color_reduction("../tests/images/graph.png")
   color_reduction("../tests/images/quokka.jpg")


test_color_reduction()