from sys import argv

script, filename = argv

txt = open(filename)

print "here's your file %r" % filename

print txt.read()

txt.close()
