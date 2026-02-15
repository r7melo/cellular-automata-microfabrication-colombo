import pygame
import numpy as np

# --- 1. Configurações ---
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 5
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE

V_ETCH = 1.5  # Velocidade da corrosão
DT = 0.5      # Passo de tempo

# Cores
COLOR_SI = (45, 45, 50)       # Silício sólido
COLOR_ETCH = (0, 120, 255)    # Ácido / Vazio
COLOR_INTERFACE = (255, 255, 255) # Frente de onda (Branco)
COLOR_POINT = (255, 0, 0)     # Ponto inicial (Vermelho)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TCC - Setup de Múltiplos Pontos (Huygens)")
clock = pygame.time.Clock()

# Matriz de distâncias (Começa com infinito)
distancia_ao_acido = np.full((ROWS, COLS), 1000.0)
raio_onda = 0.0
pontos_iniciais = []

# Estados do simulador
EDITANDO = 0
SIMULANDO = 1
estado_atual = EDITANDO

def adicionar_ponto_corrosao(pos):
    mx, my = pos
    c_origem = mx // CELL_SIZE
    r_origem = my // CELL_SIZE
    pontos_iniciais.append((r_origem, c_origem))
    
    # Para cada célula da grade, calculamos se este novo ponto é o mais próximo dela
    for r in range(ROWS):
        for c in range(COLS):
            dist = np.sqrt((r - r_origem)**2 + (c - c_origem)**2)
            if dist < distancia_ao_acido[r, c]:
                distancia_ao_acido[r, c] = dist

# --- Loop Principal ---
running = True
while running:
    screen.fill((30, 30, 30))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and estado_atual == EDITANDO:
            adicionar_ponto_corrosao(event.pos)
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: # ENTER começa a simulação
                estado_atual = SIMULANDO
            if event.key == pygame.K_r:      # R reseta tudo
                distancia_ao_acido.fill(1000.0)
                raio_onda = 0.0
                pontos_iniciais = []
                estado_atual = EDITANDO

    if estado_atual == SIMULANDO:
        raio_onda += V_ETCH * DT

    # --- Renderização ---
    for r in range(ROWS):
        for c in range(COLS):
            d = distancia_ao_acido[r, c]
            rect = (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
            if d < raio_onda:
                pygame.draw.rect(screen, COLOR_ETCH, rect)
            elif d < raio_onda + 1.5 and estado_atual == SIMULANDO:
                pygame.draw.rect(screen, COLOR_INTERFACE, rect)
            else:
                # Se estiver no modo de edição, desenha os pontos iniciais
                if (r, c) in pontos_iniciais:
                    pygame.draw.rect(screen, COLOR_POINT, rect)
                elif d == 1000.0:
                    # Desenha o fundo do silício apenas se necessário (performance)
                    if (r + c) % 2 == 0: # Efeito de grade leve
                        pygame.draw.rect(screen, (40, 40, 45), rect)

    # Instruções na tela
    font = pygame.font.SysFont(None, 24)
    if estado_atual == EDITANDO:
        img = font.render("MODO EDIÇÃO: Clique para adicionar pontos. ENTER para começar.", True, (255, 255, 0))
    else:
        img = font.render("MODO SIMULAÇÃO: Pressione R para resetar.", True, (0, 255, 0))
    screen.blit(img, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()