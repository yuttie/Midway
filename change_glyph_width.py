#!/usr/bin/fontforge -script
import fontforge
import math
import psMat
import sys


def change_glyph_width(font, target_width):
    for glyph in font.glyphs():
        glyph.transform(psMat.skew(math.radians(font.italicangle)))

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

        glyph.left_side_bearing = target_lsb
        glyph.right_side_bearing = target_rsb
        glyph.width = target_width

        glyph.transform(psMat.skew(math.radians(-font.italicangle)))

src_fp       = sys.argv[1]
target_width = int(sys.argv[2])
dest_fp      = sys.argv[3]

font = fontforge.open(src_fp)
change_glyph_width(font, target_width)
font.save(dest_fp)
font.close()
