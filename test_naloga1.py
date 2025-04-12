import unittest
import numpy as np
import cv2 as cv
from naloga1 import zmanjsaj_sliko, prestej_piklse_z_barvo_koze, obdelaj_sliko_s_skatlami, doloci_barvo_koze

class TestImageProcessing(unittest.TestCase):
    
    def setUp(self):
        # Setup a dummy image (e.g., 100x100 pixels, white background)
        self.image = np.ones((100, 100, 3), dtype=np.uint8) * 255

    def test_zmanjsaj_sliko(self):
        # Test the image resizing functionality
        resized_image = zmanjsaj_sliko(self.image, 50, 50)
        self.assertEqual(resized_image.shape, (50, 50, 3), 
                         msg="Expected resized image shape to be (50, 50, 3), but got {}".format(resized_image.shape))

    def test_prestej_piklse_z_barvo_koze(self):
        # Test the skin color detection function (assuming skin color is within a certain range)
        skin_color = (100, 150, 100)  # This would be a sample skin color in HSV format
        count = prestej_piklse_z_barvo_koze(self.image, skin_color)
        self.assertIsInstance(count, int, 
                              msg="Expected count to be an integer, but got {}".format(type(count)))

    def test_obdelaj_sliko_s_skatlami(self):
        # Test the image processing with boxes
        processed_image = obdelaj_sliko_s_skatlami(self.image, 10, 10, (100, 150, 100))  # Dummy skin color
        self.assertEqual(processed_image.shape, (100, 100, 3), 
                         msg="Expected processed image shape to be (100, 100, 3), but got {}".format(processed_image.shape))

    def test_doloci_barvo_koze(self):
        # Test skin color detection in a region (dummy region)
        skin_color = doloci_barvo_koze(self.image, (10, 10), (50, 50))
        self.assertIsInstance(skin_color, tuple, 
                              msg="Expected skin color to be a tuple, but got {}".format(type(skin_color)))
        self.assertEqual(len(skin_color), 3, 
                         msg="Expected skin color tuple to have 3 elements, but got a tuple of length {}".format(len(skin_color)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
