import numpy.random as rand

def dead_state(width, height):
    return [[0] * width for i in range(height)]


def random_state(width, height):
    state = dead_state(width, height)
    for y in range(len(state)):
        for x in range(len(state[0])):
            random_number = rand.random()
            if random_number >= 0.5:
                state[y][x] = 0
            else:
                state[y][x] = 1
    return state


def render(board_state):
    print(' ', end="")
    print(' - ' * len(board_state[0]))
    for y in range(0, len(board_state)):
        print('| ', end="")
        for x in range(0, len(board_state[y])):
            if board_state[y][x] == 1:
                print(' # ', end="")
            else :
                print('   ', end="")
        print(' |')
    print(' ', end="")
    print(' - ' * len(board_state[0]))


def next_board_state(board_state):
    new_state = dead_state(len(board_state), len(board_state[0]))
    for y in range(0, len(board_state)):
        for x in range(0, len(board_state[y])):
            neighbors = number_of_neighbors(x, y, board_state)
            if board_state[y][x] == 1:
                if neighbors <= 1:
                    new_state[y][x] = 0
                elif neighbors > 3:
                    new_state[y][x] = 0
                else:
                    new_state[y][x] = 1
            else:
                if neighbors == 3:
                    new_state[y][x] = 1
    return new_state


def number_of_neighbors(x, y, state):
    width = len(state[y])
    height = len(state)
    tool = [-1, 0, 1]
    num = 0
    for opx in range(3):
        for opy in range(3):
            if (0 <= x + tool[opx] < width and 0 <= y + tool[opy] < height):
                if state[y + tool[opy]][x + tool[opx]] == 1 and not (opx == 1 and opy == 1):
                    num += 1
    return num

board_state = random_state(20, 20)
render(board_state)
for i in range(0, 100):
    board_state = next_board_state(board_state)
    render(board_state)

