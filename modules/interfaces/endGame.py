import sys
import pygame

def endGame(screen, sounds, showScore, score, number_images, bird, pipe_sprites, background_image, other_images, base_pos, cfg):
    sounds['die'].play()
    gameover_pos = [(cfg.SCREENWIDTH - other_images['message'].get_width())/2, cfg.SCREENHEIGHT // 2.3]
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    return
        boundary_values = [0, base_pos[-1]]
        bird.update(boundary_values, float(clock.tick(cfg.FPS))/1000)
        screen.blit(background_image, (0, 0))
        pipe_sprites.draw(screen)
        screen.blit(other_images['base'], base_pos)
        showScore(screen, score, number_images)
        bird.draw(screen)
        screen.blit(other_images['gameover'], gameover_pos)
        pygame.display.update()
        clock.tick(cfg.FPS)