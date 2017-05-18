from collections import namedtuple

Color = namedtuple('Color', ['r', 'g', 'b'])


GUMDB = {
    b'012546612296': {
        'brand': 'Trident',
        'colorname': 'light blue',
        'color': Color(0x87, 0xCE, 0xEB),
    },
    b'012546004701': {
        'brand': 'Trident',
        'colorname': 'dark blue',
        'color': Color(0x00, 0x00, 0x8B),
    },
    b'012546619592': {
        'brand': 'Trident',
        'colorname': 'orange',
        'color': Color(0xFF, 0xA5, 0x00),
    },
    b'012546615563': {
        'brand': 'Trident',
        'colorname': 'pink',
        'color': Color(0xFF, 0xC0, 0xCB),
    },
    b'012546672511': {
        'brand': 'Trident',
        'colorname': 'mint',
        'color': Color(0x00, 0xFF, 0x7F),
    },
    b'012546673099': {
        'brand': 'Trident',
        'colorname': 'gold',
        'color': Color(0xFF, 0xD7, 0x00),
    },

}
