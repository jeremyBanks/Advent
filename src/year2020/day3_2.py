from .. import viz
from ..functions import run_solution, read_input_and_store_values_in_nested_list
import math

input_filename = "./inputs/202003.txt"
expected_output = 5140884672


def solution(input_lines):
    input_lines = input_lines[:64]

    slopes_to_check = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    slope_tree_counts = []

    nested_list_containing_input = read_input_and_store_values_in_nested_list(
        input_lines
    )

    trees = viz.new_layer(z=-1, color=(0x00, 0x80, 0x20))
    for line_index, line in enumerate(nested_list_containing_input):
        for character_index, character in enumerate(line):
            if character == "#":
                trees.dot_at(character_index, line_index)

    for slopes in slopes_to_check:
        slope_tree_counts.append(
            trees_encountered_on_given_slope(slopes, nested_list_containing_input)
        )

    answer = math.prod(slope_tree_counts)
    print(f"answer: {answer}")


def trees_encountered_on_given_slope(slope, nested_list_containing_input):
    layer = viz.new_layer()

    trees_encountered_on_path = 0

    first_line = True
    distance_to_bottom = 0

    for line in nested_list_containing_input:
        distance_to_bottom += 1

    current_line_count = 2
    current_location_on_line = 0

    skip_line_counter = slope[1]

    first = True
    for line in nested_list_containing_input:
        if first_line == True:
            first_line = False
            continue

        if skip_line_counter > 1:
            skip_line_counter -= 1
            continue

        if skip_line_counter == 1:
            skip_line_counter = slope[1]

        current_location_on_line += slope[0]
        wrapped = current_location_on_line >= len(line)

        current_location_on_line = current_location_on_line % len(line)

        if wrapped or first:
            layer.move_to(current_location_on_line, current_line_count)
        else:
            layer.line_to(current_location_on_line, current_line_count)
        first = False

        if line[current_location_on_line] == "#":
            trees_encountered_on_path += 1

            layer.dot_at(current_location_on_line, current_line_count)

        else:
            pass

        current_line_count += 1

    print(f"trees_encountered_on_path: {trees_encountered_on_path}")

    return trees_encountered_on_path


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
