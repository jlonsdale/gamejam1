# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Maria", color="#c8a2c8")

image placeholder_neutral= "placeholder_neutral.png"
image placeholder_happy = "placeholder_happy.png"
image placeholder_angry = "placeholder_angry.png"
image placeholder_bored = "placeholder_bored.png"

# The game starts here.

label start:

    scene bg room

    show placeholder_neutral

    m "Hi, I'm Maria. How are you going to make me feel today?"

    menu:
        "Say something to Maria:"
        "You look great today!":
            show placeholder_happy
            m "Aww, thank you! That makes me happy."
        "I'm bored...":
            show placeholder_bored
            m "Oh, I guess I'm a bit bored too."
        "I don't like your outfit.":
            show placeholder_angry
            m "Oh... that makes me mad."

    m "Thanks for talking to me!"

    return
