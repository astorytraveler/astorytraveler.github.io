print("You are a magical vulture familiar and your master is a young witch. You just broke one of your masters potion. The good news is that you remember that it was from a teasure chest that she found in a dungeon. The problem is that she counted how many potions she had and will most likely find you are the reason she is down one potion. You have observe your master making potion, but have never tried yourself. But as they say, there is no time like the present, because right now if you can't get a new potion, lets just say there are going to be some horrible consequences.")





answer = input("You decide to fly to your master potion room. Thankfully as a magical familiar you are able to conjure some fire to start the stove. You see a great assortment of potion ingedients and two catch your eye, a fermented SHEIRKSHROOM, or elemental CORE. Which one do you chose too put in the pot as your main ingediant.")

if answer.upper().strip() == "SHEIRKSHROOM":
    print("You slowing see the liquid in the cualdron turn purple.")
    answer = input("You fly around in the room looking what you feel would work well for your new potion. You can't decide if you should put an EYE of a basilisk or sonicboom FROG.")
    if answer.lower().strip() == "eye":
        answer = input("That didn't seem to change the potion that much. It is bubbling a bit more but you feel like it needs some strong. You can either put in a SEED of terrible darkness or mythril DUST")
        if answer.lower().strip() == "seed":
            print("You have just made the worst choice of your life. Enjoy being chased by a huge hungrey demon. Really what were you thinking. It didn't get the name of terrible for nothing.")
        elif answer.lower().strip() == "dust":
            print("The potion has somewhat changed and gained a hue that is a mix of purple and blue. By your magical senses you feel this can help the drinker sense any nearby undead. Not very interesting but should do the trick in keeping you from trouble.")
        else:
            print("That is not one of the paths you are able to choose from.")
    elif answer.lower().strip() == "frog":
        answer = input("Finally put that frog into the cualdron. It was rather noisy to say the least. You feel this potions needs some elemental crystals to finish it off. Do you put WIND, ICE or ELETRIC crystals into the potion.")
        if answer.lower().strip() == "ice":
            print("You might of put too many ice crystals in the cualdron as the potion has now frozen. Even though there is a fire under it. And making the fire bigger doesn't seem to be helping.")
        elif answer.lower().strip() == "wind":
            print("Great job. You have open a tornado that has sucked you into the plane of elemental air. Good thing you can fly.")
        elif answer.lower().strip() == "eletric":
            print("While a few sparks do seems to come out of the potion, over all it seems you have succeeded. You have created a potion that gives the drinker an eletrical orb that moves around and defends them")
        else:
            print("That is not one of the paths you are able to choose from.")
    else:
            print("That is not one of the paths you are able to choose from.")
        


elif answer.lower().strip() == "core":
    print("A fire roars burning a few of your feathers from the cualdron")
    answer = input("You feel like it needs to be stir to help cool it down. Do you decide to stir it CLOCKWISE or COUNTER clockwise.")
    if answer.lower().strip() == "clockwise":
        answer = input("As you stir it cools down and bubbles without any major problems. You decide that you need something exotic to help create this potion. You are thinking of using a glob of SLIME from the deadly gelatinous cube or HAIR from the legendary Thunderwolf.")
        if answer.lower().strip() == "slime":
            print("Fear swells up inside of you as you see the glob starts to absorb the potion in the cualdron. The slime then starts to crawl out of the cualdron and towards you. You decide the best option is to leave.")
        elif answer.lower().strip() == "hair":
            print("The potion is complete. The only problem is you don't know how to get near it to scoop enough for a potion as getting near it keeps shocking you. So close to solving your problem, yet so far. You guess your choice was a bit too powerful for a potion.")
        else:
            print("That is not one of the paths you are able to choose from.")
    elif answer.lower().strip() == "counter":
        answer = input("The cualdron shreiks violently. Nearby are two ingediants, a strange FRUIT that you haven't seen before and a large slab of SALT. What do you decide to put in the cauldron.")
        if answer.lower().strip() == "fruit":
            print("Well that didn't go well. The potion has exploded along with the room. Your situation has gone form bad to worse.")
        elif answer.lower().strip() == "salt":
            print("The cualdron seems to have calmed down creating a potion that helps in warding of elemental beings. You live to see another day.")
        else:
            print("That is not one of the paths you are able to choose from.")
    else:
        print("That is not one of the paths you are able to choose from.")
else:
     print("That is not one of the paths you are able to choose from.")
