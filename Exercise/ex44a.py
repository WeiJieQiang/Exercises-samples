class parent(object):
    
    def implicit(self):
        print "Parent implicit()"
        
class child(parent):

    pass
    
dad = parent()
son = child()

dad.implicit()
son.implicit() 
