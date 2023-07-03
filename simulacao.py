Web VPython 3.2

parede1 = box(pos=vector(-35, 0, 0), size=vector(1, 10, 10), color=color.yellow)
bloco1 = sphere(pos=vector(-25, 0, 0), size=vector(4, 4, 4), color=color.red)
mola1 = helix(pos=parede1.pos + vector(0.5, 0, 0), axis=bloco1.pos - parede1.pos - vector(0.5, 0, 0), radius=0.5, thickness=0.5, coils=5, color=color.blue)

parede2 = box(pos=vector(35, 0, 0), size=vector(1, 10, 10), color=color.yellow)
bloco2 = sphere(pos=vector(25, 0, 0), size=vector(4, 4, 4), color=color.green)
mola2 = helix(pos=parede2.pos - vector(0.5, 0, 0), axis=bloco2.pos - parede2.pos + vector(0.5, 0, 0), radius=0.5, thickness=0.5, coils=5, color=color.orange)

# Define o espaço entre as molas
espaco_entre_molas = 8.0

# Atualiza a posição das molas com base no espaço entre elas
mola1.pos = parede1.pos + vector(espaco_entre_molas / 2, 0, 0)
mola2.pos = parede2.pos - vector(espaco_entre_molas / 2, 0, 0)

# Condições iniciais
bloco1.vel = vector(0, 0, 0)
bloco2.vel = vector(0, 0, 0)
k = 400
m = 5
t = 0
dt = 0.001

# Equações
while True:
    rate(500)
    
    # Primeiro bloco
    f1 = vector(-bloco1.pos.x * k, 0, 0)
    acel1 = f1 / m
    bloco1.pos = bloco1.pos + (bloco1.vel * dt)
    bloco1.vel = bloco1.vel + (acel1 * dt)
    
    # Verificar limite do primeiro bloco
    if bloco1.pos.x <= -8:
        bloco1.pos.x = -8
    
    mola1.axis = bloco1.pos - mola1.pos
    
    # Segundo bloco
    f2 = vector(-bloco2.pos.x * k, 0, 0)
    acel2 = f2 / m
    bloco2.pos = bloco2.pos + (bloco2.vel * dt)
    bloco2.vel = bloco2.vel + (acel2 * dt)
    
    # Verificar limite do segundo bloco
    if bloco2.pos.x >= 8:
        bloco2.pos.x = 8
    
    mola2.axis = bloco2.pos - mola2.pos
    
    t = t + dt
