import os
import time
import openpyxl
from os import path
from tkinter import Tk
from tkinter.filedialog import askopenfilename

from openpyxl import Workbook

Tk().withdraw()
files = askopenfilename()
loc = 'C:/Users/jorda/Documents/getpath.xlsx'


sht_loc_filename = input("Enter sheet loc for file name: ")
sht_loc_extension = input("Enter sheet loc for extension: ")
row = int(input("Input the desired row: "))
column = int(input("Input the desired column: "))
# print(files)




# wbvalue = workBook(loc, files, sht_loc, 2, 1)


def filename(paths):
    pathway = os.path.basename(paths)
    print(f'Full file name: {pathway}')
    return pathway


def file_off_ext(ext):
    path_way = os.path.splitext(ext)[1]
    print(f'File name without extension: {path_way}')
    return path_way


def filesize(file):
    filestats = os.stat(file).st_size
    print(f'File size in Bytes: {filestats} bytes')
    return filestats


def filesize_MB(file):
    file_stats = os.stat(file).st_size
    filestats = file_stats / (1024 * 1024)
    print(f'File size in MegBytes: {filestats} MB')
    return file_stats


def filecreation(file):
    file_date = os.path.getctime(file)
    dates = time.ctime(file_date)
    print(f'Created on: {dates}')
    return dates


datas = filename(files)
extension = file_off_ext(filename(files))
filesize(files)
filesize_MB(files)
filecreation(files)


def workBook(flink, Filename, Extension, data, ext):
    wb_obj = openpyxl.load_workbook(flink)
    sht_obj = wb_obj.active
    xl_filename = sht_obj[f'{Filename}']
    xl_extention = sht_obj[f'{Extension}']
    xl_filename.value = data
    xl_extention.value = ext
    # cell_obj = sht_obj.cell(rows, colums)
    # value = cell_obj.value
    wb_obj.save(flink)
    # print(f'filename: {value}')
    # print(f'wb_obj: {wb_obj}')
    # print(f'sht_obj: {sht_obj}')
    # print(f'cell_obj: {cell_obj}')
    # return


workBook(loc, sht_loc_filename, sht_loc_extension, datas, extension)