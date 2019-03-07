class parent(object):
    def override(self):
        print "Parent override()"
        
class child(parent):
    def override(self):
        print "CHild override()"
        
dad = parent()
son = child()

dad.override()
son.override()
