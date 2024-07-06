import pygame

from gameMenu import Menu
from image_store import bgBg, bgGrd, bgSky, symImg, snail1, snail2, fly1, fly2, playJump, playStand, playWalk1, playWalk2, gameFont1, gameFont2, gameFont3, gameSound1, gameSound2, gameSound3, gameSound4
from calculation import addition, substration, multiplication, division



SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

bgSky = '../Programming/pythonProject/graphics/Sky.png'
bgGrd = '../Programming/pythonProject/graphics/ground.png'

gameFont1 = '../Programming/pythonProject/font/Pixeltype.ttf'
gameFont2 = '../Programming/pythonProject/font/kenvector_future.ttf'
gameFont3 = '../Programming/pythonProject/font/XpressiveBlack Regular.ttf'



class Game:
    def __init__(self):
        items = (
            'Addition',
            'Subtraction',
            'Multiplication',
            'Division'
        )
        self.menu = Menu(items, ttf_font=gameFont1, fontsize=50)
        self.problem = {
            'num1':0,
            'num2':0,
            'result':0
        }
        self.operation = ''
        self.font = pygame.font.Font(None, 45)
        self.count = 0
        self.score = 0