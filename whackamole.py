import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        initial_mole = True
        running = True
        clicked = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            #Draw Y Axis Lines Beginning
            draw_y = 512 // 32
            y = 0
            for i in range(draw_y):
                y += 32
                pygame.draw.line(screen, 'black', (0, y), (640, y))
            #Draw Y Axis Lines End
            #Draw X Axis Lines Begin
            draw_x = 640//32
            x = 0
            for i in range(draw_x):
                x += 32
                pygame.draw.line(screen, 'black',(x, 0), (x,512))
            #Draw X Axis Lines End

            if initial_mole:
                mole_x = 0
                mole_y = 0
            if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
                if mole_x <= event.pos[0] <= mole_x + 32 and mole_y <= event.pos[1] <= mole_y + 32 :
                    print(f'X: {event.pos[0]}', end = ' ')
                    print(f'Y: {event.pos[1]}')
                    mole_x = random.randrange(0, 640 , 32)

                    mole_y = random.randrange(0, 512,32)

                    initial_mole = False
                    clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                clicked = False
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))  #Mole position

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
