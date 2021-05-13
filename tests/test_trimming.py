from augmentationlib.mod_trimming import *


def test_trimming():
   trimming("https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg")
   trimming("https://pngimg.com/uploads/mario/mario_PNG53.png")
   trimming("../tests/images/graph.png")
   trimming("../tests/images/quokka.jpg")


test_trimming()
