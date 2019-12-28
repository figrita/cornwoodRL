import pygame as pg
from enum import Flag, auto
import spritesheet


class Map(object):
    bs = None
    walltiles = None
    background = None
    mapData = None

    def __init__(self):
        self.bs = spritesheet.spritesheet('DawnLike/Objects/Wall.png')
        TESTMAP = [
            "#####xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "    #                                   ",
            "x   #                                   ",
            "xx  #                                   ",
            "x   #                                   ",
            "    #                                   ",
            "    #                                   ",
            "    xxxxxxxxxxxxxxxxxxxxx               ",
            "         x              x               ",
            "         x              xxx             ",
            "         x                x             ",
            "         x                x             ",
            "         x                xxxxxxxxxxxxxx",
            "         x                     x  x     ",
            "         xxxxxxxxxxxxxxxxxxxxxxxxxx     ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "          x               x             "
            "          x               x             ",
            "          x               x             ",
            "          x               x             ",
            "          x               x             ",
            "          x               x             ",
            "xxxxxxxxxxx               xxxxxxxxxxxxxx",
        ]
        self.walltiles = self.bs.load_walls(0, 10)
        self.background = pg.Surface(pg.Rect(0, 0, 640, 480).size)

        self.mapData = [[{'wall': False if cell == ' ' else True, 'borders': Borders.NONE} for cell in line] for line in
                        TESTMAP]
        # create the background, tile the bgd image

        for y, row in enumerate(self.mapData):
            for x, cell in enumerate(row):
                if cell['wall']:
                    # if self.has_cell( x - 1, y - 1):
                    #    mapData[y - 1][x - 1]['borders'] |= Borders.UL
                    if self.has_cell(x, y - 1):
                        self.mapData[y - 1][x]['borders'] |= Borders.S
                    # if self.has_cell( x + 1, y - 1):
                    #    mapData[y - 1][x + 1]['borders'] |= Borders.UR
                    if self.has_cell(x - 1, y):
                        self.mapData[y][x - 1]['borders'] |= Borders.E
                    if self.has_cell(x + 1, y):
                        self.mapData[y][x + 1]['borders'] |= Borders.W
                    # if self.has_cell( x - 1, y + 1):
                    #    mapData[y + 1][x - 1]['borders'] |= Borders.DL
                    if self.has_cell(x, y + 1):
                        self.mapData[y + 1][x]['borders'] |= Borders.N
                    # if self.has_cell( x + 1, y + 1):
                    #    mapData[y + 1][x + 1]['borders'] |= Borders.DR
        for y, row in enumerate(self.mapData):
            for x, cell in enumerate(row):
                if cell['wall']:
                    if cell['borders'] == Borders.E | Borders.S:
                        self.background.blit(self.walltiles[0][0], (x * 16, y * 16))
                    if (cell['borders'] == Borders.W | Borders.E) or (cell['borders'] == Borders.W) or (
                            cell['borders'] == Borders.E):
                        self.background.blit(self.walltiles[1][0], (x * 16, y * 16))
                    if cell['borders'] == Borders.W | Borders.S:
                        self.background.blit(self.walltiles[2][0], (x * 16, y * 16))
                    if cell['borders'] == Borders.NONE:
                        self.background.blit(self.walltiles[3][0], (x * 16, y * 16))
                    if cell['borders'] == Borders.W | Borders.E | Borders.S:
                        self.background.blit(self.walltiles[4][0], (x * 16, y * 16))
                    if (cell['borders'] == Borders.N | Borders.S) or (cell['borders'] == Borders.S):
                        self.background.blit(self.walltiles[0][1], (x * 16, y * 16))
                    if cell['borders'] == Borders.N:
                        self.background.blit(self.walltiles[1][1], (x * 16, y * 16))
                    if cell['borders'] == Borders.N | Borders.E | Borders.S:
                        self.background.blit(self.walltiles[3][1], (x * 16, y * 16))
                    if cell['borders'] == Borders.N | Borders.W | Borders.E | Borders.S:
                        self.background.blit(self.walltiles[4][1], (x * 16, y * 16))
                    if cell['borders'] == Borders.N | Borders.W | Borders.S:
                        self.background.blit(self.walltiles[5][1], (x * 16, y * 16))
                    if cell['borders'] == Borders.N | Borders.E:
                        self.background.blit(self.walltiles[0][2], (x * 16, y * 16))
                    if cell['borders'] == Borders.N | Borders.W:
                        self.background.blit(self.walltiles[2][2], (x * 16, y * 16))
                    if cell['borders'] == Borders.N | Borders.W | Borders.E:
                        self.background.blit(self.walltiles[4][2], (x * 16, y * 16))

    def has_cell(self, x, y):
        if x < 0 or y < 0:
            return False
        if y >= len(self.mapData) or x >= len(self.mapData[0]):
            return False
        return True


class Borders(Flag):
    NONE = 0
    N = auto()
    S = auto()
    E = auto()
    W = auto()
    UL = auto()
    UR = auto()
    DL = auto()
    DR = auto()
