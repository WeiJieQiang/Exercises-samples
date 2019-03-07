# this is for the composition, which is better than inheritance
class other(object):
    
    def override(self):
        print "other override()"
        
    def implicit(self):
        print "other implicit()"
        
    def altered(self):
        print "other altered()"
        
class child(object):

    def __init__(self):
        self.other = other()
    
    #this is the same as implicit inheritance     
    def implicit(self):
        self.other.implicit()
    
    # this is the same as override explicit   
    def override(self):
        print "child override()"
    
    # this is the same as altered after and before in inheritance    
    def altered(self):
        print "child, before other altered()"
        self.other.altered()
        print "child, after other altered()"
        
dad = other()
son = child()

son.implicit()
son.override()
son.altered()
