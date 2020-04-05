#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import pdb
import logging
import traceback
import re
from pathlib import Path


import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook

logger = logging.getLogger('commonWrapper')
logger.addHandler(logging.NullHandler())

gStubFlag = False
myWorkSheetName='output'

def funcWrapper(function):
    from functools import wraps
    @wraps(function)
    def wrapper(*args,**kwargs):
        functionName = function.__name__
        logger.debug(str(functionName) + " with parameters: " +  str(args))

        logger.info(functionName + ' in ...')
        result = function(*args,**kwargs)
        logger.info(functionName + ' out ...')

        if not result:
            sys.exit(1)

    return wrapper


def parseProfitAndPercent(content):
    matchList = []
    rePatternForProfit ='(?<=净利润)([\.\d-]+)(万|亿)(?:[^\.\d-]+)([\.\d-]+)(万|亿)'
    rePatternForPercent='(?:增长|下降)(?:[^\.\d-]*)([\.\d-]+)(%)(?:[^\.\d-]*)([\.\d-]+)(%)'
    rePattern = [ rePatternForProfit, rePatternForPercent]

    if  content is None or type(content) is not str:
                return []

    for searchPatten in rePattern:
        result = re.search(searchPatten,str(content))
        if  result is not None :
            logger.debug(  result.group()  )
            logger.debug(  result.groups() )
            matchList += result.groups()
        else:
             logger.debug('not found ' + searchPatten + ' in ' + str(content))

    return matchList

def getSaveFile(filenameWithPath):

        filePath, filename =  os.path.split(filenameWithPath)
        callName, extension = os.path.splitext(filename)
        saveFile = filePath+"/" + callName + extension
        saveAsFile = filePath+"/" + callName + str(2) + extension
        logger.debug( 'current absolute dir:' + os.path.dirname(os.path.abspath(filenameWithPath)) )
        logger.debug( 'filenameWithPath:' + filenameWithPath)
        logger.debug( 'filePath|name|extension:' + filePath + " " + callName + extension)
        logger.debug( 'Save into the file: ' + saveAsFile)

        return saveFile

def parseAndWriteSheet(workBook,srcSheet):
    logger.debug("max_row : "    + str(srcSheet.max_row))
    logger.debug("max_column : " + str(srcSheet.max_column))

    if  myWorkSheetName in workBook.get_sheet_names():
                workBook.remove_sheet(workBook.get_sheet_by_name(myWorkSheetName))

    #myWorkSheet = workBook.create_sheet(myWorkSheetName)
    myWorkSheet = workBook.copy_worksheet(srcSheet)
    myWorkSheet.title = myWorkSheetName

    myWorkSheet.insert_cols(0, 9)

    #cellRange = srcSheet['F2':'F4']
    dataTitle = ['万元'
                ,'万元'
                ,'%'
                ,'%'
                ,'PE'     #  股票软件上的浮动PE
                ,'JPE1'   #  price*总股本/(历史利润+最近季度利润估算年内剩余利润)
                ,'JPE2'
                ,'WPE1'   #  price*总股本/季度利润1*4
                ,'WPE2'
                ]

    dataOffset =0  # srcSheet.max_column
    for index in range(0,len(dataTitle)):
        column = (index+1) + dataOffset
        myWorkSheet.cell(1,column).value = dataTitle[index]

    offset =0  # srcSheet.max_column
    for row in range(2, srcSheet.max_row):
        content = srcSheet.cell(row,6).value
        matchList = parseProfitAndPercent(content)
        logger.info(matchList)
        for index in range(0,len(matchList)):
            writeColumn = int(index/2+ 1) + offset
            if index % 2 ==0:
                myWorkSheet.cell(row, writeColumn).value=matchList[index]
    return

@funcWrapper
def readExcel(filenameWithPath):
    logger.info("read file: " + filenameWithPath)
    srcFile = Path(filenameWithPath)

    if not srcFile.exists():
        logger.critical("file not exist")
        return
    else:
        #https://www.jianshu.com/p/576c0c6fa3d9

        workBook = load_workbook(filenameWithPath)
        logger.info(workBook.get_sheet_names())
        #current_ws = workBook.active

        sheets = workBook.worksheets
        srcSheet = sheets[0]

        parseAndWriteSheet(workBook,srcSheet )
        workBook.save(getSaveFile(filenameWithPath))
        workBook.close()


@funcWrapper
def create_sheet_cell(nSheet, nCell, filename):
        wb = Workbook()

        for n in range(nSheet):
            wb.create_sheet(index=n, title="Sheet_" + str(n+1))

        currentSheet = wb.active
        for r in range(1, nCell+1):
            for c in range(1, nCell+1):
                 cell = currentSheet.cell(row=r, column=c, value= r * c)

        wb.save(saveFile= "output/" + str(filename))


def create_workbook():
        nSheet = int(input("输入电子表格的个数（整数）："))
        nCell =  int(input("输入乘法表的最大值（整数）："))
        saveFileName =  str(input("最终存储的文件名："))
        create_sheet_cell(nSheet, nCell, saveFileName)


def  debug():
        sys.exit(0)