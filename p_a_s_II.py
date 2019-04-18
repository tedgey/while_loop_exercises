# print a square II - user chooses square size

square_size_input = input("How long should the square's sides be? ")

square_size_length = int(square_size_input)

symbol_count = square_size_length * ("*")

counter = 0

while counter < square_size_length:
    counter = counter + 1
    if counter <= square_size_length:
        print(symbol_count)