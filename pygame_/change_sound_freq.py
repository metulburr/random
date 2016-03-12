import pygame as pg

frequency = 4100
done = False

while not done:
    print(frequency)
    pg.mixer.pre_init(frequency, 16, 2, 4096)
    pg.mixer.init()
    test_sound = pg.mixer.Sound('test.wav')
    test_sound.play()
    while pg.mixer.get_busy():
        pass
    pg.mixer.quit()
    frequency += 10000
