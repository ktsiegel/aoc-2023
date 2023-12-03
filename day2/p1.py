from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    limits = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    possible_id_sum = 0

    for line in input:
        subgames = [x.split(', ') for x in line.split(': ')[1].split('; ')]
        game_num = line.split(': ')[0].split(' ')[1]

        possible = True
        for subgame in subgames:
            for dice_shown in subgame:
                [number, color] = dice_shown.split(' ')
                if limits[color] < int(number):
                    possible = False
                    break
            if not possible:
                break
            
        if possible:
            possible_id_sum += int(game_num)

    print(possible_id_sum)




if __name__ == "__main__":
    main(argv[1])

        