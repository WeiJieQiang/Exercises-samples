from sys import argv

script, filename = argv

txt = open(filename,'w') # return a file object named as txt
 
print "Here is your file %r: " % filename
#print txt.read() # apply read method on txt
#print txt.readline(20)

#txt.close()
txt.write("sth more") # overwrite the file with the input
txt.write("\n even more") # these are just concatenated 


print "I will also ask you to type it again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
