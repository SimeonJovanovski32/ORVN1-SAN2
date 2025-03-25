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

def prestej_piklse_z_barvo_koze(slika, barva_koze) -> int:
    '''Prestej število pikslov z barvo kože v škatli.'''
    pass

def doloci_barvo_koze(slika,levo_zgoraj,desno_spodaj) -> tuple:
    '''Ta funkcija se kliče zgolj 1x na prvi sliki iz kamere. 
    Vrne barvo kože v območju ki ga definira oklepajoča škatla (levo_zgoraj, desno_spodaj).
      Način izračuna je prepuščen vaši domišljiji.'''
    pass

if __name__ == '__main__':
    #Pripravi kamero

    #Zajami prvo sliko iz kamere

    #Izračunamo barvo kože na prvi sliki

    #Zajemaj slike iz kamere in jih obdeluj     
    
    #Označi območja (škatle), kjer se nahaja obraz (kako je prepuščeno vaši domišljiji)
        #Vprašanje 1: Kako iz števila pikslov iz vsake škatle določiti celotno območje obraza (Floodfill)?
        #Vprašanje 2: Kako prešteti število ljudi?

        #Kako velikost prebirne škatle vpliva na hitrost algoritma in točnost detekcije? Poigrajte se s parametroma velikost_skatle
        #in ne pozabite, da ni nujno da je škatla kvadratna.
    pass