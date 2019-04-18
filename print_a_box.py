# Print a box with a given height and width

box_width_input = input("What should the width of the box be? ")

box_width = int(box_width_input)

box_height_input = input("What should the height of the box be? ")

box_height = int(box_height_input)

width_count = box_width * ("*")

inner_width_count = box_width - 2

inner_width_set = inner_width_count * (" ")

inner_width = ("*" + str(inner_width_set) + "*")

counter = 0

print(width_count)

while counter < box_height:
    counter = counter + 1
    if counter < box_height - 1:
        print(inner_width)
    
print(width_count)