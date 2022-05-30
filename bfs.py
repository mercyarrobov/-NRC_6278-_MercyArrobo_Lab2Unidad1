#Importación de Queue
from queue import Queue

class Grafo:  
     #Constructor
    def __init__(self, num_de_nodos, directo=True):
        
        #Número de aristas
        self.m_num_de_nodos = num_de_nodos 
        #Inicializa el rango de los nodos
        self.m_nodos = range(self.m_num_de_nodos)
        #Definir el tipo de un grafo
        self.m_directo = directo
        # Lista de adyacencia usando diccionario
        self.m_list_ady = {nodo: set() for nodo in self.m_nodos}  