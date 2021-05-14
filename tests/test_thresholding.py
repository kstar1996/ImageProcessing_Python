from augmentationlib.mod_thresholding import *


def test_thresholding():
   thresholding("https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg")
   thresholding("https://pngimg.com/uploads/mario/mario_PNG53.png")
   thresholding("../tests/images/graph.png")
   thresholding("../tests/images/quokka.jpg")



test_thresholding()