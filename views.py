from email.mime import image
import os
import sys
import pytesseract
import cv2
import requests
from urllib.parse import unquote
from flask import request

IMAGEPATH = "data"

def read_ocr():
    content = request.json
    image = content['image']
    lang = content['lang']
    # config = content['config']
    custom_config = r'--oem 3 --psm 6'
    response = requests.get(image)
    image_name = unquote(os.path.basename(image))
    image_path = os.path.join(IMAGEPATH, image_name)
    with open(image_path, 'wb') as file:
        file.write(response.content)
    img_arr = cv2.imread(image_path)
    text = pytesseract.image_to_string(img_arr, lang=lang, config=custom_config)
    if os.path.isfile(image_path):
        os.unlink(image_path)
        text = text.replace("\n", " ")
    return {"text": text}


def root():
    return {"API Documentation": 'http://localhost:4000/swagger/'}
