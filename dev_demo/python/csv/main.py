#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import requests
import configparser
import argparse
import logging
import traceback
from  logging import config
from os import path
import re

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
        parser = argparse.ArgumentParser()
        parser.add_argument("-op","--targetOperation",  nargs='+', type=str, choices=['dataWash'], required=True,
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
                targetOperation = args.targetOperation[0]
                if targetOperation == 'dataWash':
                        logger.info("read file: " + args.filename[0])

                else:
                        logger.error("unexpect operation...")

        except KeyboardInterrupt:
                logger.error('KeyboardInterrupt')

        except Exception as e:
                logger.critical('Exception is catched')
                logger.critical(traceback.logger.info_exc())

if __name__ == '__main__':
        loadLoggingFile(['csv', 'conf', 'bin'], 'logging.conf' )
        operationHandler( argumentParser())