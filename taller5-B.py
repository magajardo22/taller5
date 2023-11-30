import random
from random import sample
import timeit
from heap import *
from busqueda import *

listas = sample(range(1000000000),10000)
# menor a mayor

heap = Heap(len(listas))
heap.tamanio = len(listas)
heap.vector = listas
    
monticulizar(heap)
HeapSort(heap)

menor = heap.vector[0]
medio = heap.vector[(heap.tamanio//2)-1]
mayor = heap.vector[heap.tamanio-1]
n_random = random.choice(listas) 


time = timeit.timeit("secuencial(heap.vector,menor)",globals=globals(),number = 10)

print(time/10)

