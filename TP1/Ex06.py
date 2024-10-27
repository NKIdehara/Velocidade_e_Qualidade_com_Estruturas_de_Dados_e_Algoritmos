def encontra_quadrado(graos):
    quadrado = 1
    num_graos = 1
    for i in range(2, 64):
        num_graos = num_graos * 2
        if num_graos >= graos:
            quadrado = i
            break
    return quadrado

print(encontra_quadrado(16))