from PIL import Image
from groovis import vision


def test_vision():
    image_1 = Image.open("images/tiger1.jpg")
    image_2 = Image.open("images/tiger2.jpg")

    representation_1 = vision(image_1)
    representation_2 = vision(image_2)

    assert representation_1 == representation_2
