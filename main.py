# from PySide6.QtWidgets import QMainWindow
import pytesseract
import cv2
import os
import re

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PYTESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pytesseract.pytesseract.tesseract_cmd = PYTESSERACT_PATH

img = cv2.imread('./test.png', cv2.IMREAD_COLOR)

res: str = pytesseract.image_to_string(img, config='--psm 6')

def get_page_number(text: str = ''):
    # 페이지 쪽수 추출
    if not text:
        return ''

    get_page_number_compile = re.compile('([0-9]+/[0-9]+)')
    find_number_str: list[str] = get_page_number_compile.findall(text)

    if not find_number_str:
        return ''

    cur_page, all_page = find_number_str[-1].split('/')

    return [cur_page, all_page]


print(get_page_number(res))
