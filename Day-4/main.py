with open('data.txt', 'r') as bingo_file:
    draws = list(map(lambda x: int(x), bingo_file.readline().strip().split(',')))
    grids_string = [element.strip('\n') for element in bingo_file.readlines() if element != '\n']


def create_grids(grids_data):
    grids_list = []
    grid = []
    for element in grids_data:
        if len(grid) == 5:
            grids_list.append(grid)
            grid = []
        row = [int(data) for data in element.split(' ') if data != '']
        grid.append(row)
    return grids_list


def get_win_result(grid):
    res = 0
    for i in range(5):
        for j in range(5):
            if grid[i][j] not in done_draws:
                res += grid[i][j]
    return res


def check_grid(grid):
    for row in grid:
        bingo = True
        checked_element = 0
        for element in row:
            if element not in done_draws:
                bingo = False
                pass
            else:
                checked_element += 1

            if not bingo:
                break
            elif checked_element == 5:
                return get_win_result(grid)

    for i in range(5):
        bingo = True
        checked_element = 0
        for j in range(5):
            element = grid[j][i]
            if element not in done_draws:
                bingo = False
                pass
            else:
                checked_element += 1

            if not bingo:
                break
            elif checked_element == 5:
                return get_win_result(grid)
    return -1


grids = create_grids(grids_string)
done_draws = []

for draw in draws:
    done_draws.append(draw)
    for grid_to_check in grids:
        result = check_grid(grid_to_check)
        if result > 0:
            print(done_draws[-1] * result)
