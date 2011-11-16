#!/usr/bin/env python
import base64
import sys
import os

# This will Base-64 encode an image for inline inclusion in HTML formatted content.
if len(sys.argv) != 2:
	print "Usage: encodeimg <image file>"
else:
	image_filename = sys.argv[1]
	if os.path.isfile(image_filename):
		print base64.b64encode( open(image_filename).read() )
	else:
		print "Can't open %s" % image_filename
