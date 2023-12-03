from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    calibration = 0
    for line in input:
        num = ''
        curr_digit = ''
        for c in line:
            if c.isdigit():
                curr_digit = c
                if num == '':
                    num += c
        num += curr_digit
        calibration += int(num)
    print(calibration)


if __name__ == "__main__":
    main(argv[1])

        