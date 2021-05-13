from augmentationlib.mod_histogram_eq import *


def test_histogram_eq():
   histogram_eq("../tests/images/quokka.jpg")
   histogram_eq("https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg")
   histogram_eq("https://pngimg.com/uploads/mario/mario_PNG53.png")
   histogram_eq("../tests/images/graph.png")


test_histogram_eq()