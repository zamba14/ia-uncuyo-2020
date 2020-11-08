#Reporte búsqueda informada A*

Para el algoritmo de búsqueda informada A* se utilizó como base lo propuesto por TechWithTim en el siguiente enlace: https://www.youtube.com/watch?v=JtiK0DOeI4A&t=2894s

El mismo consiste en una clase Node que almacenara cada cuadro de la grilla: su posición en las coordenadas x e y, los nodos a los que se puede acceder desde el y el "tipo" de nodo
(lo cual será relevante para imprimir por pantalla los resultados).

En lugar de implementar la visualización del algoritmo mediante el módulo pygame, como en el caso del tutorial, se prefirió utilizar los módulos Colorama y Termcolor para dar color a los
caracteres de la terminal de Python; dibujando así dos caracteres █ por cada nodo con un color correspondiente a su "tipo". (NOTA: para que el resultado se imprima correctamente en 
una grilla de 100x100 es mejor utilizar un solo caracter en lugar de dos. El código fuente mantiene la utilización de dos caracteres en una grilla de 50x50 para que se pueda visualizar
mejor el proceso)

A partir de la línea 139 se encuentra la ejecución del algoritmo. Comienza llamando a la función init() del módulo colorama para poder parsear los códigos de colores provistos por
termcolor.

Luego se inicializa una variable grid_size que contendrá el tamaño de la grilla a generar, pasándola como argumento a las funciones make_grid y make_obstacules
La primera nos devolverá la grilla en sí, generando un objeto de clase Node en una matriz de grid_size * grid_size e inicializando todos los nodos a con tipo "white" (que corresponde al nodo abierto). 
El segundo método genera aleatoriamente grid_size x 5 obstáculos (tipo "red") que serán las barreras que marcarán el sendero por el cual deba moverse la solución; más los puntos de inicio y fin también aleatoriamente. (Se utilizó numpy.random.randint para generar seudoaleatoriamente los valores de x e y de cada nodo obstáculo, inicio y fin)

Acto seguido se corre el método aStar, donde se encuentra el algoritmo de búsqueda informada.

	__recibe como parámetros la grilla generada más los nodos de inicio y fin__
	def aStar(grid, start, end):
	__inicializa una cuenta para resolver la paridad entre dos nodos que tengan el mismo valor de f(n), almacenando en qué orden fue añadido a la lista__
    count = 0
	__inicializa una PriorityQueue para llevar el set de nodos a explorar__
    open_set = PriorityQueue()
	__coloca el nodo de comienzo al principio de la Queue con valor de f(0) y count 0__
    open_set.put((0,count,start))
	__inicializa un diccionario para almacenar desde qué nodo fue expandido cada hijo, lo cual será relevante para revelar el camino más corto__
    came_from = {}
	__inicializa en infinito una matriz con los valores de g(n) y f(n) donde g(n) es el costo de transitar a cada nodo y f(n) la suma del costo +  la heurística 	de cada nodo__
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
	__en el caso del nodo inicial, la f(n) es igual a su heurística dado que el costo es 0 __
    f_score[start] = h(start.get_pos(), end.get_pos())

	__utiliza un dicionario para indexar los nodos que se encuentran en el set a explorar__
    open_set_hash = {start}

	__bucle de ejecución mientras el set de nodos a explorar se encuentre vacío__
    while not open_set.empty():
		__dado que la priorityqueue colocará primero a los valores con menos f(n) y count, accediendo al primer elemento con el método get() tomamos el mejor candidato a explorar__
        current_node = open_set.get()[2]
		__y lo removemos del diccionario que guarda los nodos a explorar__
        open_set_hash.remove(current_node)

        if current_node == end:
			__si es el nodo final, ya podemos trazar el recorrido, las llamadas a make_end y make_start es para que vuelva a colorear los nodos de comienzo y final con sus colores
			originales (que han sido sobreescritos mientras se exploraba el grafo)__
            make_path(came_from, end)
            end.make_end()
            start.make_start()
			__interrumpimos el bucle while__
            break
		__si no es el nodo final, se buscan los vecinos de ese nodo. (NOTA: En el video se inicializan los vecinos de todos los nodos una vez que se crea la grilla. con ambos procedimientos
		el resultado no se altera, por lo que me pareció más ventajoso para el aprovechamiento de memoria sólo expandir los vecinos del nodo que estamos explorando)
        current_node.get_neighbors(grid)
		
        for neighbor in current_node.neighbors:
            temp_g_score = g_score[current_node]+1
			__por cada vecino del nodo actual evaluará si se ha descubierto antes un camino más corto para llegar a este nodo__
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
				__en caso de que el camino actual sea el más corto, se indicará en el diccionario came_from y se actualizarán las matrices g(n) y f(n) con los valores actuales__
				__la función h(n) se explica debajo__
                if neighbor not in open_set_hash:
					__si el vecino expandido no se encuentra ya en el set de nodos a explorar, lo añadiremos__
                    count +=1
                    open_set.put((f_score[neighbor],count,neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        __ya que se exploró el nodo, se cierra__
        current_node.make_closed()
		
		Una vez descubierto el camino, la función make_path tomará cada nodo en el diccionario came_from y lo coloreará en verde
		
#Heurística propuesta
		
Dado que estamos en una grilla de NxN donde cada nodo almacena su posición de X e Y y las posiciones de X e Y de los nodos inicial y final son conocidas en todo momento,
es fácil asumir que la distancia mínima entre un punto N y el nodo final E es el resultado absoluto de x(N)- x(E) y de y(N)-y(E)
		
		def h(p1,p2):
		x1, y1 = p1
		x2, y2 = p2
		return abs(x1-x2) + abs(y1-y2)
		
Esta heurística se conoce como Distancia Manhattan o Geometría del Taxista, la cual es admisible y consistente.
		
En todos los casos, la distancia nunca será menor a esta relación entre los dos puntos. Sí puede ser mayor (en caso de que el camino óptimo esté bloqueado por un obstáculo) y
es consistente el costo de alcanzar el objetivo desde un nodo no es mayor al costo de expandirse a un nodo vecino y alcanzarlo desde allí. 


