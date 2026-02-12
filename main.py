import pygame
import numpy as np

# Configurações Iniciais
WIDTH, HEIGHT = 800, 800
SIZE = 10
COLS, ROWS = WIDTH // SIZE, HEIGHT // SIZE

# Cores
COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_ALIVE = (0, 255, 150)

def update(screen, grid):
    new_grid = grid.copy()

    for row in range(ROWS):
        for col in range(COLS): 
            # Soma dos vizinhos (Vizinhança de Moore)
            neighbors = np.sum(grid[row-1:row+2, col-1:col+2]) - grid[row, col]

            # Regras de Conway
            if grid[row, col] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[row, col] = 0
            else:
                if neighbors == 3:
                    new_grid[row, col] = 1

            # Desenho
            color = COLOR_ALIVE if grid[row, col] == 1 else COLOR_BG
            pygame.draw.rect(screen, color, (col * SIZE, row * SIZE, SIZE - 1, SIZE - 1))

    return new_grid

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("CA Intelligence")
    
    grid = np.zeros((ROWS, COLS))
    running = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            # Controladores
            if event.type == pygame.KEYDOWN:
                # SPACE: pausa/despausa
                if event.key == pygame.K_SPACE:
                    running = not running
                # TECLA C: limpa a matriz
                if event.key == pygame.K_c: 
                    grid = np.zeros((ROWS, COLS))

            # Interatividade: desenhar com o mouse
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                grid[pos[1] // SIZE, pos[0] // SIZE] = 1

        screen.fill(COLOR_GRID)
        
        if running:
            grid = update(screen, grid)
        else:
            # Desenha o estado atual parado para permitir edição
            for row in range(ROWS):
                for col in range(COLS):
                    color = COLOR_ALIVE if grid[row, col] == 1 else COLOR_BG
                    pygame.draw.rect(screen, color, (col * SIZE, row * SIZE, SIZE - 1, SIZE - 1))

        pygame.display.flip()

if __name__ == "__main__":
    main()