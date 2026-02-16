import pygame
import math

# --- CONFIGURAÇÕES ---
LARGURA, ALTURA = 600, 600
GRID = 60
TAM = LARGURA // GRID


# -------------------- UTIL --------------------

def calcular_cor(d):
    if d > 1000:
        return (0, 0, 0)
    v = int((math.sin(d * 0.6) + 1) * 127)
    return (0, v, v)


# -------------------- ESTADO --------------------

def resetar_tudo():
    dx = [[1000.0 for _ in range(GRID)] for _ in range(GRID)]
    dy = [[1000.0 for _ in range(GRID)] for _ in range(GRID)]
    obs = [[False for _ in range(GRID)] for _ in range(GRID)]
    return dx, dy, obs


# -------------------- EVENTOS --------------------

def tratar_eventos(dx, dy, obstaculos, simulando):
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False, simulando, dx, dy, obstaculos

        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_r:
                dx, dy, obstaculos = resetar_tudo()
                simulando = False
            if ev.key == pygame.K_RETURN:
                simulando = True

    return True, simulando, dx, dy, obstaculos


def tratar_mouse(dx, dy, obstaculos):
    m_esq, _, m_dir = pygame.mouse.get_pressed()
    mx, my = pygame.mouse.get_pos()
    c, r = mx // TAM, my // TAM

    if 0 <= r < GRID and 0 <= c < GRID:
        if m_esq:
            dx[r][c], dy[r][c] = 0.0, 0.0
            obstaculos[r][c] = False
        elif m_dir:
            obstaculos[r][c] = True
            dx[r][c], dy[r][c] = 1000.0, 1000.0


# -------------------- SIMULAÇÃO --------------------

def atualizar_simulacao(dx, dy, obstaculos):
    prox_dx = [l[:] for l in dx]
    prox_dy = [l[:] for l in dy]

    for r in range(GRID):
        for c in range(GRID):
            if obstaculos[r][c]:
                continue

            for dr, dc, ax, ay in [
                (-1,0,0,1),
                (1,0,0,1),
                (0,-1,1,0),
                (0,1,1,0)
            ]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < GRID and 0 <= nc < GRID:
                    if not obstaculos[nr][nc]:
                        nx = dx[nr][nc] + ax
                        ny = dy[nr][nc] + ay

                        if (nx**2 + ny**2) < (prox_dx[r][c]**2 + prox_dy[r][c]**2):
                            prox_dx[r][c] = nx
                            prox_dy[r][c] = ny

    return prox_dx, prox_dy


# -------------------- RENDER --------------------

def desenhar(tela, dx, dy, obstaculos):
    tela.fill((0, 0, 0))

    for r in range(GRID):
        for c in range(GRID):
            rect = (c*TAM, r*TAM, TAM, TAM)

            if obstaculos[r][c]:
                pygame.draw.rect(tela, (100, 100, 100), rect)
            else:
                d = math.sqrt(dx[r][c]**2 + dy[r][c]**2)

                if d == 0:
                    pygame.draw.rect(tela, (255, 255, 255), rect)
                elif d < 500:
                    pygame.draw.rect(tela, calcular_cor(d), rect)

    pygame.display.flip()


# -------------------- LOOP PRINCIPAL --------------------

def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption(
        "LAB: [Esq] Semente | [Dir] Obstáculo | [Enter] Iniciar | [R] Reset"
    )
    clock = pygame.time.Clock()

    dx, dy, obstaculos = resetar_tudo()
    simulando = False
    rodando = True

    while rodando:

        rodando, simulando, dx, dy, obstaculos = tratar_eventos(
            dx, dy, obstaculos, simulando
        )

        tratar_mouse(dx, dy, obstaculos)

        if simulando:
            dx, dy = atualizar_simulacao(dx, dy, obstaculos)

        desenhar(tela, dx, dy, obstaculos)

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
