from Dijkstra import *

grafo = Grafo()
grafo.agregar_nodo('McDonalds')
grafo.agregar_nodo('Lider')# lider de la 2 norte
grafo.agregar_nodo('Copec')# copec de la 2 sur
grafo.agregar_nodo('Mall Portal Centro')
grafo.agregar_nodo('Plaza') 
grafo.agregar_nodo('Alameda') # altura 3 oriente
grafo.agregar_nodo('UST')
grafo.agregar_nodo('Colegio San Ignacio')
grafo.agregar_nodo('Completos') #5 sur
grafo.agregar_nodo('Biblioteca Municipal')

grafo.agregar_arista('Colegio San Ignacio', 'UST', 6)
grafo.agregar_arista('Colegio San Ignacio', 'Plaza', 4)
grafo.agregar_arista('Colegio San Ignacio', 'Alameda', 6)
grafo.agregar_arista('Colegio San Ignacio', 'Biblioteca Municipal', 8)
grafo.agregar_arista('UST', 'Copec', 5)
grafo.agregar_arista('Copec', 'Completos', 4)
grafo.agregar_arista('Plaza', 'Alameda', 5)
grafo.agregar_arista('Plaza', 'Biblioteca Municipal', 5)
grafo.agregar_arista('Plaza', 'McDonalds', 4)
grafo.agregar_arista('Plaza', 'Completos', 6)
grafo.agregar_arista('Plaza', 'Copec', 1)
grafo.agregar_arista('Alameda', 'Lider', 8)
grafo.agregar_arista('Alameda', 'Biblioteca Municipal', 4)
grafo.agregar_arista('Biblioteca Municipal', 'McDonalds', 1)
grafo.agregar_arista('Biblioteca Municipal', 'Lider', 3)
grafo.agregar_arista('McDonalds', 'Lider', 4)
grafo.agregar_arista('McDonalds', 'Completos', 3)
grafo.agregar_arista('McDonalds', 'Mall Portal Centro', 2)
grafo.agregar_arista('Mall Portal Centro', 'Lider', 1)
grafo.agregar_arista('Mall Portal Centro', 'Completos', 5)


nodo_inicial = 'Colegio San Ignacio'
nodo_destino = 'Copec'

ruta_eficiente = dijkstra_unica_ruta(grafo, nodo_inicial, nodo_destino)

if ruta_eficiente:
    print(f"Ruta más eficiente desde {nodo_inicial} hasta {nodo_destino}: {ruta_eficiente}")
else:
    print(f"No hay ruta desde {nodo_inicial} hasta {nodo_destino}")
