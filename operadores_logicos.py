'''  
OPERADORES LOGICOS
Los operadores logicos son :
 and, or, not
 obedecen las tablas de verdad


'''

op1 = False
op2 = True
op3 = op1 and op2
print(op3)


op4 = True
op5 = False
op6 = op4 and op5
print(op6)


#operador not

op7 = not op2
print(op7)

'''
JERARQUIA DEFINITIVA DE OPERADORES
1.          ()
2.          **
3          /,*,%,
4.          +,-
5.       >,<,>=,<=,!=,==     
6.            NOT
7.            AND
8.             OR
9.              =
Nota: si hay operacones en el mismo nivel de jerarquia se resuelve de izquierda a derecha 
'''


op1 = False
op2 = True
op3 = False
op4 = True

resultado = not op1 and op2 or op3 and not op4
