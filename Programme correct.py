import os
from math import*


def dateExist():                                                                #On crée la fonction qui définit si la date entrée existe réellement
    if (Day['value'] == "31"):
        if (Month['value'] == "avril" or Month['value'] == "juin" or Month['value'] == "septembre" or Month['value'] == "novembre"):
            return False
    if (Month['value'] == "février")or (Month['value']=="fevrier"):                                  # Si le jour saisi pour le mois de février est=31 ou =30 ou =29 alors que l'année n'est pas bissextile --> false
        if (Day['value'] == "31" or Day['value'] == "30" or (Day['value'] == "29" and bissextile(getYear()) == False)):
            return False
    return True                                                                      #Sinon --> true



def bissextile(annee):                                                            #On définit la fonction déterminant si l'année entrée est bissextile ou non.
    bissextile = False                                                             #Par défaut, on considère que l'année n'est pas bissextile, sauf si:
    if (annee % 400 == 0) or (annee % 4 == 0 and not annee % 100 == 0):              #Le reste de sa division par 400 est nul ou que le reste de sa division par 4 est nul et qu'elle n'est pas divisible par 100.
        bissextile = True                                                              #Dans ce cas précis, l'année est bissextile
    return bissextile


def nb_jour(annee):                                                             #On définit la fonction nombre de jour, permettant d'affecter le nombre de jours à l'année saisie si elle est bissextle ou non
    som = 0
    i = 1
    while i < annee:
        if bissextile(i):
            som += 366
        else:
            som += 365
        i += 1
    return som


def reste(jour, mois, annee):                                                       #on définit une fonction "reste" qui nous donnera le jour de l'année en question
    if not bissextile(annee):
        if mois == 'janvier':
            rest = jour - 1
        if mois == 'février' or mois == 'fevrier':
            rest = 31 + jour - 1
        if mois == 'mars':
            rest = 31 + 28 + jour - 1
        if mois == 'avril':
            rest = 31 + 28 + 31 + jour - 1
        if mois == 'mai':
            rest = 31 + 28 + 31 + 30 + jour - 1
        if mois == 'juin':
            rest = 31 + 28 + 31 + 30 + 31 + jour - 1
        if mois == 'juillet':
            rest = 31 + 28 + 31 + 30 + 31 + 30 + jour - 1
        if mois == 'aout' or mois == 'août':
            rest = 31 + 28 + 31 + 30 + 31 + 30 + 31 + jour - 1
        if mois == 'septembre':
            rest = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + jour - 1
        if mois == 'octobre':
            rest = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + jour - 1
        if mois == 'novembre':
            rest = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + jour - 1
        if mois == 'decembre' or mois=='décembre':
            rest = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + jour - 1
    else:
        if mois == 'janvier':
            rest = jour - 1
        if mois == 'février' or mois == 'fevrier':
            rest = 31 + jour - 1
        if mois == 'mars':
            rest = 31 + 29 + jour - 1
        if mois == 'avril':
            rest = 31 + 29 + 31 + jour - 1
        if mois == 'mai':
            rest = 31 + 29 + 31 + 30 + jour - 1
        if mois == 'juin':
            rest = 31 + 29 + 31 + 30 + 31 + jour - 1
        if mois == 'juillet':
            rest = 31 + 29 + 31 + 30 + 31 + 30 + jour - 1
        if mois == 'aout' or mois == 'août':
            rest = 31 + 29 + 31 + 30 + 31 + 30 + 31 + jour - 1
        if mois == 'septembre':
            rest = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + jour - 1
        if mois == 'octobre':
            rest = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + jour - 1
        if mois == 'novembre':
            rest = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + jour - 1
        if mois == 'decembre'or mois=='décembre':
            rest = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + jour - 1
    return rest


print("Ce programme va vous aider à déterminer le jour de la semaine d'une date saisie")
jour = int(input("Veuillez saisir le jour : "))
mois = input("Veuillez saisir le mois (en lettre) : ")
annee = input("Saisissez enfin l'année : ")
jour = int(jour)
annee = int(annee)
s = nb_jour(annee) + reste(jour, mois, annee)                               #On définit la variable 's' qui nous permettra le calcul du rang de la journée selon le résultat de s%7
if s % 7 == 0:
    print("Lundi, ", jour, mois, annee)
elif s % 7 == 1:
    print("Mardi, ", jour, mois, annee)
elif s % 7 == 2:
    print("Mercredi, ", jour, mois, annee)
elif s % 7 == 3:
    print("Jeudi, ", jour, mois, annee)
elif s % 7 == 4:
    print("Vendredi, ", jour, mois, annee)
elif s % 7 == 5:
    print("Samedi, ", jour, mois, annee)
else:
    print("Dimanche, ", jour, mois, annee)

