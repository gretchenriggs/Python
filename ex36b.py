from sys import exit

def board_bus():
    print "Once you arrive at the concert grounds, do you stop to get a cold beer or"
    print "head out to the stage to set up camp to see Modest Mouse?"
    
    next = raw_input("> ")
    
    if "beer" in next:
        print "Boy, it's a long beer line.  That's OK, Modest Mouse doesn't start playing for another"
        print "half hour."
        print "You set up somewhere near the back of the audience, but the view is still great."
        print "You have an awesome time!  Next up, your fav band Wilco!"
        wilco()
        
    elif "set" or "camp" or "stage" in next:
        print "You got a great spot!  Way to go!"
        print "Now that you've got your spot that your buddies will hold for you,"
        print "should you go get a beer before the show?"

        next = raw_input("> ")

        if next == "yes" or next == "beer":
            print "You go out to get the beer, but on the way back you get smushed to death by the crowd!"
            dead("You do NOT 'float on okay'!")
        elif next == "no":
            print "Good idea.  It's $8 a beer, anyway."
            print "You have the time of your life!  Next up, the Wilco stage!"
            wilco()
        else:
            print "I got no idea what that means."
            dead("So, your time at ACL is over.")
            
    else:
        print "Well, if you can't make up your mind, I will for you."
        dead("Your time at ACL is over.")

    
def wilco():
    print "The headliner for the entire festival, Wilco, takes the stage."
    print "How many people are in the band?  Remember this is 2004."
    
    next = int(raw_input("> "))
    print next
    
    while next != 6:
        print "Nope.  Remember it's less than 10, but greater than 0 ;)"
        print "Again, how many people are in the band?  Remember this is 2004." 
        next = int(raw_input("> "))
    
    print "You're right!  There are 6 guys in the band."
    print "For that correct trivia answer, you win a free commemorative T-shirt!"
    
    print "Next, the band starts playing your favorite song 'Passenger Side'"
    print "You start to sing along."
    print "The guy next to you starts laughing in your face.  Do you punch him?"
    
    next = raw_input("> ")
    
    if next == "yes":
        print "Ouch!  Your hand is broken and the guy's nose is, too.  He's threatening to sue."
        print "Violence rarely solves anything"
        dead("...and you are kicked out of the show.")
    elif next == "no":
        print "Good job keeping your feelings in check."
        print "Enjoy the show and forget about that jerky bloke."
        dead("You finish the show smiling and think about next year's festival!")
    else:
        print "I cannot understand you, man."
        dead("It must be time for you to go.")
        
        
def walk():
    print "One thing you didn't think to consider for this walk:"
    print "You're in Austin in early September"
    print "AND it's 100 degrees with 95% humidity outside."
    print "Do you take a break from walking to drink some nice cold water or trudge on?"

    next = raw_input("> ")

    if next == "break" or next == "water":
        print "Boy, does that water feel good going down.  You needed that!"
        board_bus()
    else:
        print "You made a BAD choice refusing that water."
        dead("You overheat and keel over dead on the side of the road just as Modest Mouse kicks off their show.")

        
def dead(why):
    print why, "Peace out!"
    exit(0)

def start():
    print "Woo!  The 2004 ACL Fest is here at last."
    print "Austin City Limits...who'd have thought you'd be here to enjoy this giant concert?!?"
    print "You're in downtown Austin.  Do you wait for the bus or set out walking to the park grounds?"

    next = raw_input("> ")

    if "bus" in next:
        board_bus()
    elif "walk" in next:
        walk()
    else:
        dead("Well...guess you aren't going after all :(")


start()