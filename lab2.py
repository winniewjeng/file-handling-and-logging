import sys, os, argparse, platform, logging, re

LOG_FILENAME = 'lab2.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

logging.debug('This message should go to the log file')