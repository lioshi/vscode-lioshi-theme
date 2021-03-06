import asyncio

def showcase():
    """Some code to showcase the syntax.
    HACK doctests are highlighted too.
            >>> print('''hello
        ... world''')
    """
activities = {8: 'Sleeping',
              20: 'Eating',
              22: 'Resting' }
raw_input("Enter an integer from 1 to 99: ")

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print activities[activity_time]

class TestMedian(unittest.TestCase):
    def testMedian(self):
        self.failUnlessEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)

    @decorator(param='spam')
    async def coroutine(db:aio_db.DatabaseConnection) -> List[str]:
        r"""A coroutine.""" 

        await logger.log('working\x12with %r', aio_db)

        async with db.transaction():
            result = await db.query(...)
            print(f'Result: {result!r}')

    mapping = None     # type: Dict[int, Any] # PEP 484
    # a regular expression
    get_regex = lambda: re.compile(     # type: ignore
        r"""\A
            word
            (?:                         # a comment
               (?P<fill>.)?
               (?P<align>[<>=^])        (?# another comment)
            )?
            another word\.\.\.
            (?:\.(?P<precision>0|(?!0)\d+))?
        \Z""",
        re.VERBOSE | re.DOTALL)

    # NOTE Numbers with leading zeros are invalid in Python 3,
    # use 0o...
    answer = func(0xdeadbeef + 0b00100001 + 0123 + 0o123 +
                  1_005_123 + # PEP 515
                  # complex numbers
                  .10e12 + 2j) @ mat

    return R'''No escapes '\' in this \one'''






from time import localtime

activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting' }
raw_input("Enter an integer from 1 to 99: ")
# This is the first attempt 
# type: int
time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print activities[activity_time]
        break
else:
    print 'Unknown, AFK or sleeping!'

Celsius = int(raw_input("Enter a temperature in Celsius: "))

Fahrenheit = 9.0/5.0 * Celsius + 32

print "Temperature:", Celsius, "Celsius = ", Fahrenheit, " F"    

class TestMedian(unittest.TestCase):
    def testMedian(self):
        self.failUnlessEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)

print queens
print "\n".join(". "*q + "Q " + ". "*(BOARD_SIZE-q-1) for q in queens)

import random
n = random.randint(1, 99)
guess = int(raw_input("Enter an integer from 1 to 99: "))
while n != "guess":
    print
    if guess < n:
        print "guess is low"
        guess = int(raw_input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print "guess is high"
        guess = int(raw_input("Enter an integer from 1 to 99: "))
    else:
        print "you guessed it!"
        break
    print


"""
theme test
"""
# pylint: disable=C0301

import os
import datetime
import sys
from shutil import copy

from theme_lib import (
    get_scope_params,
    get_general_params,
    get_general_infos,
    get_color_file_html_new_color,
    get_color_file_html_header,
    get_color_file_html_footer,
    get_closer_color,
    replace_in_file
)
from clint.textui import colored
from palette import Color

if len(sys.argv) > 1:
    ARG1 = sys.argv[1]
else:
    ARG1 = ""

THEME_FILE = os.path.dirname(os.path.abspath(__file__))+'/lioshi.tmTheme'

# copy theme file
FILE_COPY_EXT = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
print colored.green("Save "+ THEME_FILE+" into "+THEME_FILE+"."+FILE_COPY_EXT)
copy(THEME_FILE, THEME_FILE+"."+FILE_COPY_EXT)

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
    "#6C6C6C",
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
    amt_list = [0.12, 0.21]
    for amt in amt_list:
        a = Color(theme_color)
        theme_color_lighter = a.lighter(amt).hex
        THEME_COLORS_EXTENDED.append(theme_color_lighter)
        COLORS_HTML_FILE_CONTENT += get_color_file_html_new_color("", theme_color_lighter, False)
    COLORS_HTML_FILE_CONTENT += "<br>"
# print THEME_COLORS_EXTENDED

# add scopes
COLORS_HTML_FILE_CONTENT += "<p><b>scope colors not in theme's colors extended</b></p>"
SCOPE_PARAMS = get_scope_params(THEME_FILE)
# print colored.cyan("Scope params")
i = 0
j = 0
COLORS_REPLACEMENTS = {}
for param in SCOPE_PARAMS:
    param = SCOPE_PARAMS[param]
    # print param['scope']

    try:
        # print colored.yellow(param['foreground'])
        scope_color = param['foreground']
        scope_color_closer = get_closer_color(scope_color, THEME_COLORS_EXTENDED)
        if scope_color_closer.lower() != scope_color.lower():
            COLORS_REPLACEMENTS[scope_color] = scope_color_closer # repalce colors
            COLORS_HTML_FILE_CONTENT += get_color_file_html_new_color(param['scope'], scope_color, False)
            COLORS_HTML_FILE_CONTENT += get_color_file_html_new_color(param['scope'], scope_color_closer, True)
            COLORS_HTML_FILE_CONTENT += "<div>&nbsp;</div>"
        i += 1

    except KeyError:
        # print colored.red("no foreground setting")
        j += 1

if ARG1 == "replace":
    # replace in tmTheme file
    print colored.cyan("Replace colors into "+ THEME_FILE)
    for old_color in COLORS_REPLACEMENTS:
        print colored.red(old_color)+" -> "+colored.red(COLORS_REPLACEMENTS[old_color])
    replace_in_file(COLORS_REPLACEMENTS, THEME_FILE)

print colored.cyan(str(i) + " scopes with foreground setting")
print colored.red(str(j) + " scopes without foreground setting")

COLORS_HTML_FILE_CONTENT += get_color_file_html_footer()

COLORS_HTML_FILE_RES.write(COLORS_HTML_FILE_CONTENT)
COLORS_HTML_FILE_RES.close()
print colored.cyan("Replace infos into "+ COLORS_HTML_FILE)










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














