import tkinter
import pywhatkit
import webbrowser
import pyautogui as pa
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pywhatkit import sendwhats_image

Tk().withdraw()


file_path = askopenfilename()

num = "+22962747600"
msg = 'image'
# pa.moveTo(1330, 680, 0.5)
sendwhats_image(num, file_path, msg, 30, False, 25)
pa.moveTo(1330, 680, 0.5)
pa.leftClick()
pa.hotkey('ctrl', 'w')
