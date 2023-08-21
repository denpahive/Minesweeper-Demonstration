import random

def create_minefield(x):
    icons = ['#', '-']
    my_list = []
    
    for i in range(x):
        row_list = []
        
        for j in range(x):
            row_list.append(random.choice(icons))
        
        my_list.append(row_list)
    
    return my_list


def count_mines_adjacent_to_dashes(grid):
    rows = len(grid)
    cols = len(grid[0])
    adjacent_offsets = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    mine_count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '-':  # If the current cell is a dash (-)
                for offset in adjacent_offsets:
                    x = i + offset[0]
                    y = j + offset[1]
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '#':
                        mine_count += 1

                grid[i][j] = str(mine_count)  # Update the dash with the mine count
                mine_count = 0  # Reset the mine count for the next dash

    return grid


x = 5  # Replace with the desired size of the minefield
minefield = create_minefield(x)
print("Minefield:")
for row in minefield:
    print(' '.join(row))

counted_minefield = count_mines_adjacent_to_dashes(minefield)
print("\nCounted Minefield:")
for row in counted_minefield:
    print(' '.join(row))