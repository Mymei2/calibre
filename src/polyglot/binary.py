#!/usr/bin/env python2
# vim:fileencoding=utf-8
# License: GPL v3 Copyright: 2019, Kovid Goyal <kovid at kovidgoyal.net>

from __future__ import absolute_import, division, print_function, unicode_literals

from base64 import standard_b64encode, standard_b64decode
from polyglot.builtins import unicode_type


def as_base64_bytes(x, enc='utf-8'):
    if isinstance(x, unicode_type):
        x = x.encode(enc)
    return standard_b64encode(x)


def as_base64_unicode(x, enc='utf-8'):
    if isinstance(x, unicode_type):
        x = x.encode(enc)
    return standard_b64encode(x).decode('ascii')


def from_base64_unicode(x, enc='utf-8'):
    if isinstance(x, unicode_type):
        x = x.encode('ascii')
    return standard_b64decode(x).decode(enc)


def from_base64_bytes(x):
    if isinstance(x, unicode_type):
        x = x.encode('ascii')
    return standard_b64decode(x)
