# coding: utf8
def Summakone2():
    operaatio = 0
    numerolista = []
    ohjsuor = 0

    while (operaatio != 'Summa' and operaatio != 'summa' and operaatio != 'Sum' and operaatio != 'sum'
           and operaatio != 'Erotus' and operaatio != 'erotus' and operaatio != 'ero' and operaatio != "Kertoma" and
           operaatio != "kertoma"and operaatio != "ker" ):
        try:
            if ohjsuor == 0:
                operaatio = input('Anna luvut ja kerro lopuksi haluatko summan, erotuksen vai kertoman.')
            if ohjsuor != 0:
                operaatio = input('Anna uudet luvut ja kerro lopuksi haluatko summan, erotuksen vai kertoman.')

            if (operaatio  != 'Summa' and operaatio != 'summa' and operaatio != 'Erotus' and operaatio != 'erotus' and
                operaatio != 'ero' and operaatio != 'Kertoma' and operaatio != 'kertoma' and operaatio != 'ker'
                and operaatio != 'Sum' and operaatio != 'sum'):
                numerolista.append(int(operaatio))

            if operaatio == 'Summa' or operaatio == 'summa' or operaatio == 'Sum' or operaatio == 'sum':
                s1 = sum(numerolista)
                print('Summa= ',s1,sep='')
                operaatio = 0
                ohjsuor += 1
                del numerolista[:]

            if operaatio == 'Erotus' or operaatio == 'erotus' or operaatio == 'ero':
                s1 = sum(numerolista)
                print('Erotus= ''-',s1, sep='')
                operaatio = 0
                ohjsuor += 1
                del numerolista[:]

            if operaatio == "Kertoma" or operaatio == "kertoma" or operaatio == "ker":
                s1 = sum(numerolista)
                if int(s1) <= 109:
                    print('Kertoma luvulle ', s1,':', sep='')
                    b = 1
                    for j in range(0, int(s1)):
                        b = b * (j + 1)
                    print(b)
                    print('Luvussa on', len(str(b)), 'numeroa')
                    operaatio = 0
                    ohjsuor += 1
                    del numerolista[:]

                if s1 >= 109 and s1 <= 205000:  # Why you no work yet????????
                    print('Kertomaa ei lasketa loopilla')

                if s1 >= 110 and s1 <= 205000:
                    import math
                    import decimal
                    print('Lasketaan kertoma Strirlingin kaavalla:')
                    c = (((decimal.Decimal(s1) / decimal.Decimal(math.exp(1))) ** decimal.Decimal(s1))
                    * (decimal.Decimal(math.sqrt(2 * decimal.Decimal(math.pi) * decimal.Decimal(s1)))))
                    print(c)
                    operaatio = 0
                    ohjsuor += 1
                    del numerolista[:]
                if s1 >= 205000:
                    print('Luku ylittää käsittelykyvyn 205 000 kohdalla.')
                    operaatio = 0
                    ohjsuor += 1
                    numerolista = []

        except:
            print('Try again Rocket Surgeon !!!')
            del numerolista[:]

Summakone2()