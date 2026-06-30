# Direitos Autorais 2020, Brigham Young University-Idaho. Todos os direitos reservados.

def main():
    print("Este programa calcula consumo de combustível")
    print("do seu veículo em quilômetros por litro.")

    odom_anterior = float(input("Digite a leitura anterior do odômetro em quilômetros: "))
    odom_atual = float(input("Digite a leitura atual do odômetro em quilômetros: "))
    combustivel = float(input("Digite a quantidade de combustível consumido: "))

    consumo = quilometros_por_litro(combustivel, odom_anterior, odom_atual)

    print(f"{consumo} quilômetros por litro")


def quilometros_por_litro(odometro_inicial, odometro_final, quantidade_litros):
    """Calcula e retorna a quantidade de quilômetros
    que um veículo percorreu por litro de combustível.

    Parâmetros
        odometro_inicial: valor inicial do odômetro em quilômetros.
        odometro_final: valor final do odômetro em quilômetros.
        quantidade_litros: quantidade de combustível em litros.
    Retorna: consumo de combustível em quilômetros por litro.
    """
    distancia = odometro_final - odometro_inicial
    kml = distancia / quantidade_litros
    return kml


# Se este arquivo for executado assim:
# > python exemplo.py
# então chame a função main. No entanto, se este arquivo
# for apenas importado, pule a chamada para main.
if __name__ == "__main__":
    main()
