def condicional_2 ():
    respuesta = raw_input("Que hora es?")
    if (int(respuesta)<12):
        print "Buenos días"
    else:
        if(int(respuesta)>=12):
           print "Buenas tardes"
        else:
           print "Buenas noches"
        if (int(respuesta)>24):
            print "Introduce un número válido"
condicional_2 ()               
           
        
        

