# TODO: Add dialogue for this scene (this might take a long time)
# TODO: Add music, sound effects, and background art (Im broke T^T)

label chapter0:

# Beginning Scene
    "Have you ever had one of those days where everything seems to go wrong, but then a small act of kindness from a friend turns it all around?"
    "That's exactly what happened to me today."
    "It all started when I was caught in a sudden downpour without an umbrella."
    "I was drenched and feeling pretty miserable when Kasuka, my coworker, noticed me struggling."
    "Without hesitation, she offered me her umbrella and walked me home."
    "That simple gesture made my day so much better."
    "We chatted along the way, and I couldn't help but feel a little spark between us."
    "Maybe it was the rain, or maybe it was just Kasuka's kindness, but I found myself looking forward to our next encounter."
    "As we reached my doorstep, I thanked her for the umbrella and the company."
    "She smiled and said it was no problem at all."
    "I watched her walk away, feeling grateful and a bit hopeful."
    "Sometimes, it's the little things that make the biggest difference."
    "And today, Kasuka's kindness was exactly what I needed."

# Scene 1: Studio Entrance


# Choices for Scene 1

label kasuka_walk_home_choice:
    menu:
        "Thank for the umbrella. You're really thoughtful.":
            $ flag_walk_home = True
            $ kasuka_affection += 1
            jump choices1_a

        "I could've handled it myself.":
            jump choices1_b

label choices1_a:
    main "" # I forgot what to put here, please fix it
    k "Don't mention it! I just wanted to make sure you didn't get soaked."
    jump choices_common

label choices1_b:
    main "" # You little brat, dumbass
    k "Well, I just thought it would be nice to walk you home since it's raining." # Change it, It doesn't make sense!!
    jump choices_common

# Continue the story flow

label choices_common:
    main "Anytime! Let's celebrate with some ice cream later."
    k "Sounds like a plan!"



# Jump to chapter 1 after chapter 0 end
    jump chapter1





    