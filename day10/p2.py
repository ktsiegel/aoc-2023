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

    expanded_grid = []
    for lindex in range(len(grid)):
        line = grid[lindex]
        l = []
        for c in range(len(line)):
            l.append(line[c])
            if c < len(line)-1:
                l.append('.')
        expanded_grid.append(l)
        if lindex < len(grid)-1:
            expanded_grid.append(['.' for _ in range(len(l))])

    # expand the grid by adding a space between each cell, then fill in the relevant pipe loop segments
    queue = [(start[0], start[1], 0)]
    visited = set()
    while len(queue) > 0:
        curr = queue.pop(0)
        visited.add((curr[0], curr[1]))
        if curr[0] > 0 and grid[curr[0]-1][curr[1]] in '|7F' and grid[curr[0]][curr[1]] in '|JLS' and (curr[0]-1, curr[1]) not in visited:
            # go up
            queue.append((curr[0]-1, curr[1], curr[2]+1))
            expanded_grid[curr[0]*2-1][curr[1]*2] = '|'
        if curr[0] < len(grid)-1 and grid[curr[0]+1][curr[1]] in '|JL' and grid[curr[0]][curr[1]] in '|F7S' and (curr[0]+1, curr[1]) not in visited:
            # go down
            queue.append((curr[0]+1, curr[1], curr[2]+1))
            expanded_grid[curr[0]*2+1][curr[1]*2] = '|'
        if curr[1] > 0 and grid[curr[0]][curr[1]-1] in '-FL' and grid[curr[0]][curr[1]] in '-J7S' and (curr[0], curr[1]-1) not in visited:
            # go left
            queue.append((curr[0], curr[1]-1, curr[2]+1))
            expanded_grid[curr[0]*2][curr[1]*2-1] = '-'
        if curr[1] < len(grid[0])-1 and grid[curr[0]][curr[1]+1] in '-7J' and grid[curr[0]][curr[1]] in '-FLS' and (curr[0], curr[1]+1) not in visited:
            # go right
            queue.append((curr[0], curr[1]+1, curr[2]+1))
            expanded_grid[curr[0]*2][curr[1]*2+1] = '-'

    grid = expanded_grid

    start = (0,0)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = (i,j)
                break

    # bfs to find the new loop
    visited = set()
    queue = [(start[0], start[1], 0)]
    while len(queue) > 0:
        curr = queue.pop(0)
        visited.add((curr[0], curr[1]))
        if curr[0] > 0 and grid[curr[0]-1][curr[1]] in '|7F' and grid[curr[0]][curr[1]] in '|JLS'  and (curr[0]-1, curr[1]) not in visited:
            # go up
            queue.append((curr[0]-1, curr[1], curr[2]+1))
        if curr[0] < len(grid)-1 and grid[curr[0]+1][curr[1]] in '|JL' and grid[curr[0]][curr[1]] in '|F7S' and (curr[0]+1, curr[1]) not in visited:
            # go down
            queue.append((curr[0]+1, curr[1], curr[2]+1))
        if curr[1] > 0 and grid[curr[0]][curr[1]-1] in '-LF' and grid[curr[0]][curr[1]] in '-J7S' and (curr[0], curr[1]-1) not in visited:
            # go left
            queue.append((curr[0], curr[1]-1, curr[2]+1))
        if curr[1] < len(grid[0])-1 and grid[curr[0]][curr[1]+1] in '-7J' and grid[curr[0]][curr[1]] in '-FLS' and (curr[0], curr[1]+1) not in visited:
            # go right
            queue.append((curr[0], curr[1]+1, curr[2]+1))

        
    outside_visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[0])-1:
                if grid[i][j] == '.':
                    outside_visited.add((i,j))

    potential_inside_candidates = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            potential_inside_candidates.add((i,j))

    # bfs to find the area outside the loop
    v = set()
    queue = list(outside_visited)
    while len(queue) > 0:
        curr = queue.pop(0)
        if curr in v:
            continue
        v.add(curr)
        if curr not in visited:
            if curr[0] > 0 and (curr[0]-1, curr[1]) not in v:
                queue.append((curr[0]-1, curr[1]))
            if curr[0] < len(grid)-1 and (curr[0]+1, curr[1]) not in v:
                queue.append((curr[0]+1, curr[1]))
            if curr[1] > 0 and (curr[0], curr[1]-1) not in v:
                queue.append((curr[0], curr[1]-1))
            if curr[1] < len(grid[0])-1 and (curr[0], curr[1]+1) not in v:
                queue.append((curr[0], curr[1]+1))
        else:
            if curr[0] > 0 and (curr[0]-1, curr[1]) not in v and (curr[0]-1, curr[1]) in visited:
                queue.append((curr[0]-1, curr[1]))
            if curr[0] < len(grid)-1 and (curr[0]+1, curr[1]) not in v and (curr[0]+1, curr[1]) in visited:
                queue.append((curr[0]+1, curr[1]))
            if curr[1] > 0 and (curr[0], curr[1]-1) not in v and (curr[0], curr[1]-1) in visited:
                queue.append((curr[0], curr[1]-1))
            if curr[1] < len(grid[0])-1 and (curr[0], curr[1]+1) not in v and (curr[0], curr[1]+1) in visited:
                queue.append((curr[0], curr[1]+1)) 

    c = 0
    # grid miinus whatever is outside or on the loop is what is inside the loop
    for x in potential_inside_candidates - v:
        # make sure to remove the expanded grid elements that didn't exist before we expanded the grid
        if x[0] % 2 == 0 and x[1] % 2 == 0:
            c += 1
        
    print(c)


if __name__ == "__main__":
    main(argv[1])

        