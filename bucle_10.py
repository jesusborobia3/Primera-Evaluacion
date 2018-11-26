def bucle_10():
    nfinal=input("Hasta que numero quieres sumar?")
    numeros_pares=0
    numeros_impares=0
    for numero in range (1,nfinal+1):
        if (numero%2==0):
            print str(numero), "es par"
            numeros_pares=numeros_pares+1
        else:
            print str(numero)," es impar"
            numeros_impares=numeros_impares+1
    print "He contado", numeros_pares,"números pares"
    print "He contado", numeros_impares, "números impares"
bucle_10()

            
