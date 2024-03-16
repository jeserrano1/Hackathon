import random

def generar_ssn():
    # Generar los tres primeros dígitos
    primeros_tres = str(random.randint(1, 899)).zfill(3)
    while primeros_tres in ['000', '666']:
        primeros_tres = str(random.randint(1, 899)).zfill(3)
        
    # Generar los siguientes dos dígitos
    siguientes_dos = str(random.randint(1, 99)).zfill(2)
    
    # Generar los últimos cuatro dígitos
    ultimos_cuatro = ''.join(str(random.randint(1, 9)) for _ in range(4))
    
    # Concatenar todos los dígitos
    ssn = primeros_tres + siguientes_dos + ultimos_cuatro
    
    # Verificar si el SSN cumple con las condiciones adicionales
    if ssn == '123456789' or ssn == ssn[0] * 9:
        return generar_ssn()  # Si no cumple, generar otro SSN
    else:
        return ssn
    

def ssn_generator(ssn, tipo):
    print("Original: ")
    print(ssn)
    
    if tipo == 'twins':
        # Generar nuevo SSN para gemelos 
        # Solo puede cambiar un caracter de los ultimos 4
        primeros_digitos = ssn[:-4]
        ultimos_digitos = list(ssn[-4:])
        posicion_cambio = random.randint(0, 3) 
        nuevo_digito = str(random.randint(1, 9))
        ultimos_digitos[posicion_cambio] = nuevo_digito
        nuevo_ssn = primeros_digitos + ''.join(ultimos_digitos)
        
    elif tipo == 'random':
        nuevo_ssn = generar_ssn()
        
    else:
        print("Debe tener un tipo")
        
    print(nuevo_ssn)
    
    return nuevo_ssn