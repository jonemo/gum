from curses.ascii import isdigit

from .db import GUMDB


def _clean_upc(upc):
    if isinstance(upc, bytes):
        upc = upc.decode('ascii')
    upc_numbers_only = ''.join([ch for ch in upc if isdigit(ch)])
    upc_ascii = upc_numbers_only.encode('ascii')
    return upc_ascii


def upc_to_color(upc):
    clean_upc = _clean_upc(upc)
    return GUMDB.get(clean_upc, {}).get('color')


def upc_to_brand(upc):
    clean_upc = _clean_upc(upc)
    return GUMDB.get(clean_upc, {}).get('brand')
