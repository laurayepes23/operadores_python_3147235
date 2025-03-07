# operadores en python
'''
    los operadores en python siguen el siguiente orden jerarquico
    1.             ( )
    2.             **
    3.            /,*,%,
    4.              +,-
    5.               =
    NOTA 1: Si hay operaciones en el mismo nivel de jerarquia se resulve de izquierda a derecha
    NOTA 2: Si hay parentesis dentro del parentesis se resuelve primero el parentisis interno 
'''
a = 2
b = 3
c = 7
x = 5
h = 1

y = c / ( x + 2 ) < c * a - c + 1 - b * 2
print(y)

'''
OPERACIONES RELACIONALES:
las operaciones aritmeticas resultan en un valor numerico
las operaciones relacionales resultan en un valor booleano: true, dfalso (V, F SI NO)
OPERACIONES RELACIONALES:
>,<,>=,<=,!=,==
JERARQUIA DE OPERADORES INCLUYENDO LOS RELACIONALES:
1.          ()
2.          **
3          /,*,%,
4.          +,-
5.       >,<,>=,<=,!=,==     
6.            =
'''

a = 3
b = 2
c = 1

y = a