import random
import time 
from heap import *


listas = []

while len(listas) <= 100: #de cien a un millon
    listas.append(random.randint(0,1000))
# menor a mayor

heap = Heap(len(listas))
heap.tamanio = len(listas)
heap.vector = listas

#calculo del tiempo
inicio = time.time()
monticulizar(heap)
HeapSort(heap)
fin = time.time()

print(fin-inicio)












