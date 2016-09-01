"""
10 colour names and their hex codes in a dictionary.
Input a colour name and the hex code is returned.
"""

COLOUR_NAMES = {"Alice Blue": "f0f8ff", "Cadet Blue": "#5f9ea0",
                "Cornflower Blue": "#6495ed", "Dark Olive Green 2": "#bcee68",
                "Dark Orchid": "#9932cc", "Dark Sea Green": "#8fbc8f"}

print(COLOUR_NAMES)

colour = input("Please enter a colour (use spaces to separate the words): ").title()
while colour != "":
    if colour in COLOUR_NAMES:
        print("Your colour hex code is {}".format(COLOUR_NAMES[colour]))
    else:
        print("Sorry, try again")
    colour = input("Please enter a colour (use spaces to separate the words)").title()
