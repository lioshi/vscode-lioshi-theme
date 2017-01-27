'''
lib of theme
'''

from lxml import etree

def get_scope_params(fil):
    '''Get scope's dict from a tmThemefile'''

    scope_params = {}

    tree = etree.parse(fil)
    i = 0

    # general settings
    # for elem in tree.xpath("dict/array/dict/dict"):


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
            if elem.text == "settings":
                dict2 = elem.getnext()
                for settings in list(dict2):
                    if settings.text == "background":
                        background = settings.getnext()
                        scope_params[0] = {}
                        scope_params[0]["scope"] = "general.background"
                        scope_params[0]["background"] = background.text
            # pass


    # scope_params_format = {}
    # for entry, entry_value in scope_params
    #     if entry == "scope"
    #         scope_params_format[entry_value] = {}
    #     if entry == "scope"
    #         scope_params_format[entry_value] = {}


    return scope_params


def get_color_file_html_header(bgcolor):
    """ return header """

    html = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>colors-rgb.html</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        html {
            background-color : """+bgcolor+""";
        }
        div#colors div {
            float: left;
            width: 64px;
            height: 64px;
            margin: 2px;
            text-align: center;
            font-size: 12px;
            font-family: Arial, Helvetica, sans-serif;
            color:#000;
        }
        
        div#colors div span {
            font-weight: bold;
            cursor: pointer
        }
        
        div#colors div span:hover {
            text-decoration: underline
        }
        
        input {
            margin-left: 1em;
        }
    </style>
</head>

<body>
    <form>
        <div>Item size:<input type="range" id="item_size" min="16" max="128" value="64" oninput="var elements = document.querySelectorAll('div#colors div'); for (var i = 0; i < elements.length; i++){ elements[i].style.width = this.value + 'px'; elements[i].style.height = this.value + 'px'; }"
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

def get_color_file_html_new_color(color):
    """ return new color """

    html = "<div style=\"background-color:"+color+";\"><br/><span>#"+color+"</span></div>\n"

    return html




