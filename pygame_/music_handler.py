#play music/sound track one after another

import pygame as pg
import os

class Music:
    def __init__(self, volume):
        self.path = '.'
        self.allowed_exts = ['.wav']
        self.setup(volume)
        
    def setup(self, volume):
        self.track_end = pg.USEREVENT+1
        self.tracks = []
        self.track = 0
        for track in os.listdir(self.path):
            for ext in self.allowed_exts:
                if track.endswith(ext):
                    self.tracks.append(os.path.join(self.path, track))
        #random.shuffle(self.tracks)
        pg.mixer.music.set_volume(volume)
        pg.mixer.music.set_endevent(self.track_end)
        try:
            pg.mixer.music.load(self.tracks[0])
        except IndexError:
            raise Exception('Files {} not found in directory {}'.format(self.allowed_exts, os.path.abspath(self.path)))

pg.init()
screen = pg.display.set_mode((600,400))
done = False
sound = Music(.5)
pg.mixer.music.play()
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == sound.track_end:
            sound.track = (sound.track+1) % len(sound.tracks)
            pg.mixer.music.load(sound.tracks[sound.track]) 
            pg.display.set_caption(sound.tracks[sound.track])
            pg.mixer.music.play()
    pg.display.update()
pg.quit()
