from argparse import ArgumentParser
from sys import exit

from gum import upc_to_color


parser = ArgumentParser(
    description='Get gum package color as hex rgb value given a UPC code')
parser.add_argument(
    'UPC', type=str, help='UPC code from barcode')


def main():
    args = parser.parse_args()
    print(args)
    upc = args.UPC

    color = upc_to_color(upc)

    if not color:
        print("Cannot find information for UPC %s" % upc)
        return 1
    else:
        print("%X%X%X" % color)  # color is 3-tuple of red, green, blue values
        return 0


if __name__ == '__main__':
    exit(main())
