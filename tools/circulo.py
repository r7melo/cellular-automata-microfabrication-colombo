def obter_pontos_circulo_cheio(tamanho_grid, raio):
    centro = tamanho_grid // 2
    cx, cy = centro, centro
    
    pontos = set()
    x = raio
    y = 0
    p = 1 - raio

    def preencher_linhas(cx, cy, x, y):
        # Em vez de 8 pontos isolados, traçamos 4 linhas horizontais
        # que conectam as extremidades do círculo
        
        # Linhas nos quadrantes superiores e inferiores (lados maiores)
        for i in range(cx - x, cx + x + 1):
            if 0 <= i < tamanho_grid:
                if 0 <= cy + y < tamanho_grid: pontos.add((i, cy + y))
                if 0 <= cy - y < tamanho_grid: pontos.add((i, cy - y))
        
        # Linhas nos quadrantes laterais (lados menores)
        for i in range(cx - y, cx + y + 1):
            if 0 <= i < tamanho_grid:
                if 0 <= cy + x < tamanho_grid: pontos.add((i, cy + x))
                if 0 <= cy - x < tamanho_grid: pontos.add((i, cy - x))

    # Algoritmo de Midpoint
    preencher_linhas(cx, cy, x, y)
    while x > y:
        y += 1
        if p <= 0:
            p = p + 2 * y + 1
        else:
            x -= 1
            p = p + 2 * y - 2 * x + 1
        preencher_linhas(cx, cy, x, y)
        
    return list(pontos)