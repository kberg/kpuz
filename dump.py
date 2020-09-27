#! /usr/bin/env python
import puz
import ipuz
import sys
import pprint

input_file = sys.argv[1]

try:
  tp = puz.read(input_file)
  pp = pprint.PrettyPrinter(indent=4)
  pp.pprint(vars(tp))
except puz.PuzzleFormatError as e:
  print "error %s" % e.message
