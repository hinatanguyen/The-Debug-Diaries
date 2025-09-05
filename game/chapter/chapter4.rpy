# TODO: Add dialogue for this scene (this might take a long time)
# TODO: Add music, sound effects, and background art (Im broke T^T)


label chapter4:

# Scene 8: Valentine's Day - Love Jam 

# TODO: Write story sprite for this scene

# Choices for Scene 8
label love_jam_choice:
    menu:
        "Choose Kasuka as your partner.":
            $ flag_love_jam_partner = True
            $ kasuka_affection += 1
            jump ending_check
        "Choose someone else.": # Implement this for multiple endings later
            jump ending_check

# Check for Specific Ending
label ending_check:

    # Kasuka Happy Ending
    if kasuka_affection >= 5 and flag_confession and flag_love_jam_partner:
        jump kasuka_ending

    # Kasuka Normal Ending
    elif (kasuka_affection >= 4 and flag_love_jam_partner) or (
        kasuka_affection >= 3 and flag_confession and flag_love_jam_partner and 
        (flag_encourage_draw or flag_forest)
    ):
        jump kasuka_normal_ending

    # Kasuka Bad Ending
    else:
        jump kasuka_bad_ending

