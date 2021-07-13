from typing import List, Any, Union

import numpy.random as rand
import pandas as pd
from tkinter import *

font_size = 4

# filename = "puffer1.csv"


class Game_Of_Life(object):

    def __init__(self):
        # self.board_state = pd.read_csv("boards_file/" + filename).values
        self.board_state = self.random_state(50, 50)
        self.window = Tk()
        self.header = Label(self.window, font=("courier new", font_size), fg='white', bg='black')
        self.label = Label(self.window, font=("courier new", font_size), fg='white', bg='black')
        self.label.pack()
        self.population = 0
        self.gen = 0
        for list in self.board_state:
            for num in list:
                if num == 1:
                    self.population += 1
        self.update()
        self.window.mainloop()

    def dead_state(self, width, height):
        return [[0] * width for i in range(height)]

    def random_state(self, width, height):
        state = self.dead_state(width, height)
        for y in range(len(state)):
            for x in range(len(state[0])):
                random_number = rand.random()
                if random_number >= 0.5:
                    state[y][x] = 0
                else:
                    state[y][x] = 1
        return state

    def render(self):
        string = '  '
        string += '- ' * len(self.board_state[0]) + '\n'
        for y in range(0, len(self.board_state)):
            string += '| '
            for x in range(0, len(self.board_state[y])):
                if self.board_state[y][x] == 1:
                    string += '██'
                else:
                    string += '  '
            string += ' |\n'
        string += ' '
        string += '- ' * len(self.board_state[0]) + '\n'
        return string

    def next_board_state(self):
        new_state = self.dead_state(len(self.board_state[0]), len(self.board_state))
        for y in range(0, len(self.board_state)):
            for x in range(0, len(self.board_state[y])):
                neighbors = self.number_of_neighbors(x, y)
                if self.board_state[y][x] == 1:
                    if neighbors <= 1:
                        new_state[y][x] = 0
                        self.population -= 1
                    elif neighbors > 3:
                        new_state[y][x] = 0
                        self.population -= 1
                    else:
                        new_state[y][x] = 1
                else:
                    if neighbors == 3:
                        new_state[y][x] = 1
                        self.population += 1
        return new_state

    def number_of_neighbors(self, x, y):
        width = len(self.board_state[y])
        height = len(self.board_state)
        tool = [-1, 0, 1]
        num = 0
        for opx in range(3):
            for opy in range(3):
                if (0 <= x + tool[opx] < width and 0 <= y + tool[opy] < height):
                    if self.board_state[y + tool[opy]][x + tool[opx]] == 1 and not (opx == 1 and opy == 1):
                        num += 1
        return num

    def update(self):
        self.board_state = self.next_board_state()
        self.gen += 1
        self.label.config(text='Generation: ' + str(self.gen) + "\tPopulation: " + str(self.population))
        self.label.config(text=self.render())
        self.window.after(50, self.update)


game_of_life = Game_Of_Life()
