COLORS = {
    'red': (255, 127, 127),
    'green': (127, 255, 127),
    'black': (51, 51, 51)
}

# Size of window
METRIKA = {
    'width': 1024,
    'height': 680,
}

# Size width and height
w, h = METRIKA['width'], METRIKA['height']

# Fraction (like a 20x20)
fr = (20, 14)
METRIKA['fractions'] = fr

# Get size by faraction (1x1)
METRIKA['size'] = (w // fr[0], h // fr[1])
