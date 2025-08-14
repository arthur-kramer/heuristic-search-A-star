# --------- Libraries  ---------

import heapq # Biblioteca que trata filas de prioridade

# --------- Auxiliary Functions  ---------

# Convert km to minutes
def km_para_minutos(dist: float):
    tempo_hora = dist / 40
    tempo_minutos = tempo_hora * 60
    return tempo_minutos

# Heuristic Function
def heuristica(estacao_atual: str, estacao_destino: str, dist_direta: dict):
    # Extrai apenas o nome da estação (ex: "E2_Vermelha" -> "E2")
    estacao1 = estacao_atual.split('_')[0]
    estacao2 = estacao_destino.split('_')[0]

    # Verifica a existência do caminho no dicionário e retorna a distância direta convertida em minutos
    if (estacao1, estacao2) in dist_direta:
        return km_para_minutos(dist_direta[(estacao1, estacao2)])
    elif (estacao2, estacao1) in dist_direta:
        return km_para_minutos(dist_direta[(estacao2, estacao1)])
    else:
        return float(0)

# --------- Station Graph  ---------
grafo_estacoes = {
    'E1_Vermelha' : [('E2_Vermelha', km_para_minutos(4.3))],
    'E2_Vermelha' : [('E1_Vermelha', km_para_minutos(4.3)), ('E3_Vermelha', km_para_minutos(5.3)), ('E2_Verde', 3)],
    'E2_Verde' : [('E7_Verde', km_para_minutos(14.3)), ('E9_Verde', km_para_minutos(4.3)), ('E2_Vermelha', 3)],
    'E3_Vermelha' : [('E2_Vermelha', km_para_minutos(5.3)), ('E4_Vermelha', km_para_minutos(5.9)), ('E3_Azul', 3)],
    'E3_Azul' : [('E7_Azul', km_para_minutos(8.5)), ('E8_Azul', km_para_minutos(4.1)), ('E3_Vermelha', 3)],
    'E4_Vermelha' : [('E3_Vermelha', km_para_minutos(5.9)), ('E14_Vermelha', km_para_minutos(6.2)), ('E4_Amarela', 3)],
    'E4_Amarela' : [('E5_Amarela', km_para_minutos(2.9)), ('E8_Amarela', km_para_minutos(4)), ('E4_Vermelha', 3)],
    'E5_Amarela' : [('E4_Amarela', km_para_minutos(2.9))],
    'E6_Azul' : [('E7_Azul', km_para_minutos(3.2))],
    'E7_Azul' : [('E6_Azul', km_para_minutos(3.2)), ('E3_Azul', km_para_minutos(8.5)), ('E7_Verde', 3)],
    'E7_Verde' : [('E2_Verde', km_para_minutos(14.3)), ('E7_Azul', 3)],
    'E8_Azul' : [('E3_Azul', km_para_minutos(4.1)), ('E10_Azul', km_para_minutos(6)), ('E8_Amarela', 3)],
    'E8_Amarela' : [('E4_Amarela', km_para_minutos(4)), ('E9_Amarela', km_para_minutos(5)), ('E8_Azul', 3)],
    'E9_Amarela' : [('E8_Amarela', km_para_minutos(5)), ('E11_Amarela', km_para_minutos(3.4)), ('E9_Verde', 3)],
    'E9_Verde' : [('E2_Verde', km_para_minutos(4.3)), ('E10_Verde', km_para_minutos(3)), ('E9_Amarela', 3)],
    'E10_Verde' : [('E9_Verde', km_para_minutos(3)), ('E13_Verde', km_para_minutos(9.1)), ('E10_Azul', 3)],
    'E10_Azul' : [('E8_Azul', km_para_minutos(6)), ('E12_Azul', km_para_minutos(5.6)), ('E10_Verde', 3)],
    'E11_Amarela' : [('E9_Amarela', km_para_minutos(3.4))],
    'E12_Azul' : [('E10_Azul', km_para_minutos(5.6))],
    'E13_Verde' : [('E10_Verde', km_para_minutos(9.1))],
    'E14_Vermelha' : [('E4_Vermelha', km_para_minutos(6.2))]
}

# --------- Euclidean distance between stations  ---------
dist_direta = {
    ('E1', 'E2') : 4.3,
    ('E1', 'E3') : 9,
    ('E1', 'E4') : 14.7,
    ('E1', 'E5') : 17.2,
    ('E1', 'E6') : 13.1,
    ('E1', 'E7') : 11.8,
    ('E1', 'E8') : 11.3,
    ('E1', 'E9') : 8.2,
    ('E1', 'E10') : 10.7,
    ('E1', 'E11') : 8.4,
    ('E1', 'E12') : 14.1,
    ('E1', 'E13') : 18.5,
    ('E1', 'E14') : 17.3,

    ('E2', 'E3') : 5.3,
    ('E2', 'E4') : 10.3,
    ('E2', 'E5') : 13.1,
    ('E2', 'E6') : 12.7,
    ('E2', 'E7') : 10.3,
    ('E2', 'E8') : 6.9,
    ('E2', 'E9') : 4.3,
    ('E2', 'E10') : 7.4,
    ('E2', 'E11') : 5.9,
    ('E2', 'E12') : 11.3,
    ('E2', 'E13') : 14.8,
    ('E2', 'E14') : 12.9,

    ('E3', 'E4') : 5.9,
    ('E3', 'E5') : 8.5,
    ('E3', 'E6') : 10.9,
    ('E3', 'E7') : 7.7,
    ('E3', 'E8') : 4.1,
    ('E3', 'E9') : 6.5,
    ('E3', 'E10') : 8.9,
    ('E3', 'E11') : 9.4,
    ('E3', 'E12') : 14.5,
    ('E3', 'E13') : 13.9,
    ('E3', 'E14') : 10.3,

    ('E4', 'E5') : 2.9,
    ('E4', 'E6') : 15,
    ('E4', 'E7') : 12.7,
    ('E4', 'E8') : 4,
    ('E4', 'E9') : 9.1,
    ('E4', 'E10') : 9.7,
    ('E4', 'E11') : 12.2,
    ('E4', 'E12') : 14.7,
    ('E4', 'E13') : 10.6,
    ('E4', 'E14') : 6,

    ('E5', 'E6') : 16,
    ('E5', 'E7') : 12.3,
    ('E5', 'E8') : 7,
    ('E5', 'E9') : 12,
    ('E5', 'E10') : 15.3,
    ('E5', 'E11') : 14.8,
    ('E5', 'E12') : 17.3,
    ('E5', 'E13') : 12.7,
    ('E5', 'E14') : 6.9,

    ('E6', 'E7') : 3.2,
    ('E6', 'E8') : 15.1,
    ('E6', 'E9') : 16.5,
    ('E6', 'E10') : 18.5,
    ('E6', 'E11') : 19,
    ('E6', 'E12') : 24.3,
    ('E6', 'E13') : 25.2,
    ('E6', 'E14') : 21.1,

    ('E7', 'E8') : 12,
    ('E7', 'E9') : 13.3,
    ('E7', 'E10') : 16.4,
    ('E7', 'E11') : 16,
    ('E7', 'E12') : 22.2,
    ('E7', 'E13') : 22.6,
    ('E7', 'E14') : 17.1,

    ('E8', 'E9') : 5,
    ('E8', 'E10') : 5.6,
    ('E8', 'E11') : 7.9,
    ('E8', 'E12') : 12.4,
    ('E8', 'E13') : 9.8,
    ('E8', 'E14') : 6.4,

    ('E9', 'E10') : 3,
    ('E9', 'E11') : 3.4,
    ('E9', 'E12') : 8.1,
    ('E9', 'E13') : 10.9,
    ('E9', 'E14') : 9.6,

    ('E10', 'E11') : 3.4,
    ('E10', 'E12') : 5.6,
    ('E10', 'E13') : 7.7,
    ('E10', 'E14') : 8.4,

    ('E11', 'E12') : 5.9,
    ('E11', 'E13') : 11.2,
    ('E11', 'E14') : 12.7,

    ('E12', 'E13') : 8.6,
    ('E12', 'E14') : 12.3,

    ('E13', 'E14') : 6.1,
}

# --------- A* Algorithm  ---------
def a_estrela(estacao_inicial: str, estacao_destino: str, grafo: dict, dist_direta: dict):
    fronteira = [] # Inicializa a fronteira
    heapq.heappush(fronteira, (heuristica(estacao_inicial, estacao_destino, dist_direta), estacao_inicial)) # Adiciona a estação inicial no início da fronteira

    tempo_percorrido = {estacao_inicial : 0} # Dicionário para armazenar o tempo já percorrido até as estações
    estacao_pai = {estacao_inicial : None} # Dicionário para armazenar as estações visitadas e seus "pais"

    while fronteira != []: # Algoritmo irá rodar enquanto houver estações na fronteira
        print(f'Fronteira atual: {sorted(fronteira)}\n')
        _, estacao_atual = heapq.heappop(fronteira) # Retira e retorna a primeira estação da fronteira, ou seja, a com menor custo
        print(f' -> Estação em análise: {estacao_atual}\n')

        if estacao_atual == estacao_destino: # Verifica se já chegamos ao destino final
            # Reconstrução do caminho
            print('Chegamos ao destino final!\n')
            rota_final = [] # Lista para armazenar a rota completa
            while estacao_atual != None:
                rota_final.append(estacao_atual)
                estacao_atual = estacao_pai[estacao_atual]
            rota_final.reverse()
            return rota_final, tempo_percorrido[estacao_destino]

        filhos = []
        for filho, _ in grafo.get(estacao_atual, []):
            filhos.append(filho)
        print(f"Filhos de {estacao_atual}: {', '.join(filhos)}\n")

        for filho, tempo_a_percorrer in grafo.get(estacao_atual, []):
            custo_ate_estacao = tempo_percorrido[estacao_atual] + tempo_a_percorrer # g(n)

            if filho not in tempo_percorrido or custo_ate_estacao < tempo_percorrido[filho]:
                print(f'Tempo entre {estacao_atual} e {filho}: {tempo_a_percorrer:.2f} minutos')
                print(f'g(n) para {filho}: {custo_ate_estacao:.2f} minutos')
                tempo_percorrido[filho] = custo_ate_estacao
                custo_ate_destino = heuristica(filho, estacao_destino, dist_direta) # h(n)
                print(f'h(n) para {filho}: {custo_ate_destino:.2f} minutos')
                custo_total = custo_ate_estacao + custo_ate_destino # f(n) = g(n) + h(n)
                print(f'f(n) para {filho}: {custo_total:.2f} minutos\n')
                heapq.heappush(fronteira, (custo_total, filho)) # Adiciona à fronteira
                estacao_pai[filho] = estacao_atual

            else:
                print(f'{filho} já visitado com custo menor ou igual ({tempo_percorrido[filho]:.2f} <= {custo_ate_estacao:.2f}).\n')

        print("-------------------------------------------------------------------------------------------------\n")

    return print('Não foi possível achar um caminho até o destino final!')

# --------- A* Execution  ---------
estacao_inicial = 'E1_Vermelha' # Initial_state
estacao_destino = 'E6_Azul' # Goal_state

rota_final, tempo_total = a_estrela(estacao_inicial, estacao_destino, grafo_estacoes, dist_direta)

print('- Rota Mais Rápida:')
print(" -> ".join(rota_final))

print(f"\n- Tempo estimado total: {tempo_total:.2f} minutos")
