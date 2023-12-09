from sys import argv

def get_score(line):
    components = line.split(': ')[1]
    winning_numbers = set([int(x) for x in (components.split(' | ')[0]).strip().split()])
    my_numbers = set([int(x) for x in components.split(' | ')[1].strip().split()])
    return len(winning_numbers.intersection(my_numbers))

def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    current_idx = 0
    scratchcard_tally = [1]*len(input)
    while current_idx < len(input):
        current_score = get_score(input[current_idx])
        for i in range(current_idx+1, current_idx+current_score+1):
            scratchcard_tally[i] += scratchcard_tally[current_idx]
        current_idx += 1

    print(scratchcard_tally)
    print(sum(scratchcard_tally))


if __name__ == "__main__":
    main(argv[1])

        