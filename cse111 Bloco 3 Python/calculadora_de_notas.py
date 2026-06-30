"""
Autor: João Augusto Ferreira

Projeto: Calculadora de notas escolares

"""

def obter_notas():
    nome = input("Digite o seu nome :  ")
    print("Agora digite sua nota de 0 a 10")

# Coleta uma nota por matéria e armazena em variáveis separadas

    nota_ciencias = float(input("Digite a sua nota de Ciências: "))
    nota_matematica = float(input("Digite a sua nota de Matemática: "))
    nota_portugues = float(input("Digite a sua nota de Língua Portuguesa: "))

# Dicionário que organiza os dados do aluno 

    aluno = {
        "nome": nome,
        "notas": {
            "Ciências": nota_ciencias,
            "Matemática": nota_matematica,
            "Língua Portuguesa": nota_portugues
        }
    }

    return aluno

# Calcula e retorna a média das notas

def calcular_media(notas):
    valores = list(notas.values())
    return sum(valores) / len(valores)


def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


def mostrar_resultado(aluno, media, situacao):
    print("\n----- RESULTADO -----")
    print(f"Aluno: {aluno['nome']}")
    for materia, nota in aluno["notas"].items():
        print(f"  {materia}: {nota:.2f}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

# Percorre pelo dicionário de notas para exibir cada matéria
# E criando o arquivo resultado.txt para salvar as informações

def salvar_resultado(aluno, media, situacao):
    with open("resultado.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Aluno: {aluno['nome']}\n")
        for materia, nota in aluno["notas"].items():
            arquivo.write(f"  {materia}: {nota:.2f}\n")
        arquivo.write(f"Média: {media:.2f}\n")
        arquivo.write(f"Situação: {situacao}\n")
        

def main():
    aluno = obter_notas()                         # 1 Coleta os dados do aluno
    media = calcular_media(aluno["notas"])        # 2 Calcula a média
    situacao = verificar_aprovacao(media)         # 3 Verifica aprovação
    mostrar_resultado(aluno, media, situacao)     # 4 Exibe o resultado
    salvar_resultado(aluno, media, situacao)      # 5 Salva o resultado em resultado.txt


if __name__ == "__main__":
    main() 