Web VPython 3.2

# Configuração do ambiente de simulação
scene = canvas(width=1920, height=1080, background=color.black)
scene.autoscale = False

# Parâmetros do sistema
mass1 = 1.0  # Massa do primeiro objeto
mass2 = 2.0  # Massa do segundo objeto
k = 2.0  # Constante da mola
initial_displacement = 0.5  # Deslocamento inicial da mola
amplitude = 3.0  # Amplitude do movimento horizontal
wall_distance = 13.0  # Distância entre as paredes
num_turns = 10  # Número de voltas da mola

# Criação dos objetos
object1 = sphere(pos=vector(-amplitude/2, 0, 0), radius=0.5, color=color.red)
object2 = sphere(pos=vector(amplitude/2, 0, 0), radius=1.0, color=color.blue)
wall1 = box(pos=vector(-wall_distance/2, 0, 0), size=vector(0.1, 4, 4), color=color.green)
wall2 = box(pos=vector(wall_distance/2, 0, 0), size=vector(0.1, 4, 4), color=color.green)

# Criação das molas
spring1 = helix(pos=wall1.pos, axis=object1.pos - wall1.pos, radius=0.20, thickness=0.05, coils=num_turns)
spring2 = helix(pos=object1.pos, axis=object2.pos - object1.pos, radius=0.20, thickness=0.05, coils=num_turns)
spring3 = helix(pos=object2.pos, axis=wall2.pos - object2.pos, radius=0.20, thickness=0.05, coils=num_turns)

# Cálculo das constantes do sistema
k_eff1 = k / ((1 / mass1) + (1 / 1e9))
k_eff2 = k / ((1 / mass2) + (1 / mass1))
k_eff3 = k / ((1 / 1e9) + (1 / mass2))
angular_freq1 = sqrt(k_eff1 / mass1)
angular_freq2 = sqrt(k_eff2 / (mass1 + mass2))
angular_freq3 = sqrt(k_eff3 / mass2)

# Tempo e ângulo inicial
t = 0
theta = initial_displacement / amplitude

# Loop de simulação
while t < 1000000:
    rate(500)

    # Atualização da posição dos objetos
    object1.pos.x = -amplitude/2 + amplitude * cos(angular_freq1 * t)
    object2.pos.x = amplitude/2 + amplitude * cos(angular_freq1 * t + theta)
    spring1.axis = object1.pos - wall1.pos
    spring2.pos = object1.pos
    spring2.axis = object2.pos - object1.pos
    spring3.pos = object2.pos
    spring3.axis = wall2.pos - object2.pos

    t += 0.01
