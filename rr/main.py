from pynput.mouse import Listener
from PIL import Image
import pyautogui
import time

pages = 282
coord = []
# left, top, right, bottom
next_page_btn = (2104, 1757)
def click(x, y, btn, pressed):
  if pressed:
    x, y = int(x), int(y)
    coord.extend([x, y])
    
    if len(coord) == 4:
      return False

def make_capture_rect(coord:list = []):
  return (coord[0], coord[1], coord[2] - coord[0], coord[3] - coord[1])

def image_to_pdf():
  img_list = []
  for i in range(pages):
    img = Image.open(f'./images/{i}.png')
    img_list.append(img.convert('RGB'))
  img_list[0].save('./test.pdf', save_all=True, append_images=img_list[1:])
  
with Listener(on_click=click) as Lis:
  Lis.join()

print(coord)
for i in range(pages):
  print(f'{pages} / {i}')
  pyautogui.screenshot(f'./images/{i}.png', make_capture_rect(coord))
  pyautogui.moveTo(next_page_btn[0], next_page_btn[1])
  pyautogui.click()
  time.sleep(0.3)

image_to_pdf()