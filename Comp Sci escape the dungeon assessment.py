# James Branc, Comp Sci, 28/07/22
import time
# this section is for variables
state = {
    "username": "",
    "room": "start",
    "key": False,
    "looked_for_key": False,
    "listened": False,
    "name": True,
}

###################################################
# This section is where we define all our functions

def quit():
    print("It is sad you have to quit the game.")
    time.sleep(1.2)
    print("We hope to see you some time soon again.")
    time.sleep(1.2)
    print("Until then, good bye old friend.")
    state["room"] = "quit"

def pname():
    print("Howdy, before we begin, whats your name?")
    state["username"] = input("> ")
    username = state["username"]
    print("Nice to meet you, " + username + "!")
    time.sleep(1.5)
    print("Good luck and have fun!")
    time.sleep(1)


# def function defines what the variable does/is.
def welcome_dungeon():
    print("><><><><><><><><><><><><><")
    print(" Welcome to the dungeon!")
    print("><><><><><><><><><><><><><")
    time.sleep(1.3)
    print("A place where all hopes and dreams are lost to the sounds of isolation.")
    time.sleep(1)
# Start room is the room that you start the game in.
# Options are to go forward or look around.
def start_room():
    print("You are standing in the entrance to a deep dark dungeon.")
    time.sleep(1.3)
    print("You see no other options than to enter.")
    time.sleep(1)
    print("Actions available: forward, look")
    action = input("> ")
    if action == "look":
        print("The room is dusty, it hasn't been cleaned in years.")
        time.sleep(1.2)
        print("You notice a cobweb in the corner of the room")
        time.sleep(1.3)
        print("There is a spider chilling there")
        time.sleep(1.3)
        print("This is of no importance to you")
        time.sleep(1.1)
        print("You are not scared of spiders")
        time.sleep(1)
    elif action == "forward":
        print("You start your voyage through the dungeon.")
        time.sleep(1)
        state["room"] = "middle"
    elif action == "quit":
        quit()
    else:
        print("Oi, you can't do that!")


def middle_room():
    print("You are in a room of the dungeon. There is a door ahead of you.")
    time.sleep(1.1)
    print("Curiosity seeps through you as you wonder what could be through the door.")
    time.sleep(1.4)
    if state["key"]:
        print("Actions available: forward, backward")
    elif state["looked_for_key"]:
        print("Actions available: forward, backward, look, pickup, pull lever")
    elif state["listened"]:
        print("After listening to that noise you start to become paranoid")
        time.sleep(1)
        print("You start to panic as you now believe you are not alone")
        time.sleep(1)
        print("All you hear now are the occaisonal droplets of water")
        time.sleep(1)
        print("Although this makes you even more scared")
        time.sleep(1)
        print("You want to leave now.")
        time.sleep(1)
        print("Actions available: forward, backward, search")
        time.sleep(1)
    else:
        print("Actions available: forward, backward, look, listen")
    action = input("> ")
    if action == "forward":
        if state["key"]:
            state["room"] = "exit"
        else:
            print("The door is locked.")
    elif action == "quit":
        quit()
    elif action == "backward":
        state["room"] = "start"
    elif action == "look":
        print("You notice the glint of a gold object catches your eye.")
        time.sleep(1.2)
        print("Once again curiosity takes control,")
        time.sleep(1.2)
        print("you venture forth to see what it is.")
        time.sleep(1.2)
        print("You aproach the object and notice it is a golden key")
        time.sleep(1.2)
        print("You stare in awe")
        time.sleep(1.1)
        print("And notice its the perfect shape and size for the lock in the door")
        time.sleep(1.4)
        print("There is also a lever on the wall")
        time.sleep(1.2)
        print("You wonder what would happen if you pulled it")
        time.sleep(1.2)
        state["looked_for_key"] = True
    elif action == "pickup":
        print("You picked up the key!")
        time.sleep(1)
        state["key"] = True
    elif action == "listen":
        print("In the stillness of the dungeon you hear a slight repeating noise")
        time.sleep(1.5)
        print("You move towards a wall")
        time.sleep(1.3)
        print("In hopes of hearing it better")
        time.sleep(1.5)
        print("What you hear sends shivers down your spine")
        time.sleep(1.5)
        print(".")
        time.sleep(1.2)
        print(".")
        time.sleep(1.2)
        print(".")
        time.sleep(1.2)
        print("Thowmp")
        time.sleep(1.5)
        print("Thwomp")
        time.sleep(1.5)
        state["listened"] = True
    elif action == "search":
        print("You decide to investigate deeper")
        time.sleep(1.2)
        print("Although every fibre of your body says not too")
        time.sleep(1.2)
        print("As you approach the wall for another time")
        time.sleep(1.2)
        print("You hear a low rumbling voice echo through the rooms of the dungeon")
        time.sleep(1.2)
        print("Monster: YOU DARE ENTER MY DUNGEON!!!")
        time.sleep(1.2)
        print("Monster: NOW YOU SHALL PAY!!")
        time.sleep(1.2)
        print("As you now realise that you shouldve lsitened to your gut")
        time.sleep(1.2)
        print("It is too late")
        time.sleep(1.2)
        print("You see the big green ogre approach you at ungodly speeds")
        time.sleep(1.2)
        print("Your last thoughts ironically being 'how did i get killed by shrek?'")
        time.sleep(1.3)
        print("Well thats it. You have one option left now.")
        time.sleep(1.2)
        print("I suppose you have no other choice then to restart now")
        time.sleep(1)
        state["room"] = "start"
    elif action == "pull lever":
        print("You pull the lever and the floor collapses under you")
        time.sleep(1.2)
        print("You slide down a slide like thing and find yourself in a new place")
        time.sleep(1.2)
        state["room"] = "tunnel"
    elif action == "quit":
        quit()
    else:
        print("Oi, you cant do that!")

def tunnel_room():
    print("You realise that you have found yourself in a deep dark tunnel")
    time.sleep(1.2)
    print("You evaluate your options and decide to make a choice")
    time.sleep(1.2)
    print("Actions available: forward, climb")
    action = input("> ")
    if action == "forward":
        print("Braving the dim light, you trust your instincts and venture forth")
        state["room"] = "tunnel_end"
    elif action == "climb":
        print("You listen to the rational side of your thoughts and decide to climb")
        time.sleep(1.2)
        print("This brings you back to the middle room of the dungeon")
        time.sleep(1.2)
        state["room"] = "middle"
    elif action == "quit":
        quit()

def tunnel_end():
    print("You now find yourself in an open room")
    time.sleep(1.1)
    print("You notice a big tree in the middle of the room")
    time.sleep(1.2)
    print("Somehow it is flourishing in this environment")
    time.sleep(1.2)
    print("The tree seems to be easy enough to climb")
    time.sleep(1.2)
    print("You now decide as to what to do")
    time.sleep(1.2)
    print("Actions available: climb tree, look")
    time.sleep(0.5)
    action = input("> ")
    if action == "climb tree":
        print("You decide to climb the tree and see what is up there")
        state["room"] = "tree"
    elif action == "look":
        print("You look around and see there is nothing of interest")
        time.sleep(1.2)
        print("The only thing here that is half interesting is the tree")
        time.sleep(1.2)
        print("You think it must be fun to climb it")
    elif action == "quit":
        quit()
    else:
        print("Oi, You cant do that!")

def tree():
    print("You find yourself at the top of the tree")
    time.sleep(1.2)
    print("At the top of the tree you spot a small hole in the wall")
    time.sleep(1.2)
    print("You may be able to crawl through it")
    time.sleep(1.2)
    print("There is another hole that faces down")
    time.sleep(1.2)
    print("That may be a good idea you think")
    time.sleep(1.2)
    print("Actions available: jump down, crawl, jump down hole")
    action = input("> ")
    if action == "jump down":
        print("You jump down the big tree")
        time.sleep(1.2)
        state["room"] = "tunnel_end"
    elif action == "crawl":
        print("You decide to crawl through the hole and see what is on the other side")
        time.sleep(1.2)
        print("It is a tight squeeze but you fit")
        time.sleep(1.2)
        print("After crawling through the tight tunnel")
        time.sleep(1.2)
        print("You notice the light at the end of the tunnel and decide to follow it")
        time.sleep(1.2)
        print("You exit the small tunnel")
        time.sleep(1.2)
        print("And end up in another small room, how fun")
        time.sleep(1.2)
        print("You notice a hole in the floor and decide thats the best way to go")
        time.sleep(1.2)
        print("This is because there is no other exit in sight")
        time.sleep(1.2)
        print("Actions available: drop")
        action = input("> ")
        if action == "drop":
            print("you find youself back at the door from earlier")
            time.sleep(1.2)
            print("But this time on the other side")
            time.sleep(1.2)
            print("You have reached the end of the dungeon")
            state["room"] = "exit"
    elif action == "jump down hole":
        print("You decide to jump down the hole")
        time.sleep(1.2)
        print("And find yourself in another room")
        time.sleep(1.2)
        print("It seems vaguely familiar")
        time.sleep(1.2)
        print("You realise that you are back in the middle of the tunnel")
        state["room"] = "middle"
    elif action == "quit":
        quit()

# this is the exit_dungeon function. It runs at the end of the game
# this is what will be said when you win the game.
def exit_dungeon():
    print("Congrats" + state["username"] + "!")
    time.sleep(0.6)
    print("You have unlocked the door!")
    time.sleep(0.6)
    print("And escaped the dungeon!!")
    time.sleep(0.6)
    print("You win!!")
    time.sleep(0.6)


#################################################
# THIS SECTION IS WHERE THE MAIN GAME CODE STARTS
welcome_dungeon()
while state["room"] != "quit":
    while state["room"] != "exit":
        if state["room"] == "start":
            start_room()
        elif state["room"] == "middle":
            middle_room()
        elif state["room"] == "tunnel":
            tunnel_room()
        elif state["room"] == "tunnel_end":
            tunnel_end()
        elif state["room"] == "tree":
            tree()
        elif state["room"] == "quit":
            quit()
    exit_dungeon()

# Write your code here :-)
