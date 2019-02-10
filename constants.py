# constants.py
# Contains constants to be used with colorText to represent effects and colors.

__author__ = "Rory Brown"
__license__ = "GPL"

# Text effects
DEFAULT = 0 # Reset all colors and effects
BOLD = 1 # Make text bold / Increase color intensity
FAINT = 2 # make text faint / Decrease color intensity
ITALIC = 3
UNDERLINE = 4
SLOW_BLINK = 5 # < 150 per minute
RAPID_BLINK = 6 # > 150 per minute
INVERSE = 7 # Swaps foreground and background colors
CONCEAL = 8
CROSSED_OUT = 9
PRIMARY_FONT = 10 # Select primary / default font
ALT_FONT = 11 # Select alternative font
FRAKTUR = 20 

# Disable various text effects
DISABLE_BOLD = 21
DISABLE_BOLD_FAINT = 22
DISABLE_ITALIC_FRAKTUR = 23
DISABLE_UNDERLINE = 24
DISABLE_BLINK = 25
DISABLE_INVERSE = 27
DISABLE_CONCEAL = 28
DISABLE_CROSSED_OUT = 29

# 4-bit foreground colors
BLACK = 30
RED = 31
GREEN = 32
YELLOW = 33
BLUE = 34
MAGENTA = 35
CYAN = 36
WHITE = 37

FOREGROUND = 38 # Use in generateColor functions to set as foreground color
DEFAULT_FOREGROUND = 39 # Reset foreground color

# 4-bit background colors
BG_BLACK = 40
BG_RED = 41
BG_GREEN = 42
BG_YELLOW = 43
BG_BLUE = 44
BG_MAGENTA = 45
BG_CYAN = 46
BG_WHITE = 47

BACKGROUND = 48 # Use in generateColor functions to set as background color
DEFAULT_BACKGROUND = 49 # Reset background color

# Other text effects
FRAMED = 51
ENCIRCLED = 52
OVERLINED = 53
DISABLE_FRAMED_ENCIRCLED = 54
DISABLE_OVERLINED = 55

# Ideogram effects
IDEOGRAM_UNDERLINE = 60
IDEOGRAM_DOUBLE_UNDERLINE = 61
IDEOGRAM_OVERLINE = 62
IDEOGRAM_DOUBLE_OVERLINE = 63
IDEOGRAM_STRESS_MARKING = 64
DISABLE_IDEOGRAM_EFFECTS = 65