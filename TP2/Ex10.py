def conta_impares(fila):
    impar = 0
    for i in fila:
        if i % 2 != 0:
            impar += 1
    return impar

fila = [177, 5412, 2475, 4746, 5928, 36, 5692, 8628, 6905, 6419, 8910, 3032, 5558, 908, 925, 8367, 1478, 9308, 2878, 3711, 862, 9195, 3910, 4290, 7726, 928, 5762, 4646, 7239, 9856, 7488, 9037, 4695, 5367, 676, 4679, 491, 3435, 3157, 739, 9282, 6067, 1766, 6309, 826, 1309, 8503, 9088, 754, 5944, 62, 1395, 2757, 3857, 6066, 2460, 7325, 1488, 8924, 8843, 1394, 3138, 6827, 677, 1972, 1918, 2164, 8845, 7594, 6124, 1304, 4954, 2278, 8159, 351, 2408, 7846, 2013, 9294, 7440, 5770, 115, 2254, 2415, 3822, 3885, 277, 6028, 8560, 2602, 4770, 9879, 8615, 2221, 9900, 6475, 5016, 9230, 1043, 3999]
print(f"O número total de livros cuja identificação é um número ímpar: {conta_impares(fila)}")