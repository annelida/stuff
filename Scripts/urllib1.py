import urllib

fhand = urllib.urlopen('http://www.pythonlearn.com')
for line in fhand:
   print line.strip()

