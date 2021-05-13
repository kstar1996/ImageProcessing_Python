from augmentationlib.mod_gamma_darker import *


def test_gamma_darker():
   gamma_correction_darker("https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg")
   gamma_correction_darker("https://pngimg.com/uploads/mario/mario_PNG53.png")
   gamma_correction_darker("../tests/images/graph.png")
   gamma_correction_darker("../tests/images/quokka.jpg")


test_gamma_darker()