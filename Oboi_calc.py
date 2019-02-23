lengh_of_the_room = float(input("Enter the length of the room "))
width_of_the_room = float(input("Enter the width of the room "))
ceiling_height = float(input("Enter the ceiling height in the room "))
roll_width = float(input("Enter the roll width "))
roll_length = float(input("Wallpaper roll length "))
wight_for_formul = int((lengh_of_the_room*2+width_of_the_room*2)/roll_width)
roll_length_for_formul = int(roll_length/(ceiling_height+0.1))

print(int(wight_for_formul/roll_length_for_formul))