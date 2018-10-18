def cambio_moneda():
    moneda= input("Cuanto dinero tienes?")
    if (moneda<0):
        print "Eres pobre, lo siento"
    else:
        respuesta=raw_input("dolares o libras? (d/l)")
        if(respuesta== "d"):
         print moneda*1.15
        if (respuesta=="l"):
         print moneda*0.88
            

cambio_moneda()            
                
    
