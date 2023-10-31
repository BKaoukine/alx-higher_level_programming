#!/usr/bin/python3

_1st_digite = 0

while _1st_digite < 10:
    _2nd_digite = _1st_digite + 1
    while _2nd_digite < 10:
        separator = '' if _1st_digite == 8 and _2nd_digite == 9 else ", "
        print("{:d}{:d}".format(_1st_digite, _2nd_digite), end=separator)
        _2nd_digite += 1
    _1st_digite += 1
