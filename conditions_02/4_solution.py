"""Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)"""

fruits_dict = {
    "banana" : {
        "yellow" :"awasome ! it is ready to eat",
        "green" : "unripe. Wait ! It is not edible",
        "black" :"It may be rotten inside, plz avoid",
        } ,
    "apple" : {
        "yellow" : "normal and delicious!",
        "green" : "tart and refreshing!",
        "red" : "awasome ! it is ready to eat",
        "brown" : "It may be rotten inside, plz avoid"
        },
    "mango" : {
        "yellow" : "ripe , sweet and juicy!",
        "green" : "Wait ! It is not edible. its taste maybe firm and crunchy!",
        "black" : "overripe and mushy",
        }
}

fruit_input = input("Enter the name of any one fruit from banana, apple and mango :").lower()

if fruit_input in fruits_dict :
    color_input = input("Enter the fruit color :").lower()
    if color_input in fruits_dict[fruit_input]:
        ripness = fruits_dict[fruit_input][color_input]
        print(f"{color_input} {fruit_input} is {ripness}")
    else:
        print(f"Sorry, there is no {color_input} state for {fruit_input}. Please try a different color.")
else:
    print(f"Sorry, we don't have information on {fruit_input}. Please choose from banana, apple, or mango.")
    