import math
import random

def ruido(ba, numero_bits, por_cada):
    new_ba = ba.copy()

    proporcion = math.floor(new_ba.length()/por_cada)
    if proporcion == 0:
        proporcion = 1
    
    cantidad_ruido = proporcion * numero_bits

    i = 0
    bits_changed = []
    while i < cantidad_ruido:
        bit_cambio = random.randint(0, new_ba.length() - 1)
        if bit_cambio not in bits_changed:
            bits_changed.append(bit_cambio)
            new_ba[bit_cambio] = not new_ba[bit_cambio]
            i += 1
    

    return new_ba