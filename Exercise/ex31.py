print "You enter a dark room with two doors. Do you go through door #1 or door #2 or door #3?"

door = raw_input("> ")

if door == "1":
    print "There is a giant bear here eating a cheese cake. what do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear = raw_input('> ')
    
    if bear == "1":
        print "The bear eats your off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
        
elif door == "2":
    print "You stare into the endless abyss at cthuhlu's retina."
    print "1. Blueberries. "
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolveros yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "THe insanity rots your eyes into a pool of muck. Good job!"
        
elif door == "3":
    print "You entered the heaven."
    
    happiness = raw_input("> ")
    
    if happiness == "1":
        print "Your body is fully recovered."
        
else:
    print "You stumble around and fall on a knife and die. Good job!" 
