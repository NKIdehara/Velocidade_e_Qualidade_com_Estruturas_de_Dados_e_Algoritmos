def inverter_string(palavra):
    if len(palavra) == 0:
        return ""
    return palavra[len(palavra)-1] + inverter_string(palavra[:len(palavra)-1])

print(inverter_string("recursao"))