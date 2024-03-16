import datetime
import random

def prefix(semilla):
    fecha_nacimiento = semilla['Date of Birth'] 
    genero = semilla['Gender']
    
    prefijos_hombres = {18: ["Mr.", ""], 30: ["Mr.", "Sr.", "Rv.", ""], 40: ["Mr.", "Sr.", "Rv.", "Dr.",""]}
    prefijos_mujeres = {18: ["Ms.", ""], 25: ["Ms.", "Mrs.", "Rv.", ""], 40: ["Mrs.", "Rv.", "Dr.", ""]}
    
    # Calculamos la edad a partir de la fecha de nacimiento
    fecha_actual = datetime.datetime.now()
    fecha_nacimiento_conversion = datetime.datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    edad = fecha_actual.year - fecha_nacimiento_conversion.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento_conversion.month, fecha_nacimiento_conversion.day))
    
    # Determinamos el prefijo según el género y la edad
    if genero == 'M':
        prefijos = prefijos_hombres
    elif genero == 'F':
        prefijos = prefijos_mujeres
    else:
        prefijos = {}
    
    prefix_random = ""
    for edad_limite, prefijo_lista in prefijos.items():
        if edad >= edad_limite:
            prefix_random = random.choice(prefijo_lista)
            break  # Terminamos la búsqueda tan pronto como encontramos un prefijo adecuado
    
    print (edad)
    print(semilla['FirstName'], prefix_random)
    
    return prefix_random