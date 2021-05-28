### Colecciones en Python

- **Listas/Lists**

  - Son de proposito general
  - Es la estructura mas utiliazada
  - Tamano dinamico
  - De tipo secuencial
  - Ordenable
  - _Implementacion:_

    ```python
    lista1 = list()
    lista2 = [1, 2, 'hola']
    list3 = [i**2 for i in range(5)]

    print(lista1) # []
    print(lista2) # [1, 2, 'hola']
    print(lista3) # [0, 1, 4, 9, 16]
    ```

- **Tuplas**

  - Inmutable (No se puede agregar o cambiar elemento)
  - Son de utiliada para almacenar datos constantes
  - Son mas rapidas que las listas
  - Tipo secuencial
  - _Implementacion:_

    ```python
    tupla1 = ()
    tupla2 = (123, 234, 456)
    tupla3 = 'pegaso', 'fenix', 'cisne',

    print(tupla1) # ()
    print(tupla2) # (123, 234, 456)
    print(tupla3) # ('pegaso', 'fenix', 'cisne')
    ```

- **Conjuntos/Sets**

  - Almacenan objetos no duplicados
  - De acceso rapido
  - Aceptan operaciones logicas
  - Son desordenados
  - _Implementacion:_

    ```python
    conjunto1 = {1, 2, 3, 4}
    conjunto2 = set()
    numeros = [1, 2, 3, 4, 5, 6, 7, 2, 3]
    conjunto3 = set(numeros)

    print(conjunto1) # {1, 2, 3, 4}
    print(conjunto2) # set()
    print(conjunto3) # {1, 2, 3, 4, 5, 6, 7}
    ```

- **Diccionarios/Dictionaries**

  - Pares de llave/valor
  - Arrays asociativos (hash maps)
  - Son desordenados
  - _Implementacion:_

    ```python
    gatos1 = {
        'mulan' : 2,
        'pucca'  : 2.3,
        'percy' : 4,
    }

    gatos2 = dict([('mulan', 2), ('pucca', 2.3), ('percy', 4)])
    gatos3 = dict(mulan = 2, pucca = 2.3, percy = 4)

    print(gatos1) # {'mulan' : 2, 'pucca' : 2.3, 'percy' : 4}
    print(gatos2) # {'mulan' : 2, 'pucca' : 2.3, 'percy' : 4}
    print(gatos3) # {'mulan' : 2, 'pucca' : 2.3, 'percy' : 4}
    ```
