# ColorText.py
# Python module that allows simple printing of colored text (and text effects) using ANSI escape sequences.
__author__ = "Rory Brown"
__license__ = "GPL"

from colorText.constants import *

# Generate a color value string for use in an ANSI escape sequence for a given 8-bit color value
def generate8BitColor(colorValue, type = FOREGROUND):
	if not type in (FOREGROUND, BACKGROUND):
		raise ValueError(f"Type must be FOREGROUND ({FOREGROUND}) or BACKGROUND ({BACKGROUND}), recieved {type}")
	elif colorValue < 0 or colorValue > 255:
		raise ValueError(f"colorValue must be between 0 and 255 (inclusive), recieved {colorValue}")
	return ";".join([str(type), "5", str(colorValue)])

# Generate a color value string for use in an ANSI escape sequence for given RGB color values
def generateRgbColor(red, green, blue, type = FOREGROUND):
	if not type in (FOREGROUND, BACKGROUND):
		raise ValueError(f"Type must be FOREGROUND ({FOREGROUND}) or BACKGROUND ({BACKGROUND}), recieved {type}")
	elif any([color < 0 or color > 255 for color in [red, green, blue]]):
		raise ValueError(f"Color values must be between 0 and 255 (inclusive), recieved red = {red}, green = {green}, blue = {blue}")
	return ";".join([str(type), "2", str(red), str(green), str(blue)])

# Combine a foreground and background color to apply as a single color. Returns string for use in ANSI escape sequence
def combineFgBgColor(fg, bg):
	return fg + ";" + bg

# Generate an ANSI escape sequence for a given color and list of effects. This can then be printed to set the text color / effects
def _generateEscapeSequence(color = 0, effects = []):
	return "\033[" + ";".join([str(color)] + [str(effect) for effect in effects]) + "m"

# Wraps a string with the appropriate escape sequences to cause it to become colorised upon printing.
def coloriseText(text, color, effects = []):
	return _generateEscapeSequence(color, effects) + text + _generateEscapeSequence(DEFAULT)

# Sets the color and effects currently in use in the terminal
def setColorMode(color = 0, effects = []):
	print(_generateEscapeSequence(color, effects), end = "")

# Decorator used to wrap functions with setColorMode, allowing functions to be ran in specific color and text effect modes
def coloriseFunction(color, effects = []):
	def decorator(func):
		def wrapper(*args, **kwargs):
			setColorMode(color, effects)
			result = func(*args, **kwargs)
			setColorMode(DEFAULT)
			return result
		return wrapper
	return decorator

# Runs a function with the terminal with a specific color and set of effects.
def runFunctionColored(func, color, effects, *args, **kwargs):
	setColorMode(color, effects)
	result = func(*args, **kwargs)
	setColorMode(DEFAULT)
	return result

# prints a given text string with a specific color and set of effects. Can accept the same kwargs as print()
def printColored(text, color, effects = [], **kwargs):
	runFunctionColored(print, color, effects, text, **kwargs)

# Print functions for each 4-bit color. print() is decorated with each color respectively.
@coloriseFunction(BLACK, [BOLD])
def printBlack(text, **kwargs):
	print(text, **kwargs)

@coloriseFunction(RED, [BOLD])
def printRed(text, **kwargs):
	print(text, **kwargs)

@coloriseFunction(GREEN, [BOLD])
def printGreen(text, **kwargs):
	print(text, **kwargs)

@coloriseFunction(YELLOW, [BOLD])
def printYellow(text, **kwargs):
	print(text, **kwargs)

@coloriseFunction(BLUE, [BOLD])
def printBlue(text, **kwargs):
	print(text, **kwargs)

@coloriseFunction(MAGENTA, [BOLD])
def printMagenta(text, **kwargs):
	print(text, **kwargs)

@coloriseFunction(CYAN, [BOLD])
def printCyan(text, **kwargs):
	print(text, **kwargs)

@coloriseFunction(WHITE, [BOLD])
def printWhite(text, **kwargs):
	print(text, **kwargs)