alien_0 = {'cor':'verde', 'pontuacao': 5, 'posicao_x': 0, 'posicao_y': 25, 'poder':'fogo'}

print(alien_0)

del alien_0['poder']

print(alien_0)


for atr, val in alien_0.items():
    print(atr)
    print(val)
    print('')