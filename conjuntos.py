




def union_conj(conjuntoA, conjuntoB):
    conjuntoC = set()
    for i in conjuntoA:
        conjuntoC.add(i)
    for j in conjuntoB:
        if j not in conjuntoC:
            conjuntoC.add(j)
    return conjuntoC

def interseccion_conj(conjuntoA, conjuntoB):
    conjuntoC = set()
    for i in conjuntoA:
        for j in conjuntoB:
            if i == j:
                if i not in conjuntoC:
                    conjuntoC.add(i)
                
    return conjuntoC


def diferencia_conj(conjuntoA, conjuntoB):
    conjuntoC = set()
    for i in conjuntoA:
        if i not in conjuntoB:
            conjuntoC.add(i)
    return conjuntoC

def complemento_conj(conjuntoA, conjuntoB):
    conjuntoC = set()
    for i in conjuntoB:
        if i not in conjuntoA:
            if i not in conjuntoC:
                conjuntoC.add(i)

    return conjuntoC

def main():
    conjuntoA = {1, 2, 3, 4, 5}
    conjuntoB = {4, 5, 6, 7, 8}
    
    union = union_conj(conjuntoA, conjuntoB)
    print('union ---> ' + str(union))
    # conjuntoB = {1,4, 5, 6, 7, 8}
    interseccion = interseccion_conj(conjuntoA, conjuntoB)
    print('interseccion ---> ' + str(interseccion))
    complemento = complemento_conj(conjuntoA, conjuntoB)
    print('complemento ---> ' + str(complemento))

main()  # La llamada a la función main() se debe realizar fuera de la definición de la función.

    
    
    
    







                
                    






# def conjuntos():
#     # Conjuntos
#     # Un conjunto es una colección desordenada de elementos únicos.
#     # Se pueden usar para hacer pruebas de pertenencia, eliminación de entradas duplicadas y cálculos matemáticos como intersección, unión, diferencia y diferencia simétrica.

#     # Creación de un conjunto
#     conjunto = {1, 2, 3, 4, 5}
#     print(conjunto)

#     # Creación de un conjunto a partir de una lista
#     lista = [1, 2, 3, 4, 5]
#     conjunto = set(lista)
#     print(conjunto)

#     # Creación de un conjunto vacío
#     conjunto = set()
#     print(conjunto)

#     # Añadir elementos a un conjunto
#     conjunto = {1, 2, 3, 4, 5}
#     conjunto.add(6)
#     print(conjunto)

#     # Eliminar elementos de un conjunto
#     conjunto = {1, 2, 3, 4, 5}
#     conjunto.remove(3)
#     print(conjunto)

#     # Longitud de un conjunto
#     conjunto = {1, 2, 3, 4, 5}
#     print(len(conjunto))

#     # Comprobar si un elemento pertenece a un conjunto
#     conjunto = {1, 2, 3, 4, 5}
#     print(3 in conjunto)

#     # Comprobar si un elemento no pertenece a un conjunto
#     conjunto = {1, 2, 3, 4, 5}
#     print(3 not in conjunto)

#     # Unión de conjuntos
#     conjunto1 = {1, 2, 3, 4, 5}
#     conjunto2 = {4, 5, 6, 7, 8}
#     print(conjunto1 | conjunto2)

#     # Intersección de conjuntos
#     conjunto1 = {1, 2, 3, 4, 5}
#     conjunto2 = {4, 5, 6, 7, 8}
#     print(conjunto1 & conjunto2)

#     # Diferencia de conjuntos
#     conjunto1 = {1, 2, 3, 4, 5}
