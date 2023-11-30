

def secuencial(lista, info):
    pos = 0
    encontrado = False
    while pos < len(lista) and not encontrado:
        if lista[pos] == info:
            encontrado = True
        else:
            pos += 1
    return encontrado

def binariaIterativa(lista, info):
    izq = 0 
    der = len(lista) -1
    encontrado = False
    while izq <= der and not encontrado:
        mitad = (izq+der)//2
        if lista[mitad] == info:
            encontrado = True
            return encontrado
        elif lista[mitad] > info:
            der = mitad-1
        else:
            izq = mitad+1
    return encontrado

def binariaRecursiva(lista, info, menor, mayor):
    encontrado = False
    if mayor >= menor and not encontrado:
        mitad = (mayor + menor) // 2
        if lista[mitad] == info:
            encontrado = True
            return encontrado
        elif lista[mitad] > info:
            return binariaRecursiva(lista, info, menor, mitad-1)
        else:
            return binariaRecursiva(lista, info, mitad+1, mayor)
    else:
        return encontrado
