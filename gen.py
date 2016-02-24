#!/usr/bin/fontforge -script
import fontforge
import sys


gen_flags = (
    'opentype',
    'dummy-dsig',
    'no-hints',
    'no-flex',
    'omit-instructions',
)

src_fp  = sys.argv[1]
dest_fp = sys.argv[2]

font = fontforge.open(src_fp)
font.generate(dest_fp, flags=gen_flags)
font.close()
