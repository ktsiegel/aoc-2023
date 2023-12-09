from sys import argv

def get_score(line):
    components = line.split(': ')[1]
    winning_numbers = set([int(x) for x in (components.split(' | ')[0]).strip().split()])
    my_numbers = set([int(x) for x in components.split(' | ')[1].strip().split()])
    inters = len(winning_numbers.intersection(my_numbers))
    if inters == 0:
        return 0
    return 2 ** (inters-1)


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    total_points = 0
    for line in input:
        score = get_score(line)
        total_points += score

    print(total_points)


if __name__ == "__main__":
    main(argv[1])

        