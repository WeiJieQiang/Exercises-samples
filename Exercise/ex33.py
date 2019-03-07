def func_while(arg):

    i = 0
    numbers = []
    
    while i<arg:
        print "At the top i is %d" % i
        numbers.append(i)
    
        i = i +1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers

numbers = func_while(100)
    
print "The numbers: "

for num in numbers:
    print num
