#!/user/bin/env python

import random
    
def main():
    """start a guessing genre music between dubstep, disco, ska, latin, techno, blues."""
    print("Guess the genre music ")

    x = random.choice("genre")
    guess = None
    
    while x !=guess:
        
        guess = str(input("pick a music genre:"))
        
        if x ==guess:
          print ("taniah nad")
        else:
            print ("try again")
main()