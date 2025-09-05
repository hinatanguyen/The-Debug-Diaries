# TODO: Add dialogue for this scene (this might take a long time)
# TODO: Add music, sound effects, and background art (Im broke T^T)

label chapter2:

# Scene 4: Onsen Retreat - Arrival

# TODO: Write story sprite for this scene

# Choices for Scene 4
label compliment_choice:
    menu:
        "Compliment Kasuka sincerely.": # well well well
            $ kasuka_affection += 1
            jump chapter2_a
        "Compliment someone else.": # Implement this for multiple characters later
            jump chapter2_b

label chapter2_a:
    # TODO : Add dialogue for this scene (this might take a long time)
    jump chapter2_common_1

label chapter2_b:
    # TODO : Add dialogue for this scene (this might take a long time)
    jump chapter2_common_1

label chapter2_common_1:
    # Continue the story flow

# Scene 5: Scavenger Hunt Pairing

# TODO: Write story sprite for this scene

# Choices for Scene 5
label forest_scene_choice:
    menu:
        "I'm glad I got lost with you.": # ???
            $ flag_forest = True
            $ kasuka_affection += 1
            jump chapter2_c
        "This is a waste of time.":
            $ kasuka_affection -= 1
            jump chapter2_d

label chapter2_c:
    # TODO : Add dialogue for this scene (this might take a long time)
    jump chapter2_common_2

label chapter2_d:
    # TODO : Add dialogue for this scene (this might take a long time)
    jump chapter2_common_2

label chapter2_common_2:
    # Continue the story flow

# Jump to chapter 3 after chapter 2 end
    jump chapter3