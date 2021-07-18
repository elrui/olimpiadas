''''
Librería de funciones para manejo de medalleros olímpicos
'''

import csv

FIELDS = ['id', 'name', 'country', 'sport', 'gold', 'silver', 'bronze']

## Sample record:  ('111', 'Jhon Goodman', 'US', 'Running', '1', '3', '0')
## Title/Header: (id, name, country, sport, gold, silver, bronze)

## Create a dictionary {id: Athlete}

def readFile(filename, fields=FIELDS, delimiter=','):
    '''
    This function takes a filename and returns a list of records from the file
    The records are of type dictionary
    '''

    athletes = [] 
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)     # don't pass fields if file has headers
    
        for row in reader:
            athletes.append(row)

    return athletes
            
def writeFile(filename, athletes, fields=FIELDS, delimiter=','):
    '''
    This function takes a filename and a list of records, and save the records in said file
    Fields must be specified in order to write headers
    The records are of type dictionary
    '''

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields, delimiter=delimiter)

        writer.writeheader()
        for row in athletes:
            writer.writerow(row)

def createFile(filename, fields=FIELDS):
    '''
    Initialize a file with headers
    '''

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        writer.writeheader()

def findAthlete(id, registry):

    for person in registry:
        if person['id'] == str(id):
            return person
    
    return False

def createAthlete(id, name, country, sport, registry):
    '''
    Answers the question 
    1. Registro de atleta
    '''

    if findAthlete(id, registry):
        return False      ## Athlete already exists, so function fails and returns False
    else:
        newath = {}
        newath['id']      = str(id)
        newath['name']    = name
        newath['country'] = country
        newath['sport']   = sport
        newath['gold']    = '0'
        newath['silver']  = '0'
        newath['bronze']  = '0'

        registry.append(newath)
        return registry


def byCountry(country, registry):
    '''
    Answers the question
    2. Consulta de Medallas obtenidas por un país X. 
    (Nombre del Atleta, Deporte y Cantidad de Medallas).
    '''

    result = []

    for person in registry:
        if person['country'] == country:
            result.append(person)
    
    return result

def bySport(sport, registry):
    '''
    Finds all athletes and medals by sport
    '''

    result = []

    for person in registry:
        if person['sport'] == sport:
            result.append(person)
    
    return result

def addMedal(id, type, qty, registry):
    '''
    Add medal to a given athlete
    '''
    athlete = findAthlete(id, registry)

    if not athlete:
        return registry
    else: 
        athlete[type] = str(int(athlete[type]) + qty)   ### this works because lists support changes in place
        return registry


def totalByCountry(country, registry):
    gold = silver = bronze = 0

    for person in registry:
        if person['country'] == country:
            gold += int(person['gold'])
            silver += int(person['silver'])
            bronze += int(person['bronze'])
    
    return (gold, silver, bronze)
            

