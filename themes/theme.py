"""
theme test
"""

import os
import sys
from lxml import etree
from clint.textui import colored

THEME_FILE = os.path.dirname(os.path.abspath(__file__))+'/lioshi.tmTheme'
THEME_FILE_STRING = open(THEME_FILE, 'r').read()

# get colors into lioshi.tmTheme file


# print colored.COLORS
# sys.exit()

TREE = etree.parse(THEME_FILE)
for dictA in TREE.xpath("dict/array/dict/key"):
    if dictA.text == "scope":
        scope = dictA.getnext()
        print colored.yellow("scope")+" "+scope.text
    if dictA.text == "settings":
        dictB = dictA.getnext()
        for settings in list(dictB):
            if settings.text == "foreground":
                foreground = settings.getnext()
                print colored.cyan("foreground")+" "+foreground.text
            if settings.text == "background":
                background = settings.getnext()
                print colored.cyan("background")+" "+background.text
        print "\n"






# list colors to replace by colrs rgb txt palette






THEME_FILE_COPY = open(THEME_FILE+".copy", "w")
THEME_FILE_COPY.write(THEME_FILE_STRING)
THEME_FILE_COPY.close()








