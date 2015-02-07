#!/usr/bin/env python

# Written by Bram Cohen
# see LICENSE.txt for license information

from distutils.core import setup
import BitTornado

setup(
    name="BitTornado",
    version=BitTornado.version,
    author="Bram Cohen, John Hoffman, Uoti Arpala et. al.",
    author_email="<theshadow@degreez.net>",
    url="http://www.bittornado.com",
    description="John Hoffman's fork of the original bittorrent",
    license="MIT",

    packages=["BitTornado", "BitTornado.BT1"],

    scripts=["btdownloadheadless.py", "bttrack.py", "btmakemetafile.py",
             "btlaunchmany.py", "btcompletedir.py", "btdownloadcurses.py",
             "btlaunchmanycurses.py", "btmakemetafile.py", "btreannounce.py",
             "btrename.py", "btshowmetainfo.py",
             "btcopyannounce.py", "btsethttpseeds.py"]
)
