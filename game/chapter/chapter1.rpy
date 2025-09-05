# TODO: Add dialogue for this scene (this might take a long time)
# TODO: Add music, sound effects, and background art (Im broke T^T)

label chapter1:
    

# Scene 2: Friday Bento Swap

# Choices for Scene 2

label bento_reaction:
    menu:
        "This is amazing! Did you make it yourself?": # Kasuka is a great cook after all
            $ kasuka_affection += 1
            jump chapter1_a
        "Im not really into homemade stuff.": # I'm disappointed......
            jump chapter1_b

label chapter1_a:
    # TODO : Add dialogue for this scene (this might take a long time)
    jump chapter1_common_1

label chapter1_b:
    # TODO : Add dialogue for this scene (this might take a long time)
    jump chapter1_common_1

label chapter1_common_1:
    # Continue the story flow


# Scene 3: After Work Chat

# Choices for Scene 3

label manga_dream:
    menu:
        "You should draw again. I'd love to see your work.": # well well well well well *insert evil laugh*
            $ flag_encourage_draw = True
            $ kasuka_affection += 1
            jump chapter1_c
        "Sound like a lot of work. Maybe another time.":
            jump chapter1_d

label chapter1_c:
    # TODO : Add dialogue for this scene (this might take a long time)
    jump chapter1_common_2

label chapter1_d:
    # TODO : Add dialogue for this scene (this might take a long time)
    jump chapter1_common_2

label chapter1_common_2:
    # Continue the story flow    

# Jump to chapter 2 after chapter 1 end
    jump chapter2