import math

villes = {
    "Bordeaux": {
        "Poitiers": 250,
        "Pau": 207,
        "Limoges": 221,
        "Orthez": 191,
        "Royan": 131,
        "Ussel": 288,
        "Laluque Gare": 144,
        "Tulle": 227,
        "Bressuire": 253
    },
    "Poitiers": {
        "Bordeaux": 250,
        "Pau": 450,
        "Limoges": 119,
        "Orthez": 435,
        "Royan": 176,
        "Ussel": 269,
        "Laluque Gare": 395,
        "Tulle": 209,
        "Bressuire": 83
    },
    "Pau": {
        "Bordeaux": 207,
        "Poitiers": 450,
        "Limoges": 432,
        "Orthez": 48,
        "Royan": 342,
        "Ussel": 486,
        "Laluque Gare": 97,
        "Tulle": 426,
        "Bressuire": 464
    },
    "Limoges": {
        "Bordeaux": 221,
        "Poitiers": 119,
        "Pau": 432,
        "Orthez": 406,
        "Royan": 210,
        "Ussel": 149,
        "Laluque Gare": 366,
        "Tulle": 88,
        "Bressuire": 202
    },
    "Orthez": {
        "Bordeaux": 191,
        "Poitiers": 435,
        "Pau": 48,
        "Limoges": 406,
        "Royan": 316,
        "Ussel": 472,
        "Laluque Gare": 50,
        "Tulle": 411,
        "Bressuire": 438,
    },
    "Royan": {
        "Bordeaux": 131,
        "Poitiers": 176,
        "Pau": 342,
        "Limoges": 210,
        "Orthez": 316,
        "Ussel": 370,
        "Laluque Gare": 266,
        "Tulle": 309,
        "Bressuire": 179,
    },
    "Ussel": {
        "Bordeaux": 288,
        "Poitiers": 269,
        "Pau": 486,
        "Limoges": 149,
        "Orthez": 472,
        "Royan": 370,
        "Laluque Gare": 434,
        "Tulle": 63,
        "Bressuire": 352,
    },
    "Laluque Gare": {
        "Bordeaux": 144,
        "Poitiers": 395,
        "Pau": 97,
        "Limoges": 366,
        "Orthez": 50,
        "Royan": 266,
        "Ussel": 434,
        "Tulle": 368,
        "Bressuire": 395,
    },
    "Tulle": {
        "Bordeaux": 227,
        "Poitiers": 209,
        "Pau": 426,
        "Limoges": 88,
        "Orthez": 411,
        "Royan": 309,
        "Ussel": 63,
        "Laluque Gare": 368,
        "Bressuire": 291
    },
    "Bressuire": {
        "Bordeaux": 253,
        "Poitiers": 83,
        "Pau": 464,
        "Limoges": 202,
        "Orthez": 438,
        "Royan": 179,
        "Ussel": 352,
        "Laluque Gare": 395,
        "Tulle": 291
    }
}

def program():
    start = input("\nEntrez le nom de la ville de départ : ")
    end = input("Entrez le nom de la ville d'arrivée : ")

    if(start != end):
        if(start.capitalize() in villes):
            if(end.capitalize() in villes[start.capitalize()]):
                distance = villes[start.capitalize()][end.capitalize()] * 1000
                done = 0
                seconds = 0
                speed = 0
                last_pause = 0
                nb_pause = 0
                has_to_pause = False
                while(done < distance):
                    if(seconds != 0 and (seconds-last_pause) % (60*60*2) == 0):
                        has_to_pause = True
                    if(speed < 90 and has_to_pause == False):
                        if(speed + 10/60 <= 90):
                            speed += 10/60
                        else:
                            speed = 90
                    if(has_to_pause and speed > 0):
                        if(speed - 10/60 >= 0):
                            speed -= 10/60
                        else:
                            speed = 0
                    elif(has_to_pause and speed == 0):
                        nb_pause += 1
                        seconds += 60*15
                        last_pause = seconds
                        has_to_pause = False
                    done += (speed/3.6)
                    seconds += 1
                print(seconds)
                hours = 0
                minutes = 0
                if(seconds/60 > 0):
                    if(seconds/3600 > 0):
                        hours = math.floor(seconds/3600)
                    minutes = math.ceil((seconds % 3600)/60)

                print('------------------------------------------------------------------------------------')
                print('Départ :', start.capitalize(), '| Arrivée :', end.capitalize(), '|', distance/1000, 'km | ', "{}:{}".format(hours, minutes), "(dont {} minutes de pause)".format(nb_pause * 15))
                print('------------------------------------------------------------------------------------')
                return 0
            else:
                print("\nLa ville '{}' n'est pas autorisée.".format(end))
                return 1
        else:
            print("\nLa ville '{}' n'est pas autorisée.".format(start))
            return 1
    else:
        print("\nVous avez entré la même ville pour le départ et l'arrivée.")
        return 1

exit_code = program()
while(exit_code):
    exit_code = program()

input("\nAppuyez sur entrer pour fermer")