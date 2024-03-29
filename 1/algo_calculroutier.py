import math
import requests
from bs4 import BeautifulSoup

def program():
    start = input("\nEntrez le nom de la ville de départ : ")
    end = input("Entrez le nom de la ville d'arrivée : ")

    if(start != end):
        request = BeautifulSoup(requests.get(f"https://www.bonnesroutes.com/distance/?from={start}&to={end}").content, 'html.parser')
        error_msg = request.select('.message_error')
        error_start, error_end = request.select('.field_errors')[0].select('li'), request.select('.field_errors')[1].select('li')
        if(len(error_start) == 0 and len(error_start) == 0 and len(error_msg) == 0):
            distance = float(''.join(list(filter(str.isdigit, request.select('#total_distance .value')[0].text)))) * 1000
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
            if(len(error_msg) > 0):
                print(error_msg[0].text)
            if(len(error_start) > 0):
                print(f"Erreur pour la ville de départ ({start}) : {error_start[0].text}")
            if(len(error_end) > 0):
                print(f"Erreur pour la ville de départ ({end}) : {error_end[0].text}")
            return 1
    else:
        print("\nVous avez entré la même ville pour le départ et l'arrivée.")
        return 1

exit_code = program()
while(exit_code):
    exit_code = program()

input("\nAppuyez sur entrer pour fermer")