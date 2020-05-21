## Transformando lista en diccionario 4 con Python

Define la función `nested_list_to_dict` que recibe una lista nesteada como argumento y retorna una lista `list` con diccionario `dict`. 

Es importante desarrollar tu código usando `unittest` para verificar que tu programa se comporta y produce el resultado deseado.

Restricción: Para este ejercicio usa `list comprehensions`, siguiendo las buenas prácticas al estilo pythonista.


```python
"""nested_list_to_dict function"""

...

```

Un ejemplo de argumento recibido sería el siguiente:

```python
[
    [
        ['firstName', 'Oscar'], ['lastName', 'Majik'], ['age', 56], ['country', 'Mexico']
    ]
]
```
Y se retornaría una lista con un diccionario `dict`:

```python
[
    {firstName: 'Oscar', lastName: 'Majik', age: 56, country: 'Mexico'}
]
```

```
# unittest - TDD

$ python test_nested_list_to_dict.py
```
