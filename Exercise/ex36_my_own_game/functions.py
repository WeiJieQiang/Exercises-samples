# this is the module I keep all the functions
from sys import exit

def postdoc_life():
    print "You are in a postdoc position."
    print "There are two ways for your career."
    print "There are also two destination for your life."
    
    print "Are you Chinese?"
    
    nationality = raw_input("> ")
    
    if nationality == 'yes':
        country_dilemma()
    elif 'no' in nationality:
        country_determine()
    else:
        print "go on, alien."
        #dead("You must be an alien!!")
    
    print "Do you want to have a stable life?"
    stability = raw_input("> ")
    
    if stability == 'yes':
        go_to_industry()
        possible_company = ['Ericsson','ABB','Scania']
    else:
        postdoc_life()   
        
def dead(string):
    print string, "Good job!"
    exit(0)
    
def country_dilemma(): pass

def country_determine(): pass
    
