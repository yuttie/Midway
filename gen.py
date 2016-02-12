#!/usr/bin/fontforge -quiet -script
import fontforge
from os import path

sources = [
    'Midway-Regular.sfd',
    'Midway-Bold.sfd',
    'Midway-Italic.sfd',
    'Midway-BoldItalic.sfd',
]
gen_flags = (
    'opentype',
    'dummy-dsig',
    'no-hints',
    'no-flex',
    'omit-instructions',
)

for src_fp in sources:
    font = fontforge.open(src_fp)
    base = path.splitext(src_fp)[0]
    out_fp = base + '.otf'
    font.generate(out_fp, flags=gen_flags)
    font.close()
