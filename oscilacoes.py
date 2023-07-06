import numpy as np
import sys

def coupled_oscillations(dimensions, mass, x1, x2, amplitude, spring_constant):
    # Cálculo da frequência angular
    omega = 2*np.sqrt (spring_constant/mass)* np.sin(dimensions*np.pi/(2*(dimensions+1))) #maior autofrequencia

    # Matriz de oscilação acoplada
    A = np.zeros((dimensions, dimensions))  # Cria uma matriz vazia de dimensões x dimensões

    # Preenche todos os elementos da matriz com os valores corretos
    #(Esse for if elif, basicamente evita que a matriz receba valores incorretos e que também os valores não sejam preenchidos em suas determinadas posições)
    for i in range(dimensions):
        for j in range(dimensions):
            if i == j:
                A[i, j] = (2 *spring_constant) - (mass * omega**2)
            elif abs(i - j) == 1:
                A[i, j] = - spring_constant

    # Vetor de deslocamento inicial
    x = np.zeros(dimensions)  # Cria um vetor de deslocamento inicial com todas as posições igual a zero
    x[:2] = x1, x2  # Define os valores x1 e x2 nas duas primeiras posições do vetor x

    # Cálculo dos deslocamentos ao longo do tempo
    t = np.linspace(0, 10, 100)  # Intervalo de tempo de 0 a 10 com 100 pontos
    displacement = amplitude * np.sin(omega * t)  # Vetor de deslocamento ao longo do tempo
    x_t = np.zeros((len(t), dimensions))  # Matriz para armazenar os deslocamentos em cada instante de tempo
    x_t[0] = x  # Define o vetor de deslocamento inicial na primeira linha da matriz x_t

    for i in range(1, len(t)):
        x = np.dot(A, x) + displacement[i]  # Cálculo do próximo deslocamento com base na matriz A e no deslocamento atual
        x_t[i] = x  # Armazena o deslocamento na matriz x_t

    return omega, x_t, A, amplitude

# Obtendo os dados do usuário
try:
    dimensions = int(input("Digite a quantidade de dimensões: "))
except ValueError:
    print("Erro: A quantidade de dimensões deve ser um número inteiro.")
    sys.exit()

try:
    mass = float(input("Digite a massa: "))
except ValueError:
    print("Erro: A massa deve ser um número real.")
    sys.exit()

try:
    x1 = float(input("Digite o deslocamento x1: "))
except ValueError:
    print("Erro: O deslocamento x1 deve ser um número real.")
    sys.exit()

try:
    x2 = float(input("Digite o deslocamento x2: "))
except ValueError:
    print("Erro: O deslocamento x2 deve ser um número real.")
    sys.exit()

use_amplitude = input("Deseja inserir a amplitude? (s/n): ")
if use_amplitude.lower() == "s":
    try:
        amplitude = float(input("Digite a amplitude: "))
    except ValueError:
        print("Erro: A amplitude deve ser um número real.")
        sys.exit()
else:
    # Calculando a amplitude com base nos dados fornecidos
    amplitude = np.sqrt(x1**2 + x2**2) / np.sqrt(2)  # Amplitude é calculada como a raiz quadrada da média dos quadrados dos deslocamentos x1 e x2
    print("Amplitude com base nos dados fornecidos:", amplitude)

# Obtendo a constante elástica
try:
    spring_constant = float(input("Digite a constante elástica: "))
except ValueError:
    print("Erro: A constante elástica deve ser um número real.")
    sys.exit()



# Calculando as oscilações acopladas
omega, x_t, A, amplitude = coupled_oscillations(dimensions, mass, x1, x2, amplitude, spring_constant)

# Imprimindo o valor de omega
print("Valor de omega:", omega)

# Mostrando a matriz
print("Matriz:")
print(np.array2string(A, separator=", "))
