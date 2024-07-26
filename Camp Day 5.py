

import random

def start():
    print("You wake up in your bedroom.")
    choice = input("You hear your mom yelling at you to get down here.\nWhat do you do?:\n\n[1]Go downstairs to see your mom\n[2]Ignore your mom and stay in your comfy bed\n:")
    if choice == "1":
        print("You run downstairs to see why your mom is yelling.")
        mom()
    elif choice == "2":
        print("You wait 5 minutes then you see your mom walking up the stairs beating a rolling pin in her hand. You dodge the first swing and run downstairs to save yourself.")
        mom()
    else:
        print("Thats not 1 or 2!")
        start()


def main():
    print("Press Enter to Start!")
    input()
    start()

def mom():
    choice = input("When your downstairs in the kichtin you see that your mom has prepaired a bearly alive fried bulbasaur. Your mouth is watering looking at the bulbasaur. Your mom is looking intently at you right now\nWhat do you do?:\n\n[1]Mecilessly eat the bulbasaur, pretending to not notise its heartbeat to please your mother\n[2]Pretend that you're not hungery and try to smuggle the bulbasaur out of your house, without your mother noticing\n:")
    if choice == "1":
        print("You eat the bulbasaur, trying not to cry as you see the light leave its eyes. You mom look splended and you walk out the door to oak's lab while hoping you can keep your breakfast down.")
        deadbulb()
    elif choice == "2":
        print("You tell your mom you're not hungery and ''accidentally'' knock over the plater of bulbasaur. It looks terrorfied at you when you walk torward it, But you scoop it up and walk out the door without your mother noticing.")
        savebulb()
    else:
        print("Thats not 1 or 2!")
        start()


def pigey_incounter():
    pmove = random.randint(1,3)
    if pmove == 1:
        print("The wild pigey used tackle!")
    elif pmove == 2:
        print("The wild pigey used sand attack!")
    elif pmove == 3:
        print("The wild pigey used gust!")

def deadbulb():
    choice = input("Thankfully you keep your breakfast down and you make it to oak's lab. When you open the doors you see the professor and his son Garry sitting infront of a table with three pokeballs on it. Professor Oak tells you and Garry its time to pick a pokemon. Garry is excited and grabs the first pokeball and says ''I Want This One!'' and he throws it to see the pokemon inside. He throws it and a bulbasaur pops out. Your gag reflex instantly activates and you run out of Oak's lab as fast as you can. You run into the wood as you throw up chunks bulbasaur that you had as breakfast. Well, at least what was left of it.\nWhat do you do?:\n\n[1]Run out of the wood as fast as you can and try not to throw up again. Telling Oak and Garry that you had leave for a second and go on with you day\n[2]Carry the remaining peaces of the bulbasaur deeper into the forest and dig a grave for the bulbasaur, risking getting attack by a wild pokemon\n:")
    

def savebulb():
    choice = input("You rush to the pokecenter and demand that your bulbasaur gets healed immediately. The nurses complie and your bulbasaur is healed. The nuses hand you back your bulbasaur and ask if you would like a pokeball to put it in. The nurse pulls out a pokeball and bulbasaur looks at it very nervessly and tries to hide behind you.\nWhat do you do?:\n\n[1]Force bulbasaur into the pokeball and be on your way\n[2]Decline the pokeball and walk out the door with a wild, uncantained bulbasaur\n:")
    if choice == "1":
        print("You take the pokeball and bulbasaur is backing agaist the wall. Fear in its eyes. The bulbasaur is struggling and fighting you, but you eventually get it into the pokeball and leave the pokecenter for oak's lab")
    elif choice == "2":
        print("You decline the pokeball and the nurse puts it away. Bulbasaur looks releaved immdiately. You and bulbasaur walk out the doors comfortly. Bulbasaur even rubs affectionately agaist your leg on the way out.")
    else:
        print("Thats not 1 or 2!")
        start()
    








main()
