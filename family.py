from faker import Faker
def parent_child(semilla):
    
    semilla['ID']
    semilla['Prefix']
    firstName = semilla['FirstName']
    semilla['MiddleName']
    lastName = semilla['LastName']
    semilla['Suffix']
    semilla['Alias-1']
    semilla['Alias-2']
    semilla['Alias-3']
    semilla['Date of Birth']
    semilla['SSN']
    semilla['Address-1 Line 1']
    semilla['Address-1 Line 2']
    semilla['Address-1 City']
    a1_state =semilla['Address-1 State']
    semilla['Address-1 Zip']
    semilla['Address-1 Zip4']
    semilla['Address-1 Line 1']
    semilla['Address-1 Line 2']
    semilla['Address-1 City']
    semilla['Address-1 State']
    semilla['Address-1 Zip']
    semilla['Address-1 Zip4']
    
    semilla['Address-2 Line 1']
    semilla['Address-2 Line 2']
    semilla['Address-2 City']
    semilla['Address-2 State']
    semilla['Address-2 Zip']
    semilla['Address-2 Zip4']
    semilla['Address-2 Line 1']
    semilla['Address-2 Line 2']
    semilla['Address-2 City']
    semilla['Address-2 State']
    semilla['Address-2 Zip']
    semilla['Address-2 Zip4']
    
    semilla['Phone-1 Area Code']
    semilla['Phone-1 Base Number']
    
    semilla['Phone-2 Area Code']
    semilla['Phone-2 Base Number']
    semilla['Gender']
    
    generate_alias(firstName, lastName)
    
    return semilla

def generateName(state, gender):
    
    males, females = openPopularNames(state)
    
    name = ''
    
    if(gender):
        pass
    else: 
        pass
    
    return name

def openPopularNames(state):
    females = []
    males = []
    
    import csv

    with open(f'/files/PopularNamesByState/{state}.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            nombre_male = row[1]
            frecuencia_male = int(row[2])
            nombre_female = row[3]
            frecuencia_female = int(row[4])
            
            males.append((nombre_male, frecuencia_male))
            
            females.append((nombre_female, frecuencia_female))
    
    return males, females

def generateGender():
    import random
    probabilidad = random.random()
    if probabilidad < 0.5:
        return 'M'
    else:
        return 'F'
