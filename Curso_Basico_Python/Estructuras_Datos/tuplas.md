### Tuplas

Las tuplas son estructuras para el almacenamiento de datos, estas son inmutables por cual sus elementos no pueden ser modificados una vez declarada.

---

###### Operaciones

- Error en reasignacion de valores.

  ```python
  mi_tupla = (1, 2, 3)
  mi_tupla[0] = 0 # Error! TypeError
  ```

- Anidacion de tuplas.

  ```python
  mi_tupla = (1, 2, 3, ('a','b'), 4, 5)
  print(mi_tupla[3][1]) # 'b'
  ```

- Coversion de lista a tupla con la funcion `tuple()`.

  ```python
  lista = [1, 2, 3, 4]
  mi_tupla = tuple(lista)
  print(type(mi_tupla)) # <class 'tuple'>
  print(mi_tupla) # (1,2,3,4)
  ```

- Iteracion sobre tupla

  ```python
  mi_tupla =  (1, 2, 3)

  for elemento in mi_tupla:
      print(elemento)
  # 1
  # 2
  # 3
  ```

- Asignacion de valores de n elementos a n variables.

  ```python
  mi_tupla = (1, 2, 3)
  x, y, z = mi_tupla
  print(x, y, z) # 1, 2, 3
  ```

- Creacion de tupla de un solo elemento.

  ```python
  mi_tupla = (1,) # La coma es obligatoria, de lo contrario se toma como un int
  print(type(mi_tupla)) # <class 'tuple'>
  ```

---

###### Metodos

- Metodo ` count(<obj>)`

  El metodo count cuenta el numero de veces que el objeto que se pasa como parametro se encuentra en la tupla.

  ```python
  mi_tupla = (1, 1, 2, 3, 4)
  print(mi_tupla.count(1)) # 2
  ```

- Metodo `index(<obj>[,index])`

  Devuelve el indice el que se encuentra el objeto que se pasa como parametro.

  ```python
  mi_tupla = (1, 2, 3, 4)
  print(mi_tupla.index(2)) # 1
  ```

  Si objeto que se pasa como parametro no se encuentra en la lista, devuelve `ValueError`.

  ```python
  mi_tupla = (1, 2, 3, 4)
  print(mi_tupla.index(24)) # Error! ValueError
  ```

  Opcionalmente se le puede pasar un segundo parametro para indicarle en que indice debe empezar a buscar.

  ```python
  mi_tupla = (1, 2, 2, 3, 4)
  print(mi_tupla.index(2,1)) # 1
  ```
