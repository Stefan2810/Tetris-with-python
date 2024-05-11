import pygame
from tetris import Tetris
from shape import colors


pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BACKGROUND = (73, 69, 106)
#(105, 104, 128)
#CONTUR = ()

size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tetris")

done = False
clock = pygame.time.Clock()
fps = 20
game = Tetris(20,10)
counter = 0

pressing_down = False

while not done:
    
    if game.shape is None:
        game.new_shape()
    counter += 1
    if counter > 100000:
        counter = 0
    
    if counter % (fps// game.level// 2) == 0 or pressing_down:
        if game.state == "start":
            game.go_down()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                game.go_side(-1)
            if event.key == pygame.K_RIGHT:
                game.go_side(1)
            if event.key == pygame.K_SPACE:
                game.go_space()
            if event.key == pygame.K_ESCAPE:
                counter=0
                game.clear()
                game = Tetris(20, 10)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            pressing_down = False

    screen.fill(BACKGROUND)

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, WHITE, [game.x + game.zoom * j, game.y + game.zoom *i, game.zoom, game.zoom], 1)
            if game.grid[i][j] > 0 :
                pygame.draw.rect(screen, colors[game.grid[i][j]], [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    if game.shape is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.shape.image():
                    pygame.draw.rect(screen, colors[game.shape.color], 
                                    [game.x + game.zoom * (j + game.shape.x) + 1,
                                     game.y + game.zoom * (i + game.shape.y) + 1,
                                     game.zoom - 2, game.zoom - 2])
    
    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 45, True, False)
    text = font.render("Current score: " + str(game.score), True, BLACK)
    text_game_over = font1.render("Game Over", True, BLACK )
    text_quit = font1.render("Press Esc to quit", True, BLACK )
    text_restart = font1.render("Press Enter to Restart", True, BLACK)

    screen.blit(text, [0, 0])
    if game.state == "game_over":
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_quit, [20, 250])
        screen.blit(text_restart, [20, 300])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()