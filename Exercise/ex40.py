cities = {'CA': 'San francisco',  'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities["OR"] = 'Portland'

def find_city(themap,state):
    if state in themap:
        return themap[state]
    else:
        return "not found."
        
for item in cities.items():
    print item

# ok, pay attention!
cities['_find'] = find_city # you can assign function to an item in a dictionary

while True:
    print "state? (Enter to quit)",
    state = raw_input("> ")
    
    if not state: break
    
    # this line is the most important ever! study!
    city_found = cities['_find'](cities, state)
    print city_found 
