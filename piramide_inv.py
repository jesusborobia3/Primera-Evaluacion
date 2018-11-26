def piramide_inv():
     numero=input("numero n: ")
numcol=0
while numcol<=numero:
    fila=numcol
while (fila<numero):
     print fila,
    fila=fila+1
    print numcol,
    numcol=numcol+1
    print "\t"
piramide_inv()        
