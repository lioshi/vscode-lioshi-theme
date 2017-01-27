"""
theme test
"""

import os

from theme_lib import get_scope_params, get_color_file_html_new_color, get_color_file_html_header, get_color_file_html_footer
from clint.textui import colored

THEME_FILE = os.path.dirname(os.path.abspath(__file__))+'/lioshi.tmTheme'
THEME_FILE_STRING = open(THEME_FILE, 'r').read()

# get colors into lioshi.tmTheme file

# print colored.COLORS
# sys.exit()


COLORS_HTML_FILE = os.path.dirname(os.path.abspath(__file__))+'/colors.html'
COLORS_HTML_FILE_RES = open(COLORS_HTML_FILE, "w")

COLORS_HTML_FILE_CONTENT = ""

SCOPE_PARAMS = get_scope_params(THEME_FILE)
print colored.cyan("Scope params")
for param in SCOPE_PARAMS:
    param = SCOPE_PARAMS[param]
    print param['scope']

    try:
        if param['scope'] == "general.background":
            print colored.yellow(param['background'])
            COLORS_HTML_FILE_HEADER = get_color_file_html_header(param['background'])
            COLORS_HTML_FILE_CONTENT = COLORS_HTML_FILE_HEADER + COLORS_HTML_FILE_CONTENT

        print colored.yellow(param['foreground'])
        COLORS_HTML_FILE_CONTENT += get_color_file_html_new_color(param['foreground'])

    except KeyError:
        print colored.red("no foreground setting")


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





# 
# THEME_FILE_COPY = open(THEME_FILE+".copy", "w")
# THEME_FILE_COPY.write(THEME_FILE_STRING)
# THEME_FILE_COPY.close()








