# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pov = Character("[name]")
define sakura = Character("Sakura")
default affection = 0
default abroad = False
default ask = False

# The game starts here.

label start:

    $pov = renpy.input("What is your name?", length=32)
    $pov = pov.strip()
    if not pov:
        $pov = "Sans"
    "???" "[pov]! Hey! Wake up!"
    "???" "Hey! School is over!"
    scene bg classroom
    with fade
    pov "Ugh... Who are you?"
    show sakura laugh with dissolve
    "???" "It's Sakura! The only Sakura you've known since childhood!"
    pov "Oh, hey... Looks light I slept though class again huh?"
    show sakura smile
    sakura "Yeah... about that."
    pov "How late is it?"
    show sakura smile2
    sakura "Maybe... five thirty-ish?"
    pov "Five-thirty! Why didn't anyone wake me up! And why are you still here!"
    sakura "Well everyone in class tried, but you were sound asleep."
    sakura "As for me. Well... I was doing club activites of course!"
    pov "..."
    sakura "..."
    show sakura smile
    sakura "Um, do you want to walk home togehter?"
    menu:
        "Accept":
            $affection += 1
            pov "Sure!"
            show sakura smile2
            sakura "Okay then. Let's go!"
            jump evaluate_end_1
        "Deny":
            $affection -= 1
            pov "Sorry, I want to go straight home and sleep."
            show sakura sad
            sakura "Okay then. See you later."
            jump evaluate_end_1

label evaluate_end_1:
    if affection >= 1:
        jump scene_2
    else:
        jump bad_end_1



label bad_end_1:
    scene black
    with fade
    "After that day, we saw each other less and less, and eventually, we never saw each other again."
    "It was if she wanted to tell me something."
    "Maybe I'll never know what she wanted to say."
    "Bad End"
    return



label scene_2:
    scene bg street
    with fade
    show sakura smile with dissolve
    sakura "It's been a while since we walked home from school together."
    pov "I don't consider one week to be a while."
    show sakura annoyed
    sakura "While it is for me!"
    "As we walk home, she takes me to some kind of detour."
    menu:
        "Ask":
            $affection += 1

        "Don't say anything":
            $affection += 1

        "Go home":
            $affection -= 1
            jump bad_end_1


label ask:
    $ ask = True
    pass

label nothing:
    pass


    return
