#checking conditions

isRaining = True
if isRaining:
    print("It is raining outside.\n")
else:
    print("It is not raining outside.\n")

#testing equality
password = "pyG@me"
user_input = "pyG@me"
if password==user_input:
    print("User password is correct.\n")
else:
    print("User password is incorrect.\n")

#using game code values
x = 255
y = 678

player_x = 255
player_y = 678

if(x == player_x and y == player_y):
    print("Display next objective.")
else:
    print("Move to the marked spot.")