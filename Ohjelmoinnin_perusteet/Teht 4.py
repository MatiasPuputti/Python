#Sanat joilla ohjelma suoritetaan uudelleen.
yeslist = ['YES', 'Yes', 'yes', 'Y', 'y']       

#Sanat joilla ohjelmaa ei suoriteta uudelleen.
nolist = ['NO', 'No', 'no', 'N', 'n']           

#Sanat jotka ovat hyväksyttäviä.
lista = ['YES', 'Yes', 'yes', 'Y', 'y', 'NO', 'No', 'no', 'N', 'n'] 

#Functio joka yhdistää listat yhdeksi halutunlaiseksi listaksi.
def listayhd():                                 

    #"Kirjanlistan" arvot.
    list1 = ['a', 'b', 'c']

    #"Numerolistan" arvot.
    list2 = [1, 2, 3]                           

    #Tyhjä lista johon arvot asetetaan.
    lista3 = []                                 

    # Loop jolla listojen yhdistys tehdään ottamalla vuorotellen molemmista.
    for i in range(3):     

        #Lisää "Kirjainlistan" arvon uuteen listaan.
        lista3.append(list1[i])                 

        #Lisää "Numerolistan" arvon uuteen listaan.
        lista3.append(list2[i])                 

    #Palauttaa muodostuneen listan.    
    return lista3                               

#Functio joka tulostaa saamansa arvon ja kysyy suoritetaanko uudelleen.
def tulosta():                                  

    #Tulostaa vastaanottamansa arvon.
    print(listayhd())                           

    #Asettaa arvon jolla ohjelma suoritetaan tai ei.
    suorita = input('Haluatko suorittaa ohjelman uudestaan (Yes/No)') 

    #Tulostaa tyhjän rivin ohjelman luettavuutta parantaakseen.
    print('')                                   

    #Jos Muuttuja löytyy tästä listasta ohjelma suoriutuu uudestaan.
    if suorita in yeslist:                      

        #Suoritettava ohjelma.
        tulosta()                              

    #Jos Muuttuja löytyy tästä listasta ohjelma ei suoriudu uudestaan.
    if suorita in nolist:          

        #Mitään ei tapahdu "Placeholder".             
        pass                                    

    #Jos muuttujan arvo ei ole listassa, kysytään uudestaan kunnes on.
    while suorita not in lista:                

        #Ohje käyttäjälle.
        print('Anna vastauksesi muodossa: (Yes/No)')  

        #Tyhjä rivi ohjelman lukemista helpottamaan.
        print('')                                     

        #Kysyy arvoa ohjelman suoritusta varten.
        suorita = input('Halutko suorittaa ohjelman uudelleen:(Yes/No)')  

        #Tyhjä rivi ohjelman lukemista helpottamaan.
        print('')                               

        #Tarkastaa suoritetaanko ohjelma uudestaan.
        if suorita in yeslist:                  

            #Suoritettava ohjelma.
            tulosta()                           

        #Tarkastaa eikö ohjelmaa suoriteta uudestaan.
        if suorita in nolist:                   

            #Ei te mitään "placeholder".
            pass                                


tulosta()                                       # Matias Puputti NEA18SPC
