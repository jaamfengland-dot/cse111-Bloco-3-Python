# No código abaixo você verá # TODO.
# Essa é uma das anotações especiais que o programador pode usar em comentários para indicar que uma tarefa
#  está pendente. “TODO” traduzido para o português significa “a fazer”.

# Constantes dos tubos e da água
PVC_SCHED80_DIAMETRO_INTERNO = 0.28687   # (metros)  11.294 polegadas
PVC_SCHED80_FATOR_ATRITO = 0.013         # (sem unidade)
VELOCIDADE_ABASTECIMENTO = 1.65          # (metros / segundo)
HDPE_SDR11_DIAMETRO_INTERNO = 0.048692   # (metros)  1.917 polegadas
HDPE_SDR11_FATOR_ATRITO = 0.018          # (sem unidade)
VELOCIDADE_RESIDENCIAL = 1.75            # (metros / segundo)
DENSIDADE_AGUA = 998.2                   # densidade da água (998.2 quilogramas / metro^3)

def main():
    altura_torre = float(input("Altura da torre de água (metros): "))
    altura_tanque = float(input("Altura das paredes do tanque de água (metros): "))
    comprimento1 = float(input("Comprimento do tubo de abastecimento, do tanque até o terreno (metros): "))
    quantidade_angulos = int(input("Número de ângulos de 90° no tubo de abastecimento: "))
    comprimento2 = float(input("Comprimento do tubo do abastecimento até a casa (metros): "))
    
    altura_agua = calc_altura_coluna_agua(altura_torre, altura_tanque)
    pressao = calc_pressao_pela_altura(altura_agua)
    diametro = PVC_SCHED80_DIAMETRO_INTERNO
    atrito = PVC_SCHED80_FATOR_ATRITO
    velocidade = VELOCIDADE_ABASTECIMENTO
    reynolds = calc_num_reynolds(diametro, velocidade)
    perda = calc_perda_pressao_tubo(diametro, comprimento1, atrito, velocidade)
    pressao += perda                                                        
    perda = calc_perda_pressao_conexoes(velocidade, quantidade_angulos)
    pressao += perda
    perda = calc_perda_pressao_reducao_tubo(diametro, velocidade, reynolds, HDPE_SDR11_DIAMETRO_INTERNO)
    pressao += perda
    diametro = HDPE_SDR11_DIAMETRO_INTERNO
    atrito = HDPE_SDR11_FATOR_ATRITO
    velocidade = VELOCIDADE_RESIDENCIAL
    perda = calc_perda_pressao_tubo(diametro, comprimento2, atrito, velocidade)
    pressao += perda
    print(f"Pressão na casa: {pressao:.1f} quilopascal")

def calc_altura_coluna_agua(altura_torre, altura_tanque):
    return altura_torre + 3 * altura_tanque / 4


def calc_pressao_pela_altura(altura):
    return (DENSIDADE_AGUA * 9.80665 * altura) / 1000


def calc_perda_pressao_tubo(diametro_tubo, comprimento_tubo, fator_atrito, velocidade_fluido):
    numerador = -fator_atrito * comprimento_tubo * DENSIDADE_AGUA * (velocidade_fluido ** 2)
    # CORRIGIDO: Mudado de 200 para 2000 para bater com a fórmula do enunciado
    denominador = 2000 * diametro_tubo
    return numerador / denominador


def calc_perda_pressao_conexoes(velocidade_fluido, quantidade_conexoes):
    # Mantendo a fórmula correta dividida por 2000
    return (-0.04 * DENSIDADE_AGUA * (velocidade_fluido ** 2) * quantidade_conexoes) / 2000


def calc_num_reynolds(diametro_hidraulico, velocidade_fluido):
    reynolds = (DENSIDADE_AGUA * diametro_hidraulico * velocidade_fluido) / 0.0010016
    return reynolds


def calc_perda_pressao_reducao_tubo(diametro_maior, velocidade_fluido, numero_reynolds, diametro_menor):
    # CORRIGIDO: Mudado de + 1 para - 1 no final da fórmula para calcular o k correto
    k = (0.1 + 50 / numero_reynolds) * (((diametro_maior / diametro_menor) ** 4) - 1)
    return -k * DENSIDADE_AGUA * (velocidade_fluido ** 2) / 2000

if __name__ == "__main__":
    main()
