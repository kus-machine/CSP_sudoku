import numpy as np
import doctest
from func import *

#условие для которого будет решение
board=np.array([
    [5, 3, 0,    0, 7, 0,    0, 0, 0],
    [6, 0, 0,    1, 9, 5,    0, 0, 0],
    [0, 9, 8,    0, 0, 0,    0, 6, 0],

    [8, 0, 0,    0, 6, 0,    0, 0, 3],
    [4, 0, 0,    8, 0, 3,    0, 0, 1],
    [7, 0, 0,    0, 2, 0,    0, 0, 6],

    [0, 6, 0,    0, 0, 0,    2, 8, 0],
    [0, 0, 0,    4, 1, 9,    0, 0, 5],
    [0, 0, 0,    0, 8, 0,    0, 7, 9]])
#условие, для которого решений несколько и нет одного однозначного, который получают алгоритмом вычеркивания
board1=np.array([
    [5, 0, 0,    0, 7, 0,    0, 0, 0],
    [6, 0, 0,    1, 9, 5,    0, 0, 0],
    [0, 9, 8,    0, 0, 0,    0, 6, 0],

    [8, 0, 0,    0, 6, 0,    0, 0, 3],
    [4, 0, 0,    8, 0, 3,    0, 0, 1],
    [7, 0, 0,    0, 2, 0,    0, 0, 6],

    [0, 6, 0,    0, 0, 0,    2, 0, 0],
    [0, 0, 0,    4, 1, 0,    0, 0, 5],
    [0, 0, 0,    0, 8, 0,    0, 7, 0]])
#условие, с которым алгоритм справится за один заход
board2=np.array([
    [4,2,6,8,1,9,5,7,3],
    [9,8,3,5,7,4,2,1,6],
    [5,1,7,2,3,6,4,8,9],

    [1,5,8,3,4,2,9,6,7],
    [7,4,2,9,6,8,1,3,5],
    [3,6,9,7,5,1,8,4,2],

    [2,7,4,6,8,5,3,9,1],
    [8,3,5,1,9,7,6,2,4],
    [6,9,1,4,2,3,7,5,0]])

board3=np.array([
    [1, 2, 3,    4, 5, 6,    7, 8, 0],
    [0, 0, 0,    0, 0, 0,    0, 0, 0],
    [0, 0, 0,    0, 0, 0,    0, 0, 0],

    [0, 0, 0,    0, 0, 0,    0, 0, 0],
    [0, 0, 0,    0, 0, 0,    0, 0, 0],
    [0, 0, 0,    0, 0, 0,    0, 0, 0],

    [0, 0, 0,    0, 0, 0,    0, 0, 0],
    [0, 0, 0,    0, 0, 0,    0, 0, 0],
    [0, 0, 0,    0, 0, 0,    0, 0, 0]])
board4=np.array([
    [1, 2, 3,    4, 5, 6,    7, 8, 0],
    [0, 0, 0,    0, 0, 0,    0, 0, 0],
    [0, 0, 0,    0, 0, 0,    0, 0, 0],

    [0, 0, 0,    0, 0, 0,    0, 0, 0],
    [0, 0, 0,    0, 0, 0,    0, 0, 0],
    [0, 0, 0,    0, 0, 0,    0, 0, 0],

    [0, 0, 0,    0, 0, 0,    0, 0, 0],
    [0, 0, 0,    0, 0, 0,    0, 0, 0],
    [0, 0, 0,    0, 0, 0,    0, 0, 9]])


solve(board)
#solve(board1)
#solve(board2)
#solve(board3)