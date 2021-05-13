from augmentationlib.mod_mosaic import *


def test_mosaic():
   mosaic("https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png",
          "https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg")
   mosaic("https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg",
          "https://pngimg.com/uploads/mario/mario_PNG53.png")
   mosaic("../tests/images/graph.png", "../tests/images/quokka.jpg")
   mosaic("https://pngimg.com/uploads/mario/mario_PNG53.png", "../tests/images/graph.png")


test_mosaic()

