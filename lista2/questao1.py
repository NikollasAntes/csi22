def remover_tuplas_vazias(lista_tuplas):
    return [tupla for tupla in lista_tuplas if any(tupla)]

#print(remover_tuplas_vazias([(2,4),(),(6,8,9),(7,),()]))
