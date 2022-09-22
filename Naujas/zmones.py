import pickle
# apsirasom skaitymo funkcija
def perziura():
    try:
        with open("Naujas/zmones.pkl", 'rb') as failas:
            zmones = pickle.load(failas)
    except Exception as e:
        print('nepavyko nuskaityti failo, klaida:',e)
        return []
    else:
        for zmogus in zmones:
            print(zmogus)
        return zmones

# apsirasom irasymo funkcija
def irasymas(zmones):
    vardas = input('Iveskite varda: ') # leidzia vartotojui ivesti nauja varda
    zmones.append(vardas) # ta varda prideda i sarasa
    with open("Naujas/zmones.pkl", 'wb') as failas: #ta atnaujinta sarasa irasom i pickle faila
        pickle.dump(zmones,failas)
    return zmones #grazi

zmones = []
while True:
    veiksmas = input('zmoniu katalogas:\n 1 - perziureti\n 2 - irasyti\n bet kas kitas - iseiti')
    if veiksmas == '1':
        zmones = perziura()
    elif veiksmas == '2':
        zmones = irasymas(zmones)
    else:
        print('Programa baigta')
        break