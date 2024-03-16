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
    dob = semilla['Date of Birth']
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
    gender = semilla['Gender']
    
    #print(generateG())
    print(semilla)
    print(generatePopularName(a1_state, gender))
    #print(generateDOB())
    print(generateChildDOB(dob))
    print(generateSiblingsdDOB(dob))
    #generate_alias(firstName, lastName)
    
    return semilla

def generateRandomName(gender):
    #import csv
    import pickle
    import random
    
    #f_names = list()
    #m_names = list()
    
    #with open(f'./files/names.csv', newline='') as csvfile:
    #    reader = csv.reader(csvfile)
    #
    #    for row in reader:
    #        if(row[1]=='F'):
    #            name = row[3]
    #            if name not in f_names:
    #                f_names.append(name)
    #        else: 
    #            name = row[3]
    #            if name not in m_names:
    #                m_names.append(name)
                    
    #all_names=AllNames()
    #all_names.females = f_names
    #all_names.males = m_names

    #with open("all_names.pkl", "wb") as archivo:
    #    pickle.dump(all_names, archivo)
        
    with open("all_names.pkl", "rb") as archivo:
        all_names = pickle.load(archivo)    
        
    #print('females: ', len( all_names.females))
    #print('males: ', len(all_names.males))
    
    #print('random female name: ',f_name)
    #print('random male name: ',m_name)
    if(gender=='F'):
        index = random.randint(0, 20278)
        f_name = all_names.females[index]
        return f_name
    if(gender=='M'):
        index = random.randint(0, 13334)
        m_name = all_names.males[index]
        return m_name
    return None

class AllNames():
    females = list()
    males = list()
    
class StateAllNames():
    females =  list()
    females_p = list()
    males = list()
    males_p = list()
            
def generatePopularName(statee, gender):
    females = list()
    females_p = list()
    males = list()
    males_p = list()
    
    import csv
    
    states = [
        "Alabama",
        "Alaska",
        "Arizona",
        "Arkansas",
        "California",
        "Colorado",
        "Connecticut",
        "Delaware",
        "Florida",
        "Georgia",
        "Hawaii",
        "Idaho",
        "Illinois",
        "Indiana",
        "Iowa",
        "Kansas",
        "Kentucky",
        "Louisiana",
        "Maine",
        "Maryland",
        "Massachusetts",
        "Michigan",
        "Minnesota",
        "Mississippi",
        "Missouri",
        "Montana",
        "Nebraska",
        "Nevada",
        "New Hampshire",
        "New Jersey",
        "New Mexico",
        "New York",
        "North Carolina",
        "North Dakota",
        "Ohio",
        "Oklahoma",
        "Oregon",
        "Pennsylvania",
        "Rhode Island",
        "South Carolina",
        "South Dakota",
        "Tennessee",
        "Texas",
        "Utah",
        "Vermont",
        "Virginia",
        "Washington",
        "West Virginia",
        "Wisconsin",
        "Wyoming",
        "District of Columbia"
    ]
    # for state in states:
    #     print(state)
    #     with open(f'./files/PopularNamesByState/2003/{state}.csv', newline='') as csvfile:
    #         reader = csv.reader(csvfile)
            
    #         male_total_count = 0
    #         female_total_count = 0
            
    #         for row in reader:
                
    #             male_total_count += int(row[2])
    #             female_total_count += int(row[4])
                
    #             nombre_male = row[1]
    #             probability_male = int(row[2])
    #             nombre_female = row[3]
    #             probability_female = int(row[4])                
    #             males.append(nombre_male)
    #             males_p.append(probability_male)
    #             females.append(nombre_female)
    #             females_p.append(probability_female)
            
    #         male_probability_weight = (100 / male_total_count) / 100
    #         female_probability_weight = (100 / female_total_count) / 100
            
    #         for p in males_p:
    #             p = p * male_probability_weight
            
    #         for p in females_p:
    #             p = p * female_probability_weight
        
    #     state_all_names = StateAllNames()
    #     state_all_names.females = females
    #     state_all_names.females_p = females_p
    #     state_all_names.males = males
    #     state_all_names.males_p = males_p
        
    #     with open(f'./files/PopularNamesByState/2003/{state}_all_names.pkl', "wb") as archivo:
    #         pickle.dump(state_all_names, archivo)
    #     females.clear()
    #     females_p.clear()
    #     males.clear()
    #     males_p.clear()
        
    statee=abreviationToState(statee)
    import pickle
    with open(f'./files/PopularNamesByState/2003/{statee}_all_names.pkl', "rb") as archivo:
        state_all_names = pickle.load(archivo) 
    
    import random
    
    #print(archivo)
    #print(state_all_names.males)
    
    if (gender=='F'):
        name = random.choices(state_all_names.females, weights=state_all_names.females_p, k=1)
        return name
    if (gender=='M'):
        name = random.choices(state_all_names.males, weights=state_all_names.males_p, k=1)
        return name
    return None

def generateGender():
    import random
    probabilidad = random.random()
    if probabilidad < 0.5:
        return 'M'
    else:
        return 'F'

def abreviationToState(abreviation):
    
    state_abreviations = {
        "AL": "Alabama",
        "AK": "Alaska",
        "AZ": "Arizona",
        "AR": "Arkansas",
        "CA": "California",
        "CO": "Colorado",
        "CT": "Connecticut",
        "DE": "Delaware",
        "FL": "Florida",
        "GA": "Georgia",
        "HI": "Hawaii",
        "ID": "Idaho",
        "IL": "Illinois",
        "IN": "Indiana",
        "IA": "Iowa",
        "KS": "Kansas",
        "KY": "Kentucky",
        "LA": "Louisiana",
        "ME": "Maine",
        "MD": "Maryland",
        "MA": "Massachusetts",
        "MI": "Michigan",
        "MN": "Minnesota",
        "MS": "Mississippi",
        "MO": "Missouri",
        "MT": "Montana",
        "NE": "Nebraska",
        "NV": "Nevada",
        "NH": "New Hampshire",
        "NJ": "New Jersey",
        "NM": "New Mexico",
        "NY": "New York",
        "NC": "North Carolina",
        "ND": "North Dakota",
        "OH": "Ohio",
        "OK": "Oklahoma",
        "OR": "Oregon",
        "PA": "Pennsylvania",
        "RI": "Rhode Island",
        "SC": "South Carolina",
        "SD": "South Dakota",
        "TN": "Tennessee",
        "TX": "Texas",
        "UT": "Utah",
        "VT": "Vermont",
        "VA": "Virginia",
        "WA": "Washington",
        "WV": "West Virginia",
        "WI": "Wisconsin",
        "WY": "Wyoming"
    }
    
    state = state_abreviations[abreviation]
    return state

def generateDOB():
    import faker
    faker = Faker()
    fecha_nacimiento = faker.date_of_birth(minimum_age=18, maximum_age=80)
    fecha_nacimiento_formateada = fecha_nacimiento.strftime('%Y-%m-%d')
    return fecha_nacimiento_formateada

def generateChildDOB(DOB):
    if (get_edad(DOB) >= 39):
        print('Es mayor que 39')
        import faker
        faker = Faker()
        fecha_nacimiento = faker.date_of_birth(minimum_age=18, maximum_age=get_edad(DOB)-20)
        fecha_nacimiento_formateada = fecha_nacimiento.strftime('%Y-%m-%d')
        return fecha_nacimiento_formateada
    else:
        return None

def generateSiblingsdDOB(DOB):
    import random
    import faker
    if (get_edad(DOB) >= 19): # Generacion de hermano menor
        probabilidad = random.random()
        if probabilidad < 0.5:
            faker = Faker()
            fecha_nacimiento = faker.date_of_birth(minimum_age=18, maximum_age=get_edad(DOB)-1)
            fecha_nacimiento_formateada = fecha_nacimiento.strftime('%Y-%m-%d')
            #print(fecha_nacimiento_formateada)
                
            return fecha_nacimiento_formateada
        else:
            while(True):
                DOB2 = generateDOB()
                dif = get_edad(DOB) - get_edad(DOB2)
                if(abs(dif)<=17):
                    return DOB2
    else: 
        while(True):
            DOB2 = generateDOB()
            dif = get_edad(DOB) - get_edad(DOB2)
            if(abs(dif)<=17):
                return DOB2 

def get_edad(DOB):
    import datetime
    fecha_actual = datetime.datetime.now()
    try:
        fecha_nacimiento_conversion = datetime.datetime.strptime(DOB, "%Y-%m-%d")
    except ValueError:
        print("La cadena no coincide con el formato esperado (YYYY-MM-DD).")
    edad = fecha_actual.year - fecha_nacimiento_conversion.year - ((fecha_actual.month, fecha_actual.day) < (
        fecha_nacimiento_conversion.month, fecha_nacimiento_conversion.day))

    print('edad:', edad)
    return edad
    
def validataDOBSiblings(seedDOB, DOB):
    difference = get_edad(seedDOB) - get_edad(DOB)
    if( difference >= 0 ):  #Es hermano mayor de la semilla
        if(get_edad(DOB) > 18): # Verificar si es mayor que
            return True
        else:
            return False
        
    