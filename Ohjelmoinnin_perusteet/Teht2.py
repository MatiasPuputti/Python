#Lista joka säilöö tiedon onko lukua kysytty ennen.
suor = []

#Arvot joilla ohjelma suorituu uudelleen.                                       
yeslist = ['YES', 'Yes', 'yes', 'Y', 'y']

#Arvot joilla ohjelma suoriutuu uudelleen.
nolist = ['NO', 'No', 'no', 'N', 'n']     

#Sallitut vastaukset.
lista = ['YES', 'Yes', 'yes', 'Y', 'y', 'NO', 'No', 'no', 'N', 'n']  

 #summakone ohjelman määritys.
def summakone():                                
    #Tuo suor listan globalista localiin.
    global suor

     #Antaa muuttujalle s2 arvon jotta rivi 37 ei tule error.                                 
    s2 = ''

    #Luo listan arvoille jotka käyttäjä syöttää ja palautuu tyhjäksi.                                     
    luvut = []    

    #Luo muuttujan jolle summataan käyttäjän antamat arvot ja muuttuu 0:si.                              
    summa = 0         

    #Pitää muistissa ohjelman suorituskerrat.                          
    suorituskerrat = sum(suor)                  

    #Suorittaa komennot jos ehdot täyttyy.
    if suorituskerrat == 0:

        #Input joka tulee kun lukua kysytään 1. kerran.                     
        luku = int(input('Anna luku:')) 

        #Lisää käyttäjän ensimmäisenä antaman arvon listaan.        
        luvut.append(luku)               

        #Input joka tulee kun lukua kysytään 2. kerran.       
        luku = int(input('Anna toinen luku:'))  

        #Lisää käyttäjän toisena antaman arvon listaan.
        luvut.append(luku)                      

        #Summaa käyttäjän antamat arvot.
        summa = sum(luvut)                      

         #Lisää suorituskertaan yhden.
        suor.append(1)                          

    #Suorittaa komennot jos ehdot täyttyy.
    if suorituskerrat >= 1:           

        #Input jota kysytään kun luku on kysytty useammin kuin kaksi kertaa.          
        luku = int(input('Anna uudet luvut:')) 

        #Lisää käyttäjän antaman arvon listaan.
        luvut.append(luku)                      

        #Input jota kysytään kun luku on kysytty useammin kuin kaksi kertaa.
        luku = int(input('Anna uudet luvut:'))  

        #Lisää käyttäjän antaman arvon listaan.
        luvut.append(luku)                      

        #Summaa käyttäjän antamat arvot.
        summa = sum(luvut)                      

    #Suorittaa komennot jos ehdot täyttyy.
    if summa <= 99:                             

        #Tulostaa lauseen ja summa muuttujan.
        print('Kivat luvut, ne on yhteenlaskettuna', summa)  

        #Tulostaa tyhjän rivin ohjelman lukua helpottamaan.
        print('')                                           

        #Kysyy arvoa ohjelman uudelleen suorittamiseen.
        s2 = input('Haluatko suorittaa ohjelman uudelleen:(Yes/No)') 

    #Suorittaa komennot jos ehdot täyttyvät
    if summa > 99:                 

        #Tulostaa "virheilmoituksen"             
        print('Aika isot luvut annoit!')        

         #Tulostaa tyhjän rivin ohjelman lukua helpottamaan.
        print('')                               

        #Kysyy arvoa ohjelman uudelleen suorittamiseen.
        s2 = input('Halutko suorittaa ohjelman uudelleen:(Yes/No)')   

    #Tarkastaa suoritetaanko ohjelma uudestaan.
    if s2 in yeslist:         

        #Suoritettava ohjelma.                 
        summakone()                             

    #Tarkastaa eikö ohjelmaa suoriteta uudestaan.
    if s2 in nolist:              

        #Ei te mitään "placeholder"              
        pass                                    
    #Jos muuttujan arvo ei ole listassa, kysytään uudestaan kunnes on.
    while s2 not in lista:                      

        #Ohje käyttäjälle.
        print('Anna vastauksesi muodossa: (Yes/No)')  

        #Tyhjä rivi ohjelman lukemista helpottamaan.
        print('')                                     

        #Kysyy arvoa ohjelman uudelleen suoritusta varten.
        s2 = input('Halutko suorittaa ohjelman uudelleen:(Yes/No)')

        # Tyhjä rivi ohjelman lukemista helpottamaan.
        print('')                               

        #Tarkastaa suoritetaanko ohjelma uudestaan.
        if s2 in yeslist:       

            #Suoritettava ohjelma.
            summakone()                         

        # Tarkastaa eikö ohjelmaa suoriteta uudestaan.
        if s2 in nolist:                

            #Ei te mitään "placeholder".
            pass                               


summakone()                                     # Matias Puputti NEA18SPC
