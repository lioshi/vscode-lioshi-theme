"""
theme test
"""

import os

from theme_lib import (
    get_scope_params,
    get_general_params,
    get_general_infos,
    get_color_file_html_new_color,
    get_color_file_html_header,
    get_color_file_html_footer,
    get_closer_color
)
from clint.textui import colored
from palette import Color

THEME_FILE = os.path.dirname(os.path.abspath(__file__))+'/lioshi.tmTheme'

# get colors into lioshi.tmTheme file
# print colored.COLORS

# html color file
COLORS_HTML_FILE = os.path.dirname(os.path.abspath(__file__))+'/colors.html'
COLORS_HTML_FILE_RES = open(COLORS_HTML_FILE, "w")

# html content init
COLORS_HTML_FILE_CONTENT = ""

# general params
GENERAL_PARAMS = get_general_params(THEME_FILE)
GENERAL_INFOS = get_general_infos(THEME_FILE)
COLORS_HTML_FILE_CONTENT = get_color_file_html_header(GENERAL_PARAMS['background'], GENERAL_PARAMS['foreground'], GENERAL_INFOS)

# default colors
THEME_COLORS = [
    "#2d2d2d",
    "#c5c8c6",
    "#CC6666",
    "#DE935F",
    "#F0C674",
    "#B5BD68",
    "#5D968D",
    "#81A2BE",
    "#BE94BB"
]
THEME_COLORS_EXTENDED = list(THEME_COLORS) # create an extended list of colors (more lighters color of THEME_COLORS colors)
COLORS_HTML_FILE_CONTENT += "<p><b>default colors</b></p>"
for theme_color in THEME_COLORS:
    COLORS_HTML_FILE_CONTENT += get_color_file_html_new_color("", theme_color, False)
    amt_list = [0.078, 0.15]
    for amt in amt_list:
        a = Color(theme_color)
        theme_color_lighter = a.lighter(amt).hex
        THEME_COLORS_EXTENDED.append(theme_color_lighter)
        COLORS_HTML_FILE_CONTENT += get_color_file_html_new_color("", theme_color_lighter, False)
    COLORS_HTML_FILE_CONTENT += "<br>"
print THEME_COLORS_EXTENDED

# add scopes
COLORS_HTML_FILE_CONTENT += "<p><b>scope colors</b></p>"
SCOPE_PARAMS = get_scope_params(THEME_FILE)
# print colored.cyan("Scope params")
i = 0
j = 0
for param in SCOPE_PARAMS:
    param = SCOPE_PARAMS[param]
    # print param['scope']

    try:
        # print colored.yellow(param['foreground'])
        scope_color = param['foreground']
        scope_color_closer = get_closer_color(scope_color, THEME_COLORS_EXTENDED)
        if scope_color_closer.lower() != scope_color.lower():
            COLORS_HTML_FILE_CONTENT += get_color_file_html_new_color(param['scope'], scope_color, False)
            COLORS_HTML_FILE_CONTENT += get_color_file_html_new_color(param['scope'], scope_color_closer, True)
            COLORS_HTML_FILE_CONTENT += "<div>&nbsp;</div>"

        i += 1

    except KeyError:
        # print colored.red("no foreground setting")
        j += 1

print colored.cyan(str(i) + " scopes with foreground setting")
print colored.red(str(j) + " scopes without foreground setting")

COLORS_HTML_FILE_CONTENT += get_color_file_html_footer()

COLORS_HTML_FILE_RES.write(COLORS_HTML_FILE_CONTENT)
COLORS_HTML_FILE_RES.close()










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





# THEME_FILE_STRING = open(THEME_FILE, 'r').read()
# 
#
#
# THEME_FILE_COPY = open(THEME_FILE+".copy", "w")
# THEME_FILE_COPY.write(THEME_FILE_STRING)
# THEME_FILE_COPY.close()








