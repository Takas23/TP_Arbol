# TP - Arbol binario


este proyecto contiene la implementación de un programa que permite manipular un árbol de búsqueda, compuesto por interpretes y sus canciones.<br>

para esto fueron implementadas las siguientes estructuras:

- **Lista():** una lista simple enlazada, con sus funciones básicas y sus nodos.
  
- **ArbolDeCanciones():** un árbol binario con sus funciones y sus nodos que contienen Lista()
  
También fueron incluidas dos funcionalidades extras.

- **quickSort():** recibe una lista y la ordena de menor a mayor, utilizando el concepto del ordenado rápido<br>
  
- **binarySearch():** recibe una lista ordenada, un elemento, una posición de inicio y una posición de fin entre los que se realiza la búsqueda. retorna la posición del elemento.<br>


Las funciones del árbol son:

- **insertarCanciones():** recibe por parámetro una lista de canciones y un interprete. <br>
Primero busca el interprete en el árbol, si ya esta ingresado le carga la lista de canciones, de lo contrario se inserta el interprete y luego sus canciones.

- **interpretesDeCancion():** recibe un nombre de canción y retorna una lista de todos los interpretes que tengan una canción con ese nombre.<br>
Se crea una lista de interpretes vacía, si el árbol no esta vacío se llama a la función recursiva en la raíz, si la raíz contiene la canción buscada se agrega el interprete a la lista, y se vuelve a repetir con sus hijos si es que tiene.

- **buscarCanciones():** recibe una lista de interpretes y devuelve una lista con las canciones que tienen en común. <br>
primero se crea una lista de canciones en común que contiene la lista de canciones completa del primer interprete de la lista recibida.<br>
Luego, busca en la lista de canciones del segundo artista los recibidos, las canciones de la lista de canciones creada y va eliminando de esta ultima, las que no estén en ambas listas.<br>
cuando llega a la ultima canción se repite con el siguiente interprete.

- **eliminarInterprete():** recibe un nombre de interprete y lo elimina del árbol.<br>
primero se ubica el nodo a eliminar, luego encuentra su predecesor, siendo este el mayor entre los menores del nodo a eliminar. una vez obtenido el predecesor lo coloca en lugar del nodo a eliminar, asignándole los enlaces correspondientes.

- **eliminarCancion():** recibe una canción y la elimina de todos los interpretes del árbol.<br>
si el árbol no esta vacío llama a la función recursiva desde la raíz. utilizando la función de lista **contiene()** busca en cada interprete  la canción y si la contiene la elimina usando indices.<br>

- **altura():** calcula la altura total del árbol, para eso utiliza una función recursiva de Nodo, esta calcula la altura de un nodo sumando 1 en una variable por cada nivel hacia abajo

- **cancionesEnNivel():** recibe un nivel por parametro y devuelve una lista con las canciones de todos los interpretes en ese nivel del árbol.<br>
Se inicia con un contador en 0 y una lista vacía. Baja niveles sumando en 1 hasta que se iguala el contador y el nivel, y agrega las canciones de todos los interpretes en ese nivel a la lista creada.

- **cantidadTotalInterpretes():** recibe una palabra y devuelve la cantidad de interpretes cuyo nombre contiene la palabra.
utilizando la función recursiva en nodo se llama en la raíz y se verifica si el nombre contiene la palabra, sumando 1 si es verdadero. y se repite en sus hijos sucesivamente.

- **raizBalanceada():** utilizando la función  de Nodo altura(), se calcula la altura del subarbol izquierdo y derecho de la raíz. luego retorna True si la diferencia entre las alturas es menor o igual a 1.

- **interpretesConMasCanciones():** recibe una cantidad de canciones mínima y devuelve la cantidad de interpretes que tienen como mínimo, esa cantidad de canciones.
utilizando un contador y la función recursiva en Nodo, desde la raíz se verifica el tamaño de su lista de canciones y si es mayor al mínimo recibido, se suma 1 al contador, recursivamente se suma con el resultado de la función ejecutada desde sus hijos.

- **internosAlfabetico():** devuelve una lista de interpretes en orden alfabético que no sean hojas del árbol.
utilizando una lista se van agregando los interpretes que tengan grado mayor a 0( al menos 1 hijo) y al final se hace un quicksort() para ordenarla
 
