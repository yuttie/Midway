#!/usr/bin/python
import fontforge
import sys

sources = [
    'Midway-Regular.sfd',
    'Midway-Bold.sfd',
    'Midway-Italic.sfd',
    'Midway-BoldItalic.sfd',
]

target_width = int(sys.argv[1])

for src_fp in sources:
    font = fontforge.open(src_fp)

    for glyph in font.glyphs():
        w = glyph.width
        lsb = glyph.left_side_bearing
        rsb = glyph.right_side_bearing
        sb = lsb + rsb
        actual_width = w - sb

        target_sb = target_width - actual_width
        if sb == 0:
            target_lsb = target_sb * 1 / 2
            target_rsb = target_sb * 1 / 2
        else:
            target_lsb = target_sb * lsb / sb
            target_rsb = target_sb * rsb / sb

        glyph.width = target_width
        glyph.left_side_bearing = target_lsb
        glyph.right_side_bearing = target_rsb

    font.save()
