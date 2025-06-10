import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    kt_img = pg.image.load("fig/3.png")
    kt_img = pg.transform.flip(kt_img,True,False)
    kt_rct = kt_img.get_rect()
    kt_rct.center = 300, 200
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x=tmr%3200
        key_lst = pg.key.get_pressed()
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2,[-x+1600,0])
        screen.blit(bg_img,[-x+3200,0])
        screen.blit(kt_img, kt_rct)
        if key_lst[pg.K_UP]:
            j=-1
        elif key_lst[pg.K_DOWN]:
            j=1
        elif key_lst[pg.K_LEFT]:
            i=-2
        elif key_lst[pg.K_RIGHT]:
            i=2
        else:
            i=-1
            j=0
        kt_rct.move_ip((i,j))
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()