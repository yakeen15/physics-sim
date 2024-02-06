import pygame
import os
from datetime import datetime
def writelog(data,filepath=None):
    try:
        if filepath is None:
            current_time = datetime.now().strftime("%H-%M-%S-%d-%m-%y")
            filename = f"{current_time}.txt"
            directory = "log"
            if not os.path.exists(directory):
                os.makedirs(directory)
            filepath = os.path.join(directory, filename)
        with open(filepath, 'a') as f:
            for dat in data:
                f.write(str(dat)+'\n')
    except Exception as e:
        print("Exception occured: "+str(e))
def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)
