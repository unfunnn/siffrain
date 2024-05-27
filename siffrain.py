import random
import time

import pygame
from pygame.locals import *
import os
import win32api
import win32con
import win32gui

screen_w, screen_h = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
size = 1
siffraindrop_cap = 300

class Siffraindrop:
    def __init__(self, x, y, speed, sprite):
        self.x = int(x)
        self.y = int(y)
        self.speed = speed
        self.sprite = sprite
        self.explodefrin_progress = -1

    def draw(self):
        screen.blit(self.sprite, (self.x - (siffrin_w / 2), self.y - (siffrin_h / 2)))

    def increase_explodefrin(self):
        self.explodefrin_progress += 1


def always_on_top():
    win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], win32con.HWND_TOPMOST, 0, 0, 0, 0,
                          win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

def make_transparent():
    hwnd = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

fuchsia = (255, 0, 128)

screen = pygame.display.set_mode((screen_w, screen_h), NOFRAME|pygame.DOUBLEBUF)
pygame.display.set_caption("Forever falling")

siffrin_img = pygame.image.load("siffrin.png").convert_alpha()
pygame.display.set_icon(siffrin_img)
siffrin_w = siffrin_img.get_width()
siffrin_h = siffrin_img.get_height()

explode = [
    pygame.image.load("explode/frame_00_delay-0.05s.gif").convert_alpha(),
    pygame.image.load("explode/frame_01_delay-0.05s.gif").convert_alpha(),
    pygame.image.load("explode/frame_02_delay-0.05s.gif").convert_alpha(),
    pygame.image.load("explode/frame_03_delay-0.05s.gif").convert_alpha(),
    pygame.image.load("explode/frame_04_delay-0.05s.gif").convert_alpha(),
    pygame.image.load("explode/frame_05_delay-0.05s.gif").convert_alpha(),
    pygame.image.load("explode/frame_06_delay-0.05s.gif").convert_alpha(),
    pygame.image.load("explode/frame_07_delay-0.05s.gif").convert_alpha(),
    pygame.image.load("explode/frame_08_delay-0.05s.gif").convert_alpha(),
    pygame.image.load("explode/frame_09_delay-0.05s.gif").convert_alpha(),
    pygame.image.load("explode/frame_10_delay-0.05s.gif").convert_alpha(),
    pygame.image.load("explode/frame_11_delay-0.05s.gif").convert_alpha(),
    pygame.image.load("explode/frame_12_delay-0.05s.gif").convert_alpha(),
    pygame.image.load("explode/frame_13_delay-0.05s.gif").convert_alpha(),
    pygame.image.load("explode/frame_14_delay-0.05s.gif").convert_alpha(),
    pygame.image.load("explode/frame_15_delay-0.05s.gif").convert_alpha()
]

siffrin = Siffraindrop(screen_w/2, 20, 0, siffrin_img)
listrin = [siffrin]

screen.fill(fuchsia)
make_transparent()
always_on_top()

running = True
loops = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    listrin_temp = listrin
    for sif in listrin_temp:
        if sif.y >= screen_h-20 and sif.explodefrin_progress == -1:
            sif.explodefrin_progress = 0
        if 0 <= sif.explodefrin_progress <= 15:
            sif.sprite = explode[sif.explodefrin_progress]
            sif.increase_explodefrin()
        elif sif.explodefrin_progress > 15:
            sif.y = 0 - siffrin_h
            sif.speed = random.randint(1,6)
            sif.explodefrin_progress = -1
            sif.sprite = siffrin_img
        else:
            sif.y += sif.speed
        sif.draw()
    listrin = listrin_temp
    pygame.display.flip()
    screen.fill(fuchsia)
    time.sleep(1 / 40)
    if len(listrin) < siffraindrop_cap:
        listrin.append(Siffraindrop(random.randint(-siffrin_h, screen_w), 0, random.randint(1,6), siffrin_img))

