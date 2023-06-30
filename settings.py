# FONT
FONT="Roboto"
SMALL = 20
NORMAL = 34
LARGE = 50

CORNER_RADIUS = 10

#COLORS
PRIMARY = "#fefae0"
ACCENTBROWN = "#d4a373"
ACCENTGREEN = "#ccd5ae"
SECONDARYBROWN = "#faedcd"
SECONDARYGREEN =  "#e9edc9"
DEEPBROWN = "#855d36"
DEEPGREEN = "#728046"
# BUTTON
BUTTON = {
    "AC":{"row":0, "col":0, "colspan": 2, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "(":{"row":0, "col":2, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    ")":{"row":0, "col":3, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "7":{"row":1, "col":0, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "8":{"row":1, "col":1, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "9":{"row":1, "col":2, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "4":{"row":2, "col":0, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "5":{"row":2, "col":1, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "6":{"row":2, "col":2, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "1":{"row":3, "col":0, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "2":{"row":3, "col":1, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "3":{"row":3, "col":2, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "0":{"row":4, "col":0, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "+":{"row":1, "col":3, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "-":{"row":2, "col":3, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "x":{"row":4, "col":3, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "/":{"row":3, "col":3, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "√":{"row":2, "col":4, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "x²":{"row":1, "col":4, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "Del":{"row":0, "col":4, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    ".":{"row":4, "col":2, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "=":{"row":3, "col":4, "colspan": 1, "rowspan": 2, "hv_color": ACCENTGREEN, "color" : DEEPGREEN},
    "E":{"row":4, "col":1, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN}
}

SCIENTIFIC_BUTTON = {
    "AC":{"row":0, "col":3, "colspan": 1, "rowspan": 2, "hv_color": ACCENTGREEN, "color" : DEEPGREEN},
    "(":{"row":4, "col":1, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    ")":{"row":4, "col":2, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "7":{"row":5, "col":0, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "8":{"row":5, "col":1, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "9":{"row":5, "col":2, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "4":{"row":6, "col":0, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "5":{"row":6, "col":1, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "6":{"row":6, "col":2, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "1":{"row":7, "col":0, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "2":{"row":7, "col":1, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "3":{"row":7, "col":2, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "0":{"row":8, "col":0, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "+":{"row":4, "col":3, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "-":{"row":5, "col":3, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "x":{"row":6, "col":3, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "/":{"row":7, "col":3, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "x²":{"row":2, "col":3, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "Del":{"row":4, "col":0, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    ".":{"row":8, "col":1, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "=":{"row":8, "col":3, "colspan": 1, "rowspan": 1, "hv_color": ACCENTGREEN, "color" : DEEPGREEN},
    "ln":{"row":0, "col":2, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "log":{"row":0, "col":1, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "sin":{"row":1, "col":0, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "cos":{"row":1, "col":1, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "tan":{"row":1, "col":2, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "SHIFT":{"row":0, "col":0, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    # "e":{"row":4, "col":1, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "x!":{"row":3, "col":0, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    # "∛":{"row":4, "col":1, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "^":{"row":3, "col":1, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "𝛑":{"row":3, "col":2, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "sinh":{"row":2, "col":0, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "cosh":{"row":2, "col":1, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "tanh":{"row":2, "col":2, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "x³":{"row":3, "col":3, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "E":{"row":8, "col":2, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN}  
}

SHIFT_BUTTON = {
    "∛":{"row":3, "col":3, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "e":{"row":0, "col":2, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "√":{"row":2, "col":3, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "sin-1":{"row":1, "col":0, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "cos-1":{"row":1, "col":1, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "tan-1":{"row":1, "col":2, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN},
    "log x":{"row":0, "col":1, "colspan": 1, "rowspan": 1, "hv_color": DEEPBROWN, "color" : ACCENTBROWN}
}