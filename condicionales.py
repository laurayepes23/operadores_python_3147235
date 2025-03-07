'''
CONDICIONALES
expresion que al ser evaluada da como resultado un valor verdadero falso 
en un a condicional debe haber un poerador relacionales o logicos 
'''

#EJEMPLO DE CONDICIONAL 
a = 3
b = 2
c = 1
d = 4
resultado = (a ** 2 -b > c ** 2) and (( a * 3  + c ) /2 < d) or True
print(resultado)


#EJEMPLO
x = 5
y = 10
z = 5

resultado = (x == z + ( 8 / z ) ) and not ((y + 3) * ( 4 / ( z + 1 ))) == z
print(resultado)


#EJEMPLO
a = 6
b = 3
c = 7
d = 4
d = 5

resultado = not (a + b > c / d ) or e * 2 != d + c and not (a < b)
print(resultado)