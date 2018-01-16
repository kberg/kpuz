# -*- encoding: utf-8 -*-

import puz
import ipuz
import sys
import re

_, input_file, output_file = sys.argv

LATIN1_SUBS = {
  u"“": u'"',
  u"”": u'"',
  u"‘": u"'",
  u"’": u"'",
  u"–": u"--",
  u"—": u"---",
  u"…": u"...",
  u"№": u"No.",
  u"π": u"pi",
  u"🔥": u"[emoji: fire]",
  u"🙈": u"[emoji: monkey with hands over eyes]",
  u"👉🏾": u"[emoji: hand pointing right]",
  u"👆🏻": u"[emoji: hand pointing up]",
  u"🤘🏽": u"[emoji: hand with raised index and pinky finger]",
  u"✊🏿": u"[emoji: fist]",
  u"ǐ": "i",
}

def printASCII(ip):
  def header(s):
    of.write("<%s>\n" % s)

  def data(s):
    of.write("    %s\n" % s)
  of = codecs.open(output_file, 'w', 'utf-8')

  header("ACROSS PUZZLE V2")
    
  header("TITLE")
  data(ip['title'])
    
  header("AUTHOR")
  data(ip['author'])
    
  header("COPYRIGHT")
  data(ip['copyright'])
    
  header("SIZE")
  data("%sx%s" % (ip['dimensions']['width'], ip['dimensions']['height']))
    
  header("GRID")
  for row in ip['solution']:
    text = ''.join(row).replace('#', '.')
    data(text)
    
  header("ACROSS")
  for c in ip['clues']['Across']:
    data(c[1])
    
  header("DOWN")
  for c in ip['clues']['Down']:
    data(c[1])

  of.close()

def printBinary(ip):
  np = puz.Puzzle()
  np.author = ip['author']
  np.title = ip['title']
  np.copyright = ip['copyright']
  np.width = ip['dimensions']['width']
  np.height = ip['dimensions']['height']
    
  # Converting a solution: The ipuz format is an array of array of chars.
  # The puz format is a single string, known to be width x height chars.
  # Just need to convert # to . as each of those is the empty cell marking.
  sstrings = [''.join(row) for row in ip['solution']]
  sstring = ''.join(sstrings)
  sstring = sstring.replace('#', '.')
    
  np.solution = ''.join(sstring)
  np.fill = re.sub(r"[^.]", "-", np.solution)

  # origin and publisher fields ignored in ipuzzle. What about kind?
  # Ignoring 'puzzle' field, which contains a sophisticated grid format.
    
  # Fortunately ipuz specifies clue numbers, which allows us to order
  # in PUZ's unclear clue ordering.
  a = [(n, latin1ify(clue)) for n, clue in ip['clues']['Across']]
  d = [(n + 0.5, latin1ify(clue)) for n, clue in ip['clues']['Down']]
  np.clues = [clue for _, clue in sorted(a + d)]
   
  # np.preamble = ip['intro']
  np.save(output_file)

def latin1ify(s):
  for search, replace in LATIN1_SUBS.items():
    s = s.replace(search, replace)
  return s

# Start
with open(input_file) as x: idata = x.read()

try:
    ip = ipuz.read(idata)
except ipuz.IPUZException:
    print "Yuk."

if output_file.endswith(".puz"):
  printBinary(ip)
elif output_file.endswith(".txt"):
  printASCII(ip)
else:
  print("output_file not puz or txt")
