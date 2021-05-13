from augmentationlib.mod_rotate import *


def test_rotate():
    rotate("https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg")
    rotate("https://pngimg.com/uploads/mario/mario_PNG53.png")
    rotate("../tests/images/graph.png")
    rotate("../tests/images/quokka.jpg")


test_rotate()