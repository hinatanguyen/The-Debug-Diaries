# TODO: Add dialogue for this scene (this might take a long time)
# TODO: Add music, sound effects, and background art (Im broke T^T)

label chapter3:

# Scene 6: Studio Stress

# TODO: Write story sprite for this scene


# Scene 7: Balcony Confession 

# TODO: Write story sprite for this scene

# Choices for Scene 7
label balcony_confession_choice:
    menu:
        "I want you to stay with me. With me.":
            $ flag_confession = True
            $ kasuka_affection += 1
            jump chapter3_a

        "You should take the job.":
            jump chapter3_b

label chapter3_a:
    main "I really love u so please stay with me." #Ewwwwwwwwwwwww I cannot believe I wrote this

# TODO: Add more dialogue until common jump and fix above line because ewwwww its cringe
    jump chapter3_common

label chapter3_b:
    main "I think you should take the job. It's a great opportunity for you." #Sad but realistic, me fr

# TODO: Add more dialogue until common jump
    jump chapter3_common

label chapter3_common:

# Jump to chapter 4 after chapter 3 end
    jump chapter4