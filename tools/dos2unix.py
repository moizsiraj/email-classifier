#!/usr/bin/env python
"""\
convert dos linefeeds (crlf) to unix (lf)
usage: dos2unix.py <input> <output>
"""
import sys

outsize = 0
with open("../tools/word_data2.pkl", 'rb') as infile:
  content = infile.read()
with open("../tools/word_data3.pkl", 'wb') as output:
  for line in content.splitlines():
    outsize += len(line) + 1
    output.write(line + b"\n")

print("Done. Saved %s bytes." % (len(content)-outsize))