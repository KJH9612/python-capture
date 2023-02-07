# from PySide6.QtWidgets import QMainWindow
import pytesseract
import cv2
import os
import re
from view.MainWindow import MainWindow
from PySide6.QtWidgets import QApplication
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PYTESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = PYTESSERACT_PATH


def get_img_to_mat(path: str = ''):
  if not os.path.isfile(path):
    raise FileNotFoundError

  return cv2.imread(path, cv2.IMREAD_COLOR)

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


if __name__ == "__main__":
  # img = get_img_to_mat('./test.png')
  # res: str = pytesseract.image_to_string(img, config='--psm 6')

  # print(get_page_number(res))
  app = QApplication()
  main_window = MainWindow()
  main_window.show()
  app.exec()