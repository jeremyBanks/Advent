from AOC_Functions import read_lines


def main():

    frequency = 0
    set_of_frequencies = {0}
    first_double = 0

    input = read_lines("input201801.txt")

    while True:
        for line in input:

            if line[0] == "+":
                modifier_is_positive = True
            elif line[0] == "-":
                modifier_is_positive = False

            line_value = line[1:]

            if modifier_is_positive == True:
                frequency += int(line_value)
            if modifier_is_positive == False:
                frequency -= int(line_value)

            if frequency in set_of_frequencies:
                first_double = frequency
                break

            set_of_frequencies.add(frequency)

        if first_double == frequency:
            break

    print(first_double)


main()
