import math, random, sys, keyboard, os
import pygame

class Tile:
    def __init__(self, pX, pY, sX, sY):
        self.PositionX = pX
        self.PositionY = pY
        self.SourceX = sX
        self.SourceY = sY
