class Song(object):
    
    def __init__(self, lyrics, language): #How many variable here except self defines the extra input to class declarification
        self.lyrics = lyrics
        self.language = language
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
        
        print "I only like to hear it in %s" % self.language
            
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"],"English")
                    
bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"], "English")
                        
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
