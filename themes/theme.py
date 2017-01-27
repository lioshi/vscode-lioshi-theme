"""
theme test
"""

import os

from theme_lib import get_scope_params, get_general_params, get_general_infos, get_color_file_html_new_color, get_color_file_html_header, get_color_file_html_footer
from clint.textui import colored

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
    "#CC6666",
    "#CC7466",
    "#CC8166",
    "#DE935F",
    "#DEA15F",
    "#DEAF5F",
    "#F0C674",
    "#F0D274",
    "#F0DE74",
    "#B5BD68",
    "#92B960",
    "#80BE6A",
    "#5D968D",
    "#5D9196",
    "#7BA4AD",
    "#81A2BE",
    "#8AA6B8",
    "#96A6B3",
    "#BE94BB",
    "#BE94A1",
    "#B88A98"
]
k = 1
COLORS_HTML_FILE_CONTENT += "<p><b>default colors</b></p>"
for theme_color in THEME_COLORS:
    COLORS_HTML_FILE_CONTENT += get_color_file_html_new_color("", theme_color, False)
    if k%3 == 0:
        COLORS_HTML_FILE_CONTENT += "<br>"
    k += 1

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
        COLORS_HTML_FILE_CONTENT += get_color_file_html_new_color(param['scope'], param['foreground'], False)

        # find color most proche
# 
# 
# 
#                    http://hanzratech.in/2015/01/16/color-difference-between-2-colors-using-python.html
# 
# 
# 
# sudo pip install colormath
# Now, lets write the actual code to find the difference between 2 colors.

#  1 from colormath.color_objects import sRGBColor, LabColor
#  2 from colormath.color_conversions import convert_color
#  3 from colormath.color_diff import delta_e_cie2000
#  4 
#  5 # Red Color
#  6 color1_rgb = sRGBColor(1.0, 0.0, 0.0);
#  7 
#  8 # Blue Color
#  9 color2_rgb = sRGBColor(0.0, 0.0, 1.0);
# 10 
# 11 # Convert from RGB to Lab Color Space
# 12 color1_lab = convert_color(color1_rgb, LabColor);
# 13 
# 14 # Convert from RGB to Lab Color Space
# 15 color2_lab = convert_color(color2_rgb, LabColor);
# 16 
# 17 # Find the color difference
# 18 delta_e = delta_e_cie2000(color1_lab, color2_lab);
# 19 
# 20 print "The difference between the 2 color = ", delta_e
# - See more at: http://hanzratech.in/2015/01/16/color-difference-between-2-colors-using-python.html#sthash.Sw8L2WKY.dpuf

        COLORS_HTML_FILE_CONTENT += get_color_file_html_new_color(param['scope'], param['foreground'], True)


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








