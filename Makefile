SRCS = Midway-Regular.sfd    \
       Midway-Bold.sfd       \
       Midway-Italic.sfd     \
       Midway-BoldItalic.sfd
OTFS = $(SRCS:.sfd=.otf)

.PHONY: all clean

all: $(OTFS)

clean:
	rm -rf $(OTFS)

%.otf: %-w550.sfd
	fontforge -quiet -script gen.py $< $@

%-w550.sfd: %.sfd
	fontforge -quiet -script change_glyph_width.py $< 550 $@
