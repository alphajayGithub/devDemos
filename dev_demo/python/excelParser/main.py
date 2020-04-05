#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import configparser
import argparse
import logging
import traceback
from  logging import config
from os import path
from libexcel import commonWrapper

'''
#有关Excel
2007版之前的excel文件后缀为.xls，最大支持65535行数据，xlrd和xlwt主要应用于07版之前的Excel文件。
      xlrd(excel  read)可以用来读取.xls和.xlsx文件，
      xlwt(excel write)写文件只支持.xls，所以对数据的大小有限制
2017版之后的excel文件后缀为.xlsx, 最大支持1048576行，使用openpyxl来弥补xlwt的缺陷来处理大文件。

OpenPyXL的官网参考：
https://openpyxl.readthedocs.io/en/latest/usage.html
https://openpyxl.readthedocs.io/en/stable/
'''


logger = logging.getLogger('APP')
gStubFlag = False

def loadLoggingFile(loggingConfSearchList, filename):
        logging_conf_file = path.join(path.dirname(path.abspath(__file__)), filename)
        logger.info( 'current dir:' + path.dirname(path.abspath(__file__)) )
        logger.info( 'search  dir:' + path.abspath('.') )

        for element in loggingConfSearchList:
                loggingParentDir = path.join(path.abspath('.'), element)
                if path.exists( loggingParentDir ):
                        logging_conf_file = path.join(loggingParentDir, filename )
                        if path.isfile(logging_conf_file):
                                logger.info('found logging_conf_file: ' + logging_conf_file )
                                break
                else:
                        logger.info('not found logging_conf_file: ' + loggingParentDir )

        logging.config.fileConfig(logging_conf_file)
        logger.debug('import logging_conf_file: ' + logging_conf_file)
        logger.info("------------> Startup <------------")


def argumentParser():
        logger.debug("Total " + str(len(sys.argv))  + " parameter: " +  str(sys.argv))

        parser = argparse.ArgumentParser()
        parser.add_argument("-op","--targetOperation",  nargs='+', type=str, choices=['dataWash'],
                                                        help="what do you want to do?", default='dataWash')

        parser.add_argument("-outdir","--saveDir",      nargs='+', type=str,
                                                        help="directs all output files to a specific directory", default='.')\

        parser.add_argument("-debug","--debugMode",     action='store_true',
                                                        help="stub mode")

        parser.add_argument("-f","--filename", nargs='+', type=str, help="the csv file you need to wash data", required=True,
                                    default='all')

        return parser.parse_args()

def operationHandler(args):
        if (args.debugMode):
                logger.critical("Debug mode enable")
                gStubFlag = args.debugMode

        try:
                targetOperation = args.targetOperation
                if targetOperation == 'dataWash':
                        filename = args.filename[0]
                        commonWrapper.readExcel(filename)
                else:
                        logger.error("unexpect operation...")

        except KeyboardInterrupt:
                logger.error('KeyboardInterrupt')

        except Exception as e:
                logger.critical('Exception is catched')
                logger.critical(traceback.print_exc())

if __name__ == '__main__':
        loadLoggingFile(['csv', 'conf', 'bin'], 'logging.conf' )
        operationHandler( argumentParser())