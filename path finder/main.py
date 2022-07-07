import curses
from curses import wrapper
import time
import queue

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],  # []: for lists, this is an 2D array.
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):  # enumerate will give the index of the row and the row itself.
        # i is no of the row and row is the list of the maze we are currently on.
        for j, value in enumerate(row):  # here j, i the index and value is the values in the quotation marks respectively.
            if (i, j) in path:
                stdscr.addstr(i, j * 2, "#", RED)
            else:
                stdscr.addstr(i, j * 2, value, BLUE)


def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None


def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))  # we are putting/inserting the position and path into the queue

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)  # calling the function to print all the maze
        time.sleep(0.2)
        stdscr.refresh()
        #stdscr.getch()  # it is like input funct, bcz of this program will wait until the user hit any key.

        if maze[row][col] == end:
            return path

        neighbors = find_neighbors(maze, row, col)

        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor

            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)


def find_neighbors(maze, row, col):
    neighbors = []
    if row > 0:  # UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # DOWN
        neighbors.append((row + 1, col))
    if col > 0:  # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):
        neighbors.append((row, col + 1))

    return neighbors


def main(stdscr):
    # using stdscr bcz after which we will not need to use print("") like function #stdscr is standard output screen

    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)  # 1 represents the id of this pair
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # similarly 2 represents the id of this pair
    #stdscr.clear()  # it will clear the screen
    # print_maze(maze, stdscr)
    # stdscr.addstr(0, 0, "Hello world", black_and_blue)           #0(row),0(column), means total right corner of the
    # screen

    find_path(maze, stdscr)
    stdscr.getch()
wrapper(main)
