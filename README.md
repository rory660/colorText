# colorText.py
Python module that handles ANSI color codes and text effects.

## Functions

### generate8BitColor
```python
generate8BitColor(colorValue, type = FOREGROUND)
```

#### Parameters:
+ `colorValue`: Integer value between 0 and 255 (inclusive) corresponding to the color.
+ `type = FOREGROUND`: type of colour to generate (can be `colorText.FOREGROUND` or `colorText.BACKGROUND`)

#### Return:
A string containing the color value for use in an ANSI escape sequence.

---
### generateRgbColor
```python
generateRgbColor(red, green, blue, type = FOREGROUND)
```

#### Parameters:
+ `red`: Integer value between 0 and 255 (inclusive) corresponding to the red level.
+ `green`: Integer value between 0 and 255 (inclusive) corresponding to the green level.
+ `blue`: Integer value between 0 and 255 (inclusive) corresponding to the blue level.
+ `type = FOREGROUND`: type of colour to generate (can be `colorText.FOREGROUND` or `colorText.BACKGROUND`)

#### Return:
A string containing the color value for use in an ANSI escape sequence.

---
### combineFgBgColor
```python
combineFgBgColor(fg, bg)
```

#### Parameters:
+ `fg`: Foreground color as a string (e.g. `colorText.BLUE`, `generate8BitColor(180)`, etc).
+ `bg`: Background color as a string.

#### Return:
A string containing the combined color values for use in an ANSI escape sequence.

---
### coloriseText
```python
coloriseText(text, color, effects = [])
```

#### Parameters:
+ `text`: A string of text to have the given color and list of effects applied to.
+ `color`: Color to be applied to the text string.
+ `effects = []`: A list of text effects (defined as constants, e.g. colorText.BOLD).

#### Return:
A string containing the original `text` string, wrapped with escape sequences to set the color and text effects.

---
### setColorMode

Sets the terminal to print with the given color and set of effects.

```python
setColorMode(color = 0, effects = [])
```

#### Parameters:
+ `color = 0`: Color mode to set the terminal to.
+ `effects = []`: A list of text effects (defined as constants, e.g. colorText.BOLD).

#### Return:
None.

---
### coloriseFunction
Decorator factory used to wrap a function with calls to `setColorMode`, allowing for the function to be ran with a given print color and set of effects.

```python
coloriseFunction(color, effects = [])
```

#### Parameters:
+ `color = 0`: Color mode to set the terminal to.
+ `effects = []`: A list of text effects (defined as constants, e.g. colorText.BOLD).

#### Return:
A decorator that takes a function as an argument.

#### Example:
The following code is used in the module to create `printRed(text, \*\*kwargs)`:
```python
@coloriseFunction(RED, [BOLD])
def printRed(text, **kwargs):
	print(text, **kwargs)
```

---
### runFunctionColored

Runs a function with calls to `setColorMode`, causing the function to be ran with a given print color and set of effects.

```python
runFunctionColored(func, color, effects, *args, **kwargs)
```

#### Parameters:
+ `func`: function to be ran.
+ `color`: Color mode to set the terminal to.
+ `effects`: A list of text effects (defined as constants, e.g. colorText.BOLD).
+ `*args`: The anonymous arguments to be passed to `func`.
+ `**kwargs`: The named arguments to be passed to `func`.

#### Return:
Returns the return value of `func`.

---
### printColored

Prints a given string with a given color and set of text effects. Accepts the same named arguments as `print`.

```python
printColored(text, color, effects = [], **kwargs)
```

#### Parameters:
+ `text`: A string of text to be printed.
+ `color`: Color for the text to be printed in.
+ `effects`: A list of text effects (defined as constants, e.g. colorText.BOLD) to be applied to `text` when printing.
+ `**kwargs`: Named arguments identical to those accepted by the `print` function.

#### Return:
None.

---
### print\<color\>

Prints the given string in the color specified in the function name.

```python
printBlack(text, **kwargs)
printRed(text, **kwargs)
printGreen(text, **kwargs)
printYellow(text, **kwargs)
printBlue(text, **kwargs)
printMagenta(text, **kwargs)
printCyan(text, **kwargs)
printWhite(text, **kwargs)
```

#### Parameters:
+ `text`: A string of text to be printed.
+ `**kwargs`: Named arguments identical to those accepted by the `print` function.

#### Return:
None.

## Constants
```python
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
```