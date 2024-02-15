listaNom = ["Pedro", "Juan", "Pedrito","Juanito","Juanon", "Pedrón"]
listaHora = [40, 50, 20, 23, 30, 42]
listaPrecio = [35, 12, 22, 11, 14, 100]

i = 0
while i < 6:
    print("El trabajador " + listaNom[i] + " que trabajó " + str(listaHora[i]) + " con un costo de cada hora de: $" + str(listaPrecio[i]))
    i+= 1
