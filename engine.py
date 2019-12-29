import os

# import basic pygame modules
import pygame as pg

import spritesheet
import player
import Map


# see if we can load more than standard BMP
if not pg.image.get_extended():
    raise SystemExit("Sorry, extended image module required")


# game constants
SCREENRECT = pg.Rect(0, 0, 640, 480)
SCORE = 0

main_dir = os.path.split(os.path.abspath(__file__))[0]


# Each type of game object gets an init and an update function.
# The update function is called once per frame, and it is when each object should
# change it's current position and state.
#
# The Player object actually gets a "move" function instead of update,
# since it is passed extra information about the keyboard.

def main(winstyle=0):
    # Initialize pygame
    if pg.get_sdl_version()[0] == 2:
        pg.mixer.pre_init(44100, 32, 2, 1024)
    pg.init()
    if pg.mixer and not pg.mixer.get_init():
        print("Warning, no sound")
        pg.mixer = None
    pg.mixer = None

    fullscreen = False
    # Set the display mode
    winstyle = 0  # |FULLSCREEN
    bestdepth = pg.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pg.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    # Load images, assign to sprite classes
    # (do this before the classes are used, after screen setup)
    ss = spritesheet.spritesheet('DawnLike/Characters/Cat0.png')
    img = ss.image_at((0, 0, 16, 16))
    all = pg.sprite.RenderUpdates()
    myplayer = player.player(img, all)

    # decorate the game window
    icon = pg.transform.scale(img, (32, 32))
    pg.display.set_icon(icon)
    pg.display.set_caption("Cornwood Deluxe X Plus Ace")
    pg.mouse.set_visible(0)

    # GENERATE MAP HERE
    myMap = Map.Map()
    screen.blit(myMap.background, (0, 0))
    pg.display.flip()

    # Create Some Starting Values
    clock = pg.time.Clock()

    gameon = True

    # Run our main loop whilst the player is alive.
    while gameon:

        # get input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    if not fullscreen:
                        print("Changing to FULLSCREEN")
                        screen_backup = screen.copy()
                        screen = pg.display.set_mode(
                            SCREENRECT.size, winstyle | pg.FULLSCREEN, bestdepth
                        )
                        screen.blit(screen_backup, (0, 0))
                    else:
                        print("Changing to windowed mode")
                        screen_backup = screen.copy()
                        screen = pg.display.set_mode(
                            SCREENRECT.size, winstyle, bestdepth
                        )
                        screen.blit(screen_backup, (0, 0))
                    pg.display.flip()
                    fullscreen = not fullscreen

        # clear/erase the last drawn sprites
        all.clear(screen, myMap.background)

        # update all the sprites
        all.update()

        # draw the scene
        dirty = all.draw(screen)
        pg.display.update(dirty)

        # cap the framerate at 40fps. Also called 40HZ or 40 times per second.
        clock.tick(60)

    if pg.mixer:
        pg.mixer.music.fadeout(1000)
    pg.time.wait(1000)
    pg.quit()


# call the "main" function if running this script
if __name__ == "__main__":
    main()