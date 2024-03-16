from faker import Faker
import random
from prefixs import prefix
from ssn import ssn_generator


fake = Faker()

def twin(semilla):
    # Obtener datos de la semilla
    fecha_nacimiento = semilla['Date of Birth']
    apellido = semilla['LastName']
    ssn = str(semilla['SSN'])
    
    nueva_semilla = semilla.copy()
    
    tipo = "twins"    
    nuevo_ssn = ssn_generator(ssn, tipo)
    
    # Generar SSN distintas no repetidas para los gemelos
    nueva_semilla['SSN'] = nuevo_ssn    
    # Modificar algunos datos para el gemelo
    nueva_semilla['FirstName'] = fake.first_name()  # Generar un nombre aleatorio
    nueva_semilla['MiddleName'] = fake.last_name()  # Generar un segundo nombre aleatorio
    nueva_semilla['LastName'] = apellido  # Mantener el mismo apellido
    nueva_semilla['Date of Birth'] = fecha_nacimiento  # Mantener la misma fecha de nacimiento
        
    # Generar datos de dirección ficticios
    nueva_semilla['Address-1 Line 1'] = fake.street_address()
    nueva_semilla['Address-1 Line 2'] = fake.secondary_address()
    nueva_semilla['Address-1 City'] = fake.city()
    nueva_semilla['Address-1 State'] = fake.state_abbr()
    nueva_semilla['Address-1 Zip'] = fake.zipcode()
        
    # Generar género aleatorio
    nueva_semilla['Gender'] = random.choice(['M', 'F'])
    nueva_semilla['Prefix'] = prefix(semilla)
    
    # Tipo de caso
    nueva_semilla['CASE TYPE'] = tipo
    
    print(nueva_semilla)
    return nueva_semilla
