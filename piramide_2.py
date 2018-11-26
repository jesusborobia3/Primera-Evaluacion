def bucle_8():
    print "Indica la altura de la piramide"
    altura=input("altura = ")
    for fila in range (1,altura+1):
        for col in range (1,fila+1):
            print "*",
        print " "
bucle_8()        
