### Diccionarios

Son estrucuras de datos que almacenan su contenido en forma de `llave : valor`

- **Propiedades**

  - _Dinamicos_: pueden crecer y decrecer, se pueden anadir y eliminar elementos.
  - _Indexados_: sus elementos son accesibles a traves de su `llave o key`
  - _Anidados_: un diccionario puede contener otro diccionario en su campo `value`.

- **Creacion de diccionario**

  - Creacion con `{}` y seperando cada par `key : value` con `,`

    ```python
    diccionario = {
        'key_1' : 1,
        'key_2': 2,
        'key_3' : 3
    }

    print (diccionario) # {'key_1' = 1, 'key_2' = 2, 'key_3' = 3}
    ```

  - Creacion con `dict()` e introduciendo los pares `key : value` entre `()`

    ```python
    diccionario = dict([
        ('key_1' : "Jorge"),
        ('key_2' : "Luis"),
        ('key_3' : "Felix")
    ])

    print(diccionario) # {'key_1' : 'Jorge', 'key_2':'Luis', 'key_3':'Felix'}
    ```

  - Usando constructor `dict()`

    ```python
    diccionario = dict('key_1' = "Alfonso", 'key_2' = "Luis", 'key_3' = "Manuel" )

    print(diccionario) # {'key_1' : 'Alfonso', 'key_2' : 'Luis', 'key_3' : 'Manuel' }
    ```

- **Acceso y modificacion de elementos**

  - Acceso con `[]` o la funcion `get()`

    ```python
    diccionario = {'nombre' : 'Rosa', 'apellido': 'Santiago'}

    print(diccionario['nombre']) # 'Rosa'
    print(diccionario.get('apellido')) # Santiago
    ```

  - Modicar elementos

    ```python
    d1 = {'nombre' : 'Juan', 'apeliido':'Morales'}
    d1['nombre'] = 'Oscar'

    print(d1) # {'nombre' : 'Oscar', 'apellido' : 'Morales'}

    d1['apellido_2'] = 'Lopez' # Si el key  no existe, se agrega jusnto con el nuevo value
    print(d1) # {'nombre' : 'Oscar', 'apellido' : 'Morales', 'apellido_2' : 'Lopez'}
    ```

- **Iteracion sobre diccionario**

  - Iterando sobre keys

    ```python
    d1 = {'k_1' : 'a', 'k_2' : 'b', 'k_3' : 'c'}

    for k in d1:
      print (k)
    # Salida
    # k_1
    # k_2
    # k_3
    ```

  - Iterando sobre values

    ```python
    d1 = {'k_1' : 'a', 'k_2' : 'b', 'k_3' : 'c'}

    for v in d1:
      print(d1[v])

    # Salida
    # a
    # b
    # c
    ```

  - Iteracion sobre keys y values al mismo tiempo

    ```python
    d1 = {'k_1' : 'a', 'k_2' : 'b', 'k_3' : 'c'}

    for k,v in d1.items():
      print(k,v)

    # Salida
    # k_1 a
    # k_2 b
    # k_3 c
    ```

- **Metodos de diccionarios**

  - `clear()`
    Elimina todo el contenido del diccionario

    ```python
    d1 = {'1' : 'uno', '2' : 'dos'}

    d1.clear()
    print(d1) # {}
    ```

  - `get(<key>[,default])`
    Permite obtener el value de un key que se pasa como parametro, en segundo parametro permite mostrar un valor por defecto si el key no es hallado

    ```python
    d1 = {'uno' : 1, 'dos' : 2}

    print(d1.get('uno')) # 1
    print(d1.get('tres','Llave inexistente')) # Llave inexistente
    ```

  - `items()`
    Obtiene los `keys` y `values` del diccionario, si se convierte a lista se puede indexar como una lista normal

    ```python
    d1 = {'uno' : 1, 'dos' : 2}
    elementos = d1.items()
    print(lista) #  dict_items([('uno', 1), ('dos', 2)])
    lista = list(elementos)
    print(lista[0][1]) # 1
    ```

  - `keys()`
    Devuelve los keys del diccionario

    ```python
    d1 = {'uno' : 1, 'dos' : 2}
    k = d1.keys()
    print(k) # dict_keys(['uno','dos'])
    lista = list(k)
    print(lista) # ['uno','dos']
    ```

  - `values()`
    Devuelve los values del diccionario

    ```python
    d1 = {'uno' : 1, 'dos' : 2}
    v = d1.values()
    print(v) # dict_values([1, 2])
    lista = list(v)
    print(lista) # [1, 2]
    ```

  - `popitem()`
    Elimina elemento del diccionario de manera aleatoria

    ```python
    d1 = {'uno' : 1, 'dos' : 2}
    d1.popitem()

    print(d1) # {'uno' : 1}
    ```

  - `update()`
    Actualiza un diccionario con los valores de otro, si una key no existe en el diccionario a actualizar, esta se agrega

    ```python
    d1 = {'uno' : 1, 'dos' : 2}
    d2 = {'dos' : 3, 'cinco' : 6}
    d1.update(d2)

    print(d1) # {'uno' : 1, 'dos': 3 , 'cinco': 6}
    ```
