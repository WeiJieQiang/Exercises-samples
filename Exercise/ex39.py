ten_things = "apples oranges crows telephone light sugar"

print "wait, there is not 10 things in that list, let us fix that."

stuff = ten_things.split(' ')
more_stuff = ["day","night","song","frisbee","corn","banana","girl","boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There is %d items now." % len(stuff)
    
print "There we go: ", stuff

print "let us do some thing with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join( stuff)
print '#'.join(stuff[3:5])
