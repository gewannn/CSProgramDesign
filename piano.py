import os
try:
    import pygame
except:
    os.system("pip install pygame -i https://pypi.tuna.tsinghua.edu.cn/simple")
    import pygame
import pygame.midi
from time import sleep

GRAND_PIANO = 0
instrument = GRAND_PIANO

pygame.init()
pygame.midi.init()
port = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(port, 0)
midi_out.set_instrument(instrument)

for tone in range(40, 90):
    midi_out.note_on(tone, 127)
    sleep(0.25)
    midi_out.note_off(tone, 127)
    sleep(0.25)

del midi_out
pygame.midi.quit()
