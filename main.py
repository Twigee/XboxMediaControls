import pygame
import win32api
from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY
from win32con import VK_MEDIA_NEXT_TRACK, KEYEVENTF_EXTENDEDKEY
from win32con import VK_MEDIA_PREV_TRACK, KEYEVENTF_EXTENDEDKEY
from win32con import VK_VOLUME_DOWN, KEYEVENTF_EXTENDEDKEY
from win32con import VK_VOLUME_UP, KEYEVENTF_EXTENDEDKEY

import keyboard

pygame.init()
pygame.joystick.init()

num_joysticks = pygame.joystick.get_count()

if num_joysticks > 0:
    controller = pygame.joystick.Joystick(0)
    controller.init()
else:
    print("No controller connected")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN: 
            if controller.get_button(7):
                pygame.quit()
            elif controller.get_button(4):
                win32api.keybd_event(VK_VOLUME_DOWN, 0, KEYEVENTF_EXTENDEDKEY, 0)
            elif controller.get_button(5):
                win32api.keybd_event(VK_VOLUME_UP, 0, KEYEVENTF_EXTENDEDKEY, 0)





        if event.type == pygame.JOYHATMOTION:
            hat_value = event.value
            # Down D-pad will pause
            if hat_value == (0,-1):
                win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)
            #Right D-pad will skip to next track
            elif hat_value == (1, 0):
                win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
            # Left D-pad will got the the last track
            elif hat_value == (-1, 0):
                win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)



            

