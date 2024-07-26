



pokemon = ["Magikarp", "Venusaur", "Venonat", "Slowpoke", "Seel", "Mankey"]
questions = ["Guess this pokemon off it pokedex entery:\n An underpowered, pathetic Pokémon. It may jump high on rare occasions but never more than seven feet.", "Guess this pokemon off it pokedex entery:\n While it basks in the sun, it can convert the light into energy. As a result, it is more powerful in the summertime.", "Guess this pokemon off its pokedex entery:\n Poison oozes from all over its body. It catches small bug Pokémon at night that are attracted by light.", "Guess this pokemon off its pokedex entery:\n It is incredibly slow and dopey. It takes five seconds for it to feel pain when under attack.", "Guess this pokemon off its pokedex entery:\n The protrusion on its head is very hard. It is used for bashing through thick ice.", "Guess this pokemon off its pokedex entery:\n It lives in groups in the treetops. If it loses sight of its group, it becomes infuriated by its loneliness."]
          





score = 0
for i in range(len(questions)):
    print(questions[i])
    guess = input("\n:")
    answer = pokemon[i]
    if guess.lower() == answer.lower():
        print("Its " + pokemon[i] + "! You got it!")
        score += 1
    else:
        print("\nIncorrect! The answer was " + pokemon[i] + ".")

print("You got " + str(score) + "/" + str(len(questions)) + " correct!")


    ##################
##########O##############
    #####/|\######
#########/ \#########
    ###################


































'''input("Would you like to gamble?\n")
print("Who are we kidding, of couse you would!\n")
print("Okay, here we go!\n")

import random
x = 0
coins = 10
while x < 8:
    cards = random.randint(1, 32)
    if cards >= 11:
        print("Commen Card")
        coins += 1
    elif cards <= 10 and cards > 2:
        print("Rare Card")
        coins += 5
    elif cards <= 2:
        print("SUPER RARE CARD!")
        coins += 15
    x += 1
print(coins)
coins -= 10
print(coins)
input("Would you like to gamble again?\n")
print("Who are we kidding, of couse you would!\n")
x -= 8
'''
