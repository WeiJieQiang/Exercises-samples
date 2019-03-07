from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too. How?
inputf = open(from_file)
indata = inputf.read()

print "The input file is %d bytes long" % len(indata)

print "Dose the output file exist? %r" % exists(to_file)
print "Ready, hit return to continue, ctrl-c to abort."
raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."

output.close()
inputf.close()
