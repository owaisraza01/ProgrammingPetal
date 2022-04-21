#Importing the libraries
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#Opening the image with open-cv
image = cv2.imread('capture.PNG')
#Extracting text from image
st = pytesseract.image_to_string(image)
#Printing the text
print(st)