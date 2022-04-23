
def print_title_art():
  maze_art_m = " __      __\n|  \    /  |\n|   \  /   |\n| |\ \/ /| |\n| | \__/ | |\n"
  maze_art_a = "    ___\n   /   \\\n  / /_\ \\\n / /   \ \\\n/ /     \ \\\n"
  maze_art_z = " ________\n|_____   |\n     /  /\n    /  /\n   /  /____\n  |________|\n"
  maze_art_e = " _________\n|   ______|\n|  |_____\n|   _____|\n|  |______\n|_________|\n"
  print(maze_art_m + maze_art_a + maze_art_z + maze_art_e)
  

def print_two_tunnel_art():
  print("        _______                 _______")
  print("       /       \\               /       \\")
  print("      |         |             |         |")
  print("     /           \\           /           \\")
  print("     |            |         |            |")
  print("     |            |         |            |")
  print("     |            |         |            |")
  print("_____|            |_________|            |____")
  print("\n\n")
  
def print_three_tunnel_art():
  print("     ________       ________       ________")
  print("    /        \\     /        \\     /        \\")
  print("   |          |   |          |   |          |")
  print("   |          |   |          |   |          |")
  print("   |          |   |          |   |          |")
  print("___|          |___|          |___|          |___")
  
def print_skull():
  print("  _____")
  print(" /     \\")
  print("| () () |")
  print(" \\  ^  /")
  print("  |||||")
  print("  |||||")

print_title_art()

print("Find your way out of the maze")

input("Press any key to continue")
print("\n\n\n")

print("You see two paths in front of you")

print_two_tunnel_art()


user_input = input("Which one do you choose? 'Right' or 'Left' ")
if ((user_input == "Right") or (user_input == "right")):
  print("You go into the right tunnel and fall in a hole, meeting your demise.")
  print_skull()
else:
  print("There are two more more tunnels.")
  print_two_tunnel_art()
  user_input = input("Which one do you go in? 'Right' or 'Left'?")
  if ((user_input == "Left") or (user_input == "left")):
    print("You go into the right tunnel, and fall in a hole, meeting your demise.")
  else:
    print("Congrats! You made the right choice and made it out of the cave!")
