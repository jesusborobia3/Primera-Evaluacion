def condicional_2 ():
    respuesta = raw_input("Que hora es?")
    if (int(respuesta)<12):
        print "Buenos d�as"
    else:
        if(int(respuesta)>=12):
           print "Buenas tardes"
        else:
           print "Buenas noches"
        if (int(respuesta)>24):
            print "Introduce un n�mero v�lido"
condicional_2 ()               
           
        
        

