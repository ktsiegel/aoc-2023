from sys import argv


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    grid = []
    for line in input:
        grid.append([x for x in line])

    start = (0,0)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = (i,j)
                break

    queue = [(start[0], start[1], 0)]
    visited = set()
    max_dist = 0
    while len(queue) > 0:
        curr = queue.pop(0)
        max_dist = max(max_dist, curr[2])
        visited.add((curr[0], curr[1]))
        if curr[0] > 0 and grid[curr[0]-1][curr[1]] in '|7F' and (curr[0]-1, curr[1]) not in visited:
            queue.append((curr[0]-1, curr[1], curr[2]+1))
        if curr[0] < len(grid)-1 and grid[curr[0]+1][curr[1]] in '|JL' and (curr[0]+1, curr[1]) not in visited:
            queue.append((curr[0]+1, curr[1], curr[2]+1))
        if curr[1] > 0 and grid[curr[0]][curr[1]-1] in '-LF' and (curr[0], curr[1]-1) not in visited:
            queue.append((curr[0], curr[1]-1, curr[2]+1))
        if curr[1] < len(grid[0])-1 and grid[curr[0]][curr[1]+1] in '-7J' and (curr[0], curr[1]+1) not in visited:
            queue.append((curr[0], curr[1]+1, curr[2]+1))

        
    print(max_dist)


if __name__ == "__main__":
    main(argv[1])

        