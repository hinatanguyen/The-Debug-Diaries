# TODO: Add dialogue for this scene (this might take a long time)
# TODO: Add music, sound effects, and background art (Im broke T^T)

label prologue:

# Beginning Scene

    "Have you ever dreamed of a moment so vivid, it felt like a memory?"

    "Not the kind of dream with dragons or flying cars. I mean the quiet kind—the ones that feel like they could've happened yesterday, or maybe tomorrow."

    "In mine, I'm standing in the rain. No umbrella. No shelter. Just the cold soaking through my hoodie and the weight of another day that didn't go the way I hoped."

    "The city around me is blurred—neon signs flickering like broken pixels, headlights streaking past like ghost data. My phone's dead. My resume is damp and crumpled in my bag."

    "I had just come from another interview. Another polite rejection. Another reminder that my dream of making games people actually cared about was still out of reach."

    "I wanted to build something beautiful. Something that made people feel seen. Something that mattered."

    "But all I had was a soaked hoodie, a half-finished portfolio, and the creeping doubt that maybe I wasn't good enough."

    "And then... she appeared."

    "A stranger. She didn't say a word. Just stepped beside me, held out her umbrella, and smiled."

    "It wasn't a dramatic moment. No swelling music. No slow-motion. Just a quiet gesture in the middle of a storm."

    "We walked together, side by side, through the rain. Her presence was calm, like a loading screen that didn't rush you."

    "I didn't know her name. I didn't know why she helped me. But I remember the feeling."

    "The warmth of shared silence. The comfort of not having to explain myself. The way her umbrella tilted slightly toward me, like she was making space for more than just my body."

    "That small act of kindness... it stayed with me."

    "Maybe it was just a dream. Or maybe it was something I've been waiting for—not just someone to walk with, but someone who sees the version of me I'm still trying to become."

    "Someone who doesn't mind the bugs in my personality. Someone who doesn't need me to be perfect code."

    "In that moment, I wasn't a failed applicant. I wasn't a lonely dev. I was just... me. And that was enough."

    "We reached my doorstep. I turned to thank her, but she was already walking away."

    "No name. No goodbye. Just a smile that felt like a soft reboot."

    "I watched her disappear into the rain, and for the first time in weeks, I felt something other than tired."

    "Hope."

# Wake up screen transition

    "I wake up to the sound of my alarm and the soft light of morning."

    "The rain is gone. The dream fades."

    "But something about it lingers—like a promise waiting to be fulfilled."

    "Today's my first day at Studio Kairo. A real dev team. A real chance."

    "I don't know who she is yet. Maybe she's just a figment of my imagination. Or maybe she's out there, somewhere in the code of my life, waiting to be compiled."

    "Either way, I'm ready to start."

    jump chapter0

label chapter0:    

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





    