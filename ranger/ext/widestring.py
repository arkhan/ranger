# -*- encoding: utf-8 -*-
# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.

from __future__ import (absolute_import, division, print_function)

import sys
from unicodedata import east_asian_width

from ranger import PY3

# ASCIIONLY kept for external compatibility but no longer used internally;
# replaced by the faster str.isascii() built-in.
ASCIIONLY = set(chr(c) for c in range(1, 128))
NARROW = 1
WIDE = 2
WIDE_SYMBOLS = set('WF')

# Nerd Font version for Private Use Area (PUA) character width:
#   0 → no special handling (default)
#   2 → NF v2 glyphs are 1-cell wide (no extra handling needed)
#   3 → NF v3 glyphs are 2-cell wide (PUA U+E000..U+F8FF treated as WIDE)
# Updated at startup via ranger.container.settings signal.
NERD_FONTS_VERSION = 0

# PUA ranges used by Nerd Fonts (BMP only; supplementary PUA is uncommon)
_NF_PUA_RANGES = (
    (0xE000, 0xF8FF),   # BMP Private Use Area
)


def uwid(string):
    """Return the width of a string"""
    if not PY3:
        string = string.decode('utf-8', 'ignore')
    return sum(utf_char_width(c) for c in string)


def _is_nerd_font_pua(char):
    """Return True if *char* is in a Nerd Fonts Private Use Area range."""
    cp = ord(char)
    for lo, hi in _NF_PUA_RANGES:
        if lo <= cp <= hi:
            return True
    return False


def utf_char_width(char):
    """Return the display width of a single character.

    Accounts for Nerd Font v3 glyphs (2-cell wide) when NERD_FONTS_VERSION == 3.
    """
    if NERD_FONTS_VERSION == 3 and _is_nerd_font_pua(char):
        return WIDE
    if east_asian_width(char) in WIDE_SYMBOLS:
        return WIDE
    return NARROW


def string_to_charlist(string):
    """Return a list of characters with extra empty strings after wide chars"""
    # str.isascii() is SIMD-optimised in CPython 3.7+ and far faster than
    # building a set and computing the difference for typical filenames.
    if string.isascii():
        return list(string)
    result = []
    if PY3:
        for char in string:
            result.append(char)
            if utf_char_width(char) == WIDE:
                result.append('')
    else:
        try:
            # This raised a "UnicodeEncodeError: 'ascii' codec can't encode
            # character u'\xe4' in position 10: ordinal not in range(128)"
            # for me once.  I thought errors='ignore' means IGNORE THE DAMN
            # ERRORS but apparently it doesn't.
            string = string.decode('utf-8', 'ignore')
        except UnicodeEncodeError:
            return []
        for char in string:
            result.append(char.encode('utf-8'))
            if east_asian_width(char) in WIDE_SYMBOLS:
                result.append('')
    return result


class WideString(object):  # pylint: disable=too-few-public-methods

    def __init__(self, string, chars=None):
        try:
            self.string = str(string)
        except UnicodeEncodeError:
            # Here I assume that string is a "unicode" object, because why else
            # would str(string) raise a UnicodeEncodeError?
            self.string = string.encode('latin-1', 'ignore')
        if chars is None:
            self.chars = string_to_charlist(string)
        else:
            self.chars = chars

    def __add__(self, string):
        """
        >>> (WideString("a") + WideString("b")).string
        'ab'
        >>> (WideString("a") + WideString("b")).chars
        ['a', 'b']
        >>> (WideString("afd") + "bc").chars
        ['a', 'f', 'd', 'b', 'c']
        """
        if isinstance(string, str):
            return WideString(self.string + string)
        elif isinstance(string, WideString):
            return WideString(self.string + string.string, self.chars + string.chars)
        return None

    def __radd__(self, string):
        """
        >>> ("bc" + WideString("afd")).chars
        ['b', 'c', 'a', 'f', 'd']
        """
        if isinstance(string, str):
            return WideString(string + self.string)
        elif isinstance(string, WideString):
            return WideString(string.string + self.string, string.chars + self.chars)
        return None

    def __str__(self):
        return self.string

    def __repr__(self):
        return '<' + self.__class__.__name__ + " '" + self.string + "'>"

    def __getslice__(self, start, stop):
        """
        >>> WideString("asdf")[1:3]
        <WideString 'sd'>
        >>> WideString("asdf")[1:-100]
        <WideString ''>
        >>> WideString("モヒカン")[2:4]
        <WideString 'ヒ'>
        >>> WideString("モヒカン")[2:5]
        <WideString 'ヒ '>
        >>> WideString("モabカン")[2:5]
        <WideString 'ab '>
        >>> WideString("モヒカン")[1:5]
        <WideString ' ヒ '>
        >>> WideString("モヒカン")[:]
        <WideString 'モヒカン'>
        >>> WideString("aモ")[0:3]
        <WideString 'aモ'>
        >>> WideString("aモ")[0:2]
        <WideString 'a '>
        >>> WideString("aモ")[0:1]
        <WideString 'a'>
        """
        if stop is None or stop > len(self.chars):
            stop = len(self.chars)
        if stop < 0:
            stop = len(self.chars) + stop
        if stop < 0:
            return WideString("")
        if start is None or start < 0:
            start = 0
        if stop < len(self.chars) and self.chars[stop] == '':
            if self.chars[start] == '':
                return WideString(' ' + ''.join(self.chars[start:stop - 1]) + ' ')
            return WideString(''.join(self.chars[start:stop - 1]) + ' ')
        if self.chars[start] == '':
            return WideString(' ' + ''.join(self.chars[start:stop - 1]))
        return WideString(''.join(self.chars[start:stop]))

    def __getitem__(self, i):
        """
        >>> WideString("asdf")[2]
        <WideString 'd'>
        >>> WideString("……")[0]
        <WideString '…'>
        >>> WideString("……")[1]
        <WideString '…'>
        """
        if isinstance(i, slice):
            return self.__getslice__(i.start, i.stop)
        return self.__getslice__(i, i + 1)

    def __len__(self):
        """
        >>> len(WideString("poo"))
        3
        >>> len(WideString("モヒカン"))
        8
        """
        return len(self.chars)


if __name__ == '__main__':
    import doctest
    sys.exit(doctest.testmod()[0])
