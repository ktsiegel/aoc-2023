from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    grid = []
    for line in input:
        gridline = []
        for c in line:
            gridline.append(c)
        grid.append(gridline)

    schematic = 0
    for i in range(len(grid)):
        j = 0
        while j < len(grid[i]):
            if grid[i][j] in '1234567890':
                # we have found a number
                curr_num = ''
                initial_j = j
                while j < len(grid[i]) and grid[i][j] in '1234567890':
                    curr_num += grid[i][j]
                    j += 1
                parsed_num = int(curr_num)
                
                # now check if there are any symbols bordering it
                for border_i in range(i-1, i+2):
                    for border_j in range(initial_j-1, j+1):
                        if border_i < 0 or border_j < 0 or border_i >= len(grid) or border_j >= len(grid[i]):
                            continue
                        if border_i == i and border_j >= initial_j and border_j < j:
                            continue
                        if grid[border_i][border_j] not in '1234567890.':
                            # found a symbol
                            schematic += parsed_num
            j += 1

    print(schematic)


if __name__ == "__main__":
    main(argv[1])

        