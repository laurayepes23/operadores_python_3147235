# operadores en python
'''
    los operadores en python siguen el siguiente orden jerarquico
    1.             ( )
    2.             **
    3.            /,*,%,
    2.              +,-
    3.               =
    NOTA 1: Si hay operaciones en el mismo nivel de jerarquia se resulve de izquierda a derecha
    NOTA 2: Si hay parentesis dentro del parentesis se resuelve primero el parentisis interno 
'''
a = 3
b = 2
c = 1
x = 5

y = a ** 2 * 3 / (c - x)
print(y)