
from math import*



def jourexist():                                                                #on crée une fonction qui permet de définir si le jour entré existe
    if (jour >31 or jour <1):
        return False
        print("Veuillez saisir un jour correct")
        return True


                                                                                    # Retourne True si la date saisie existe
def dateExist():
    if (jour['value'] == "31"):
        if (mois['value'] == "avril" or mois['value'] == "juin" or mois['value'] == "septembre" or mois ['value'] == "novembre"):
            return False
    if (mois['value'] == "février"):                                                 # Si le jour saisi pour le mois de février est=31 ou =30 ou =29 alors que l'année n'est pas bissextile alors --> false
        if (jour['value'] == "31" or jour['value'] == "30" or (jour['value'] == "29" and bissextile(getYear()) == False)):
            return False
    return True                                                                      # Sinon --> true


# Retourne true si l'année est bissextile
def bissextile(annee):
    bissextile = False  # Par défaut, on considére l'année saisie comme non bissextile, sauf:
    if (annee % 400 == 0) or (
            annee % 4 == 0 and not annee % 100 == 0):  # Si l'année est divisible par 400, divisible par 4 mais pas par 100
        bissextile = True
    return bissextile


# Retourne true si le mois saisit est janvier ou février
def monthJanuaryOrFebruary():
    if (mois['value'] == 'janvier' or mois['value'] == 'février'):
        return True
    else:
        return False


# Retourne true si l'année saisie est comprise entre 1600 et 2200 (sinon aucun nombre n'est associé au siècle)
def checkYear():
    try:
        if (int(entryYear.get()) >= 1600 and int(entryYear.get()) < 2200):
            return True
    except:
        return False


# Retourne l'année sous le format integer
def getYear():
    return int(annee)


# Retourne le nombre à ajouter selon le mois transmis en paramètre
def getNumberToAddMonth():
    try:
        mois= mois['value']

        if Month == 'janvier':
            return 0
        elif Month == 'février':
            return 3
        elif Month == 'mars':
            return 3
        elif Month == 'avril':
            return 6
        elif Month == 'mai':
            return 1
        elif Month == 'juin':
            return 4
        elif Month == 'juillet':
            return 6
        elif Month == 'août':
            return 2
        elif Month == 'septembre':
            return 5
        elif Month == 'octobre':
            return 0
        elif Month == 'novembre':
            return 3
        elif Month == 'decembre':
            return 5
    except:
        # Message d'erreur si le mois n'a pas été saisi
        entryText.set("Veuillez sélectionner un mois")

        # Convertis le numéro de jour du mois en integer (nomre entier)


def getNumberToAddDay():
    try:
        return int(comboDay['value'])
    except:
        # Message d'erreur si la journée n'a pas été saisie
        entryText.set("Veuillez sélectionner un jour")


# Retourne le nombre à ajouter selon le siècle de l'année entrée
def getNumberToAddCentury():
    century = int(str(getYear())[:2])
    if century == 16:
        return int(6)
    elif century == 17:
        return int(4)
    elif century == 18:
        return int(2)
    elif century == 19:
        return int(0)
    elif century == 20:
        return int(6)
    elif century == 21:
        return int(4)


# Retourne le jour de la semaine selon le nombre transmis en paramètre
def getDayOfWeek(number):
    if number == 0 or number == 7:
        return 'Dimanche'
    elif number == 1:
        return 'Lundi'
    elif number == 2:
        return 'Mardi'
    elif number == 3:
        return 'Mercredi'
    elif number == 4:
        return 'Jeudi'
    elif number == 5:
        return 'Vendredi'
    elif number == 6:
        return 'Samedi'


def dayOfWeek():
    if (checkYear()):
        if dateExist():
            # On récupère les deux derniers chiffres de la date saisie
            last2Character = int(str(getYear())[-2:])

            # On divise par 4 sans se soucier du reste
            numberDivBy4 = last2Character + int(last2Character / 4)

            # On ajoute la journée du mois
            addedDay = numberDivBy4 + getNumberToAddDay()

            # On ajoute selon le mois
            addedMonth = addedDay + getNumberToAddMonth()

            if (bissextile(getYear()) and monthJanuaryOrFebruary()):
                addedMonth = addedMonth - 1

            addedCentury = addedMonth + int(getNumberToAddCentury())

            moduloBy7 = addedCentury % 7

            dayOfWeek = getDayOfWeek(moduloBy7)

            print('Cette date correspond à : ' + dayOfWeek)
        else:
            # Message d'erreur si l'année est mal saisie
            print("La date entrée n'existe pas.")


print ("Ce programme permet le calcul du jour exact d'une date saisie, il fonctionne pour les dates comprises entre l'année 1600 et 2200")
jour=int(input("Veuillez saisir le jour :"))
mois= str(input("Veuillez saisir le mois (en lettre):"))
annee= int(input("Veuillez saisir l'année (sous forme '1XXX' s'il vous plait):"))


print(dayOfWeek())



