import pygame

def draw_grid():
    pass
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            #Draw Y Axis Lines Beginning
            draw_y = 512 // 32
            x = 0
            for i in range(draw_y):
                x += 32
                pygame.draw.line(screen, 'black', (0, x), (640, x))
            #Draw Y Axis Lines End
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
