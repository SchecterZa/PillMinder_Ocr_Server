from PIL import Image
import cv2
import pytesseract
import os
import re


def cvtToBw(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.medianBlur(gray, 3)
    rect, bw_image = cv2.threshold(
        blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    filename = './images/ocr/{}.jpg'.format(os.getpid())
    cv2.imwrite(filename, bw_image)
    return filename


def imageToText(image_path):

    tessdata_dir_config = '--tessdata-dir "./langdata"'

    bw_image_path = cvtToBw(image_path)

    text = pytesseract.image_to_string(Image.open(
        bw_image_path), lang='tha+eng', config=tessdata_dir_config)
    os.remove(bw_image_path)
    pattern = re.compile('[^a-zA-Z]')
    return pattern.sub('', text)