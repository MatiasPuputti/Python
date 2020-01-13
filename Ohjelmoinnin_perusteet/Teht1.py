#Sanat joita verrataan Rivillä 24 suorita muuttujaan.
yeslist = ['YES', 'Yes', 'yes', 'Y', 'y']

#Sanat joita verrataan Rivillä 27 suorita muuttujaan.       
nolist = ['NO', 'No', 'no', 'N', 'n']

#sallitut vastaukset uudelleen suoritukseen.
mislist = ['YES', 'Yes', 'yes', 'Y', 'y', 'NO', 'No', 'no', 'N', 'n']

#kertotaulut ohjelman määritys
def kertotaulut():

    #Tulostaa mitä kertotaulua ollaan suorittamassa.
    print('Kahden kertotaulu:')                  

    #Kertotaulun suoritus loop jolla lasketaan kertojilla 1-10.
    for i in range(1, 11): 
        # Tuloste jossa näkyy suoritettu lasku ja laskun arvot.                    
        print(i, '*', 2, '=', 2*i)
    #Kertotaulujen väliin lisätty tyhjä rivi jotta selkeämpi lukea.              
    print('')                                   

    #Tulostaa mitä kertotaulua ollaan suorittamassa.
    print('Neljän kertotaulu:')

    #Kertotaulun suoritus loop jolla lasketaan kertojilla 1-10.                 
    for i in range(1, 11):
        # Tuloste jossa näkyy suoritettu lasku ja laskun arvot.                      
        print(i, '*', 4, '=', 4*i)

    #Kertotaulujen väliin lisätty tyhjä rivi jotta selkeämpi lukea.                  
    print('')                                   

    #Tulostaa mitä kertotaulua ollaan suorittamassa.
    print('Kuuden kertotaulu:')

    #Kertotaulun suoritus loop jolla lasketaan kertojilla 1-10.                  
    for i in range(1, 11):      
        # Tuloste jossa näkyy suoritettu lasku ja laskun arvot.                
        print(i, '*', 6, '=', 6 * i)

    #Kertotaulujen väliin lisätty tyhjä rivi jotta selkeämpi lukea.                
    print('')                                   

    #Käyttäjän arvo ohjelman uudelleensuoritukseen.
    suorita = input('Haluatko suorittaa ohjelman uudestaan (Yes/No)')

    #Jos suorita on yeslist:ssa ohjelma suoriutuu uudestaan.
    if suorita in yeslist:                      
        kertotaulut()

    #Jos muuttaja on nolist:ssa ohjelman suoritus loppuu.
    if suorita in nolist:                     
        pass

    #Kysyy käyttäjältä muuttujaa uudestaan kunnes se on sallittu vastaus.
    while suorita not in mislist:               

        #Tulostaa ohjeen käyttäjälle.
        print('Virheellinen vastaus, anna vastauksesi muodossa: (Yes/No)') 

        #Tulostaa tyhjän rivin jotta helpompi lukea ohjelmaa.
        print('')                   

        #Kysyy muuttujaa uudestaan.
        suorita = input('Halutko suorittaa ohjelman uudelleen:(Yes/No)') 
        #Tulostaa tyhjän rivin jotta ohjelmaa helpompi lukea.
        print('')                               

        #Jos suorita on yeslist:ssa ohjelma suoriutuu uudestaan.
        if suorita in yeslist:                  
            kertotaulut()

        #Jos muuttaja on nolist:ssa ohjelman suoritus loppuu.
        if suorita in nolist:                   
            pass


kertotaulut()                                    # Matias Puputti NEA18SPC
