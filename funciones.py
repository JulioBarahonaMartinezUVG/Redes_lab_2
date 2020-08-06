import math
import random
import bitarray

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


def cantidadBitsParidad(bits):
    m = len(bits)
    for i in range(len(bits)): 
        if(2**i >= m + i + 1): 
            return i
  
def bitsParidad(bits, cantidad_bits_paridad): 
    j = 0
    k = 1
    m = len(bits) 
    res = '' 

    for i in range(1, m + cantidad_bits_paridad+1): 
        if(i == 2**j): 
            res = res + '0'
            j += 1
        else: 
            res = res + bits[-1 * k] 
            k += 1
    
    return res[::-1] 
  
  
def resultadoBitsParidad(bits, cantidad_bits_paridad): 
    n = len(bits) 
    for i in range(cantidad_bits_paridad): 
        val = 0
        for j in range(1, n + 1): 
            if(j & (2**i) == (2**i)): 
                val = val ^ int(bits[-1 * j]) 
        
        bits = bits[:n-(2**i)] + str(val) + bits[n-(2**i)+1:] 
    return bits 


def reemplazarArrayBits(data, correcto, r): 
    j = 0
    k = 1
    m = len(data) 
    res = '' 

    for i in range(1, m + r+1): 
        if(i == 2**j): 
            res = res + correcto[i]
            j += 1
        else: 
            res = res + data[-1 * k] 
            k += 1
    
    return res[::-1] 
  
def busquedaError(bits, cantidad_bits_redundancia): # Solo encuentra un error
    n = len(bits) 
    res = 0
  
    for i in range(cantidad_bits_redundancia): 
        val = 0
        for j in range(1, n + 1): 
            if(j & (2**i) == (2**i)): 
                val = val ^ int(bits[-1 * j]) 

        res = res + val*(10**i) 

    return int(str(res), 2) 


# Codigo Hamming

def codigoHamming(mensaje_recibido, mensaje_esperado):
    ba_mr = bitarray.bitarray()
    ba_me = bitarray.bitarray()

    ba_mr.frombytes(mensaje_recibido.encode('utf-8'))
    ba_me.frombytes(mensaje_esperado.encode('utf-8'))

    bits_mr = ""
    bits_me = ""

    for i in ba_mr.tolist():
        if (i):
            bits_mr += '1'
        else:
            bits_mr += '0'

    for i in ba_me.tolist():
        if (i):
            bits_me += '1'
        else:
            bits_me += '0'

    # Calcular bits redundantes
    cantidad_bits_redundantes = cantidadBitsParidad(bits_me)

    # print(cantidad_bits_redundantes)
    
    bits_informacion = bitsParidad(bits_me, cantidad_bits_redundantes)

    bits_con_paridad = resultadoBitsParidad(bits_informacion, cantidad_bits_redundantes)

    bits_con_error = reemplazarArrayBits(bits_mr, bits_con_paridad, cantidad_bits_redundantes)

    error_index = busquedaError(bits_con_error, cantidad_bits_redundantes)

    print(error_index)