'''
lib of theme
'''

from lxml import etree
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

def get_closer_color(color, list_colors):
    """ get closer color of a color in a color list"""
    color_rgb = sRGBColor.new_from_rgb_hex(color)
    color_lab = convert_color(color_rgb, LabColor)
    closer_color_delta = 100
    closer_color = color
    for list_color in list_colors:
        list_color_rgb = sRGBColor.new_from_rgb_hex(list_color)
        list_color_lab = convert_color(list_color_rgb, LabColor)
        # Find the color difference
        delta_e = delta_e_cie2000(color_lab, list_color_lab)
        # print "The difference between the ", color, " and ", list_color, " = ", delta_e
        if delta_e < closer_color_delta:
            closer_color_delta = delta_e
            closer_color = list_color

    return closer_color

def get_scope_params(fil):
    '''Get scope's dict from a tmThemefile'''

    scope_params = {}

    tree = etree.parse(fil)
    i = 0

    # all dicts
    for elem in tree.xpath("dict/array/dict/key"):
        if elem.text == "scope":
            scope = elem.getnext()
            i += 1
            scope_params[i] = {}
            scope_params[i]["scope"] = scope.text
        try:
            if elem.text == "settings" and isinstance(scope_params[i], dict):
                dict2 = elem.getnext()
                for settings in list(dict2):
                    if settings.text == "foreground":
                        foreground = settings.getnext()
                        scope_params[i]["foreground"] = foreground.text
                    if settings.text == "background":
                        background = settings.getnext()
                        scope_params[i]["background"] = background.text
                    if settings.text == "fontStyle":
                        font_style = settings.getnext()
                        scope_params[i]["fontStyle"] = font_style.text

        except KeyError:
            #  no scope before
            pass

    return scope_params

def get_general_params(fil):
    '''Get general settings from a tmThemefile'''

    general_params = {}

    tree = etree.parse(fil)

    # all dicts
    for elem in tree.xpath("dict/array/dict/dict/key"):
        if elem.text == "background":
            background = elem.getnext()
            general_params["background"] = background.text
        if elem.text == "foreground":
            foreground = elem.getnext()
            general_params["foreground"] = foreground.text
        if len(general_params) == 2:
            break
    return general_params

def get_general_infos(fil):
    '''Get general infos from a tmThemefile'''

    general_infos = {}

    tree = etree.parse(fil)

    # all dicts
    for elem in tree.xpath("dict/key"):
        if elem.text == "name":
            name = elem.getnext()
            general_infos["name"] = name.text
        if elem.text == "author":
            author = elem.getnext()
            general_infos["author"] = author.text
        if len(general_infos) == 2:
            break
    return general_infos

def get_color_file_html_header(bgcolor, fgcolor, infos):
    """ return header """

    infos_formated = ""
    for info in infos:
        infos_formated += "<p><b>"+info+"</b>&nbsp;&nbsp;<span>"+infos[info]+"</span></p>"

    html = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>colors-rgb.html</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        html {
            background-color: """+bgcolor+""";
            color: """+fgcolor+""";
        }
        div#colors div {
            width: 64px;
            height: 64px;
            margin: 2px;
            text-align: center;
            font-size: 12px;
            font-family: Arial, Helvetica, sans-serif;
            color:#000;
            display: inline-block;
        }

        div#colors div.dashed {
            border: 2px grey dashed;
        }
       
        input {
            position: absolute;
            top: 20px;
            right: 20px;
        }
    </style>
</head>

<body>
    <p>
    """+infos_formated+"""
    </p>
    <form>
        <div>
        <input type="range" id="item_size" min="16" max="128" value="64" oninput="var elements = document.querySelectorAll('div#colors div'); for (var i = 0; i < elements.length; i++){ elements[i].style.width = this.value + 'px'; elements[i].style.height = this.value + 'px'; }"
            /></div>
    </form>
    <div id="colors">

    """

    return html


def get_color_file_html_footer():
    """ return footer """

    html = """
    </div>
        <script>
            function selectText(element) {
                if (document.selection) {
                    var range = document.body.createTextRange();
                    range.moveToElementText(element);
                    range.select();
                } else if (window.getSelection) {
                    var range = document.createRange();
                    range.selectNode(element);
                    window.getSelection().addRange(range);
                }
            }
        </script>
    </body>
    </html>
    """

    return html

def get_color_file_html_new_color(scope, color, dashed):
    """ return new color """
    if scope != "":
        scope_infos = "SCOPE: "+scope
    else:
        scope_infos = ""

    if dashed:
        class_added = "dashed"
    else:
        class_added = ""


    html = "<div class=\""+class_added+"\" title=\""+scope_infos+"\" style=\"background-color:"+color+";\"><br/><span>"+color+"</span></div>\n"

    return html




