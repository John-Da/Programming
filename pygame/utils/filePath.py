import pygame

BASE_PATH = 'pygame/img/'

def load_img(path):
    img = pygame.image.load(BASE_PATH + path).convert()
    img.set_colorkey((0,0,0))
    return img