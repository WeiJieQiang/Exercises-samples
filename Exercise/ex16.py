from sys import argv

script, filename = argv

print "we are going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit return."

raw_input("?")

print "Opening the file..."
target = open(filename,'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I am going to ask you for three lines."

line1= raw_input("line1:")
line2= raw_input("line2:")
line3= raw_input("line3:")

print "I am going to write these to the file."

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

strs = "%s \n %s \n %s" % (line1,line2,line3)

target.write(strs)

print "and finally, we close it."
target.close()
