from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    

    summed_powers = 0

    for line in input:
        subgames = [x.split(', ') for x in line.split(': ')[1].split('; ')]

        limits = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }

        for subgame in subgames:
            for dice_shown in subgame:
                [number, color] = dice_shown.split(' ')
                limits[color] = max(limits[color], int(number))
            
        summed_powers += limits['red'] * limits['green'] * limits['blue']

    print(summed_powers)





if __name__ == "__main__":
    main(argv[1])

        