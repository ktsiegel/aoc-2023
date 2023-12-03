from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]


    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    calibration = 0
    for line in input:
        num = ''
        curr_digit = ''
        for cindex in range(len(line)):
            c = line[cindex]
            if c.isdigit():
                curr_digit = c
                if num == '':
                    num += c
            else:
                for digit in digits:
                    if digit == line[cindex:cindex + len(digit)]:
                        curr_digit = digits.index(digit) + 1
                        if num == '':
                            num += str(curr_digit)
        num += str(curr_digit)
        calibration += int(num)
    print(calibration)


if __name__ == "__main__":
    main(argv[1])

        