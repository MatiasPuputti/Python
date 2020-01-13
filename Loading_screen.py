#Käytetään seuraavan "framen" ajastukseen. 
import time

#Animaation "framet".
loalis = ['|', '/', '-', '\\', '|', '/', '-', '\\']

#Load function määritys.
def load():

    #Kahdenksan "framen animaatio".
    for i in range(8):

        #Tulostaa consoleen tulevan lataus animaation.
        print('Loading', '|', loalis[i], '| ', i * '.', end="\r", sep='')

        #Odotus "framejen vaihtumisen välillä".
        time.sleep(0.5)

    #Tulostaa pyörivän viivan rajat.
    print('Loading | |           ', end="\r")


while True:
    load()
