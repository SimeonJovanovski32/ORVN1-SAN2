import cv2 as cv
import numpy as np

# Function to resize the image to a specified width and height
def zmanjsaj_sliko(slika, sirina, visina):
    return cv.resize(slika, (sirina, visina))  # Resize the image using OpenCV


# Function to process the image with boxes (detect skin in each box)
def obdelaj_sliko_s_skatlami(slika, sirina_skatle, visina_skatle, barva_koze) -> list:
    '''Loop through the image in box sizes (width x height) and calculate the number of skin pixels in each box.'''
    visina, sirina, _ = slika.shape  # Get the image dimensions
    seznam_skatel = []  # List for storing information about boxes
    
    # Loop through the image and split it into smaller boxes
    for y in range(0, visina - visina_skatle, visina_skatle):
        for x in range(0, sirina - sirina_skatle, sirina_skatle):
            # Crop the section of the image that represents one box
            skatelni_del = slika[y:y + visina_skatle, x:x + sirina_skatle]
            
            # Count the skin pixels in this box
            pikseli_koze = prestej_piklse_z_barvo_koze(skatelni_del, barva_koze)
            
            # If there are skin pixels in this box (more than 0), draw a red rectangle
            if pikseli_koze > 0:
                # Draw a rectangle around the box
                cv.rectangle(slika, (x, y), (x + sirina_skatle, y + visina_skatle), (0, 0, 255), 2)
    
    return slika

# Function to count the number of skin-colored pixels in an image
def prestej_piklse_z_barvo_koze(slika, barva_koze) -> int:
    '''Count the number of skin-colored pixels in the image'''
    # Convert the image to HSV color space (Hue, Saturation, Value)
    hsv_slika = cv.cvtColor(slika, cv.COLOR_BGR2HSV)
    
    # Define the lower and upper boundaries for skin color in HSV space
    spodnja_meja = np.array([0, 10, 130], dtype=np.uint8)  # Lower boundary for skin
    zgornja_meja = np.array([20, 150,255], dtype=np.uint8)  # Upper boundary for skin
    
    # Create a mask that highlights areas matching the skin color
    maska = cv.inRange(hsv_slika, spodnja_meja, zgornja_meja)
    
    # Count the pixels that are "skin" (those that are in the mask)
    pikseli_koze = cv.countNonZero(maska)
    
    return pikseli_koze

# Function to determine the skin color in a specified region
def doloci_barvo_koze(slika, levo_zgoraj, desno_spodaj) -> tuple:
    '''Returns the skin color in the area defined by the bounding box.'''
    # Crop the region from the image where we want to determine the skin color
    regija = slika[levo_zgoraj[1]:desno_spodaj[1], levo_zgoraj[0]:desno_spodaj[0]]
    
    # Convert the selected region to HSV color space
    hsv_regija = cv.cvtColor(regija, cv.COLOR_BGR2HSV)
    
    # Calculate the average HSV values in the selected region
    povprecje_hsv = np.mean(hsv_regija, axis=(0, 1))
    
    return tuple(povprecje_hsv)  # Return the average HSV values as a tuple

if __name__ == '__main__':
    # Initialize the camera
    kamera = cv.VideoCapture(0)
    
    # Check if the camera opened successfully
    if not kamera.isOpened():
        print('Camera was not opened.')
    else:
        barva_koze = None  # Initialize the skin color variable to None
        
        while True:
            # Capture an image from the camera
            ret, slika = kamera.read()
            if not ret:
                print("Unable to capture image.")
                break
            
            # Display the image in the "Camera" window
            cv.imshow('Camera', slika)
            
            # Resize the image for processing (if necessary)
            slika_zmanjsana = zmanjsaj_sliko(slika, 640, 480)
            
            # Determine the skin color (by pressing 'd')
            if cv.waitKey(1) & 0xFF == ord('d'):  # Press 'd' to determine the skin color
                barva_koze = doloci_barvo_koze(slika_zmanjsana, (100, 100), (200, 200))  # Determine the skin color in this region
                print("Skin color:", barva_koze)  # Print the determined skin color
            
            # If the skin color is determined, process the image with rectangles
            if barva_koze is not None:
                slika_z_obrobami = obdelaj_sliko_s_skatlami(slika_zmanjsana, 50, 50, barva_koze)
                # Display the image with the rectangles
                cv.imshow('Image with rectangles', slika_z_obrobami)
        
            # If we press the 'q' key, close the window
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        
        # When done, release the camera and close all windows
        kamera.release()
        cv.destroyAllWindows()