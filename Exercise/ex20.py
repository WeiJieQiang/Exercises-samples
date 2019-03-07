from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

#the following function set the offset back to the beginning of the file    
def rewind(f):
    f.seek(0)

# readline reads the line at the offset, and then the offset moves to the next line.    
def print_a_line(line_count,f):
    print line_count, f.readline()
    
current_file = open(input_file)

print "First let us print the whole file:\n"

print_all(current_file)

print "Now let us rewind, kind of like a tape."

rewind(current_file)

print "Let us print three lines:"

current_line = 1 
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1 
print_a_line(current_line,current_file)
