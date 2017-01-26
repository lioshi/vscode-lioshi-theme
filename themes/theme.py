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

# mettre tout ca dans un tableau pour traitement des couleurs

#2d2d2d Background
#393939 Current Line
#515151 Selection
#c5c8c6 Foreground
#666666 Comment
#cc6666 Red
#de935f Orange
#f0c674 Yellow
#b5bd68 Green
#5d968d Aqua
#81a2be Blue
#be94bb Purple





#CC6666
#CC7466
#CC8166

#DE935F
#DEA15F
#DEAF5F

#F0C674
#F0D274
#F0DE74

#B5BD68
#92B960
#69B24F

#5D968D
#5D9196
#5D8599

#81A2BE
#818CBE
#8381BE

#BE94BB
#BE94A1
#BE9D94





# list colors to replace by colrs rgb txt palette






THEME_FILE_COPY = open(THEME_FILE+".copy", "w")
THEME_FILE_COPY.write(THEME_FILE_STRING)
THEME_FILE_COPY.close()








