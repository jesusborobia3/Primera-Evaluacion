def piramide():
     y=input("Ingrese el numero de filas")
     for i in range (0,y):
         for i in range (0,i+1,1):
             print "*",
         print ""
piramide()
