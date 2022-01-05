from PIL import Image,ImageGrab
import pyocr.builders
import pyocr
import os
import pyperclip
import pyautogui
N=6
#0 =方向およびスクリプト検出（OSD）のみ。
#1 = OSDによる自動ページセグメンテーション。
#2 =自動ページセグメンテーション、ただしOSDまたはOCRなし
#3 =完全自動のページセグメンテーション。ただし、OSDはありません。 （デフォルト）
#4 =可変サイズのテキストの単一列を想定します。
#5 =垂直に配置されたテキストの単一の均一なブロックを想定します。
#6 =単一の均一なテキストブロックを想定します。
#7 =画像を単一のテキスト行として扱います。
#8 =画像を1つの単語として扱います。
#9 =画像を円の中の1つの単語として扱います。
#10 =画像を単一の文字として扱います。
clipimage=ImageGrab.grabclipboard()
if clipimage!=None:
    path_tesseract = 'C:\Program Files\Tesseract-OCR'
    if path_tesseract not in os.environ["PATH"].split(os.pathsep):
        os.environ["PATH"] += os.pathsep + path_tesseract
    tools = pyocr.get_available_tools()
    tool = tools[0]
    builder = pyocr.builders.TextBuilder(tesseract_layout=N)
    text = tool.image_to_string(clipimage, lang="eng",builder=builder)
    pyperclip.copy(text)
else:
    pyautogui.hotkey("win","shift","s")
