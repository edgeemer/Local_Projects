"""There are 9 white, 8 green and 7 blue balls in the box. How many variations can be made from three balls,
where two are the same color? """

from itertools import permutations

white_balls_number, black_balls_number, blue_balls_number = 9, 8, 7
total_balls_number = white_balls_number + black_balls_number + blue_balls_number
selection_length = 3

white_balls = ["WHITE" for _ in range(0, white_balls_number)]
black_balls = ["BLACK" for _ in range(0, black_balls_number)]
blue_balls = ["BLUE" for _ in range(0, blue_balls_number)]
all_balls = white_balls + black_balls + blue_balls

final_selection = {}
variant_counter = 0

for variant in permutations(all_balls, r=selection_length):
    white_counter, black_counter, blue_counter = 0, 0, 0

    for ball in variant:
        if ball == "WHITE":
            white_counter += 1
        elif ball == "BLACK":
            black_counter += 1
        elif ball == "BLUE":
            blue_counter += 1

    if white_counter >= 2 or blue_counter >= 2 or blue_counter >= 2:
        variant_counter += 1
        final_selection[f"Variant {variant_counter}"] = variant

for variant_number, variant in final_selection.items():
    print(f"{variant_number}: ", end="")
    print(*variant, sep=", ")
