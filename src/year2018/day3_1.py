from ..functions import run_solution

input_filename = "./inputs/201803.txt"
expected_output = None


def solution(input_lines):

    list_of_components = extract_components_of_lines(input_lines)

    square_inches_with_overlapping_claim = determine_locations_with_overlapping_claims(
        list_of_components
    )

    return square_inches_with_overlapping_claim


def determine_locations_with_overlapping_claims(list_of_components):

    locations_claimed = []
    locations_with_overlapping_claims = [list_of_components]

    for component in list_of_components:
        current_x_coordinate = 0
        current_y_coordinate = 0

        current_x_coordinate += component.starting_corner[0]
        current_y_coordinate += component.starting_corner[1]

        if (current_x_coordinate, current_y_coordinate) in locations_claimed:
            pass
        else:
            locations_claimed.append((current_x_coordinate, current_y_coordinate))

        x_modifier = 0
        y_modifier = 0

        for x_squares in range(component.sides[0]):
            for y_squares in range(component.sides[1]):
                y_modifier += 1

                adjusted_coordinates = (
                    current_x_coordinate + x_modifier,
                    current_y_coordinate + y_modifier,
                )

                if (
                    adjusted_coordinates in locations_claimed
                    and adjusted_coordinates not in locations_with_overlapping_claims
                ):
                    locations_with_overlapping_claims.append(adjusted_coordinates)
                else:
                    locations_claimed.append(adjusted_coordinates)

            x_modifier += 1

    return len(locations_with_overlapping_claims)


class LineComponent:
    def __init__(self, id, starting_corner, sides):
        self.id = id
        self.starting_corner = starting_corner
        self.sides = sides


def extract_components_of_lines(input_lines):

    list_of_components = []

    for line in input_lines:
        line_components = line.split()
        line_components.pop(1)

        id_component = int(line_components[0].strip("#"))

        starting_corner_values = line_components[1].strip(":").split(",")
        starting_corner_component = (
            int(starting_corner_values[0]),
            int(starting_corner_values[1]),
        )

        sides_compenent_values = line_components[2].split("x")
        sides_component = (
            int(sides_compenent_values[0]),
            int(sides_compenent_values[1]),
        )

        component = LineComponent(
            id_component, starting_corner_component, sides_component
        )

        list_of_components.append(component)

    return list_of_components


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
