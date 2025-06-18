import time  # Importa o módulo para controlar o tempo de espera
import os    # Importa o módulo para limpar a tela do terminal

# Função para remover duplicatas de uma lista, mantendo a ordem original
def remover_duplicatas(array):
    # Criamos uma lista vazia para armazenar os elementos únicos
    unicos = []
    # Percorremos cada elemento da lista original
    for elemento in array:
        # Se o elemento ainda não está na lista de únicos, adicionamos
        if elemento not in unicos:
            unicos.append(elemento)
    # Retornamos a nova lista sem duplicatas
    return unicos

# Lista de desenhos (frames) para animar a cobrinha Python
frames = [
    r"""
         ____
       / . .\
      \  ---<
       \  /
  ______/ /
 /______/ 
""",
    r"""
          ____
        / . .\
       \  ---<
        \  /
   ______/ /
  /______/ 
""",
    r"""
           ____
         / . .\
        \  ---<
         \  /
    ______/ /
   /______/ 
""",
    r"""
            ____
          / . .\
         \  ---<
          \  /
     ______/ /
    /______/ 
"""
]

# Animação da cobrinha Python
# O laço for percorre cada desenho da lista 'frames' e depois volta animando ao contrário
for frame in frames + frames[::-1]:
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela para dar efeito de movimento
    print(frame)  # Mostra o desenho da cobrinha
    print("Bem-vindo ao removedor de duplicatas em Python!\n")  # Mensagem de boas-vindas
    time.sleep(0.5)  # Espera meio segundo antes de mostrar o próximo frame

# Testes com a função, mostrando resultados em caixas bonitas e com pausas
print("╔════════════════════════════════════════════════════════════════════╗")
print("║ Teste 1: [1, 2, 2, 3, 'b', 'a', 'c', 'd', 'd']                   ║")
print("╠════════════════════════════════════════════════════════════════════╣")
resultado1 = remover_duplicatas([1, 2, 2, 3, "b", "a", "c", "d", "d"])  # Teste com números e letras repetidos
print(f"║ Resultado: {resultado1}{' ' * (56 - len(str(resultado1)))}║")
print("╚════════════════════════════════════════════════════════════════════╝\n")
time.sleep(2)  # Espera 2 segundos antes do próximo teste

print("╔════════════════════════════════════════════════════════════════════╗")
print("║ Teste 2: [1, 1, 1, 1]                                            ║")
print("╠════════════════════════════════════════════════════════════════════╣")
resultado2 = remover_duplicatas([1, 1, 1, 1])  # Teste com todos os elementos iguais
print(f"║ Resultado: {resultado2}{' ' * (56 - len(str(resultado2)))}║")
print("╚════════════════════════════════════════════════════════════════════╝\n")
time.sleep(2)  # Espera 2 segundos antes do próximo teste

print("╔════════════════════════════════════════════════════════════════════╗")
print("║ Teste 3: []                                                      ║")
print("╠════════════════════════════════════════════════════════════════════╣")
resultado3 = remover_duplicatas([])  # Teste com lista vazia
print(f"║ Resultado: {resultado3}{' ' * (56 - len(str(resultado3)))}║")
print("╚════════════════════════════════════════════════════════════════════╝")

# Fim do programa!