import codecs
import puz
import ipuz
import sys
import re

# False for ASCII, True for Binary
output = True

_, input_file, output_file = sys.argv

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
  a = [c + [0] for c in ip['clues']['Across']]
  d = [c + [.5] for c in ip['clues']['Down']]
  both = sorted(a + d, key = lambda c : (c[0] + c[2]))
    
  np.clues = [c[1] for c in both]
   
  # np.preamble = ip['intro']
  np.save(output_file)

# Start
with open(input_file) as x: idata = x.read()

try:
    ip = ipuz.read(idata)
except ipuz.IPUZException:
    print "Yuk."

if output:
  printBinary(ip)
else:
  printASCII(ip)
