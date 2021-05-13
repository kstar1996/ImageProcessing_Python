from augmentationlib.mod_gamma_brighter import *


def test_gamma_brighter():
    gamma_correction_brighter("https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg")
    gamma_correction_brighter("https://pngimg.com/uploads/mario/mario_PNG53.png")
    gamma_correction_brighter("../tests/images/graph.png")
    gamma_correction_brighter("../tests/images/quokka.jpg")


test_gamma_brighter()
