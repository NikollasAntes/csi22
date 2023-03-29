# vale ressaltar que no exemplo apresentado no enunciado da questão não se
# está calculando as médias das tuplas, mas sim a metade da soma dos elementos
# a questão foi resolvida considerando-se a média da soma das tuplas
# caso fosse fazer a metade da soma, basta modificar a linha 11 do código
# por "media = soma/2"

def media_tuplas(tuplas):
    resultado = []
    for tupla in tuplas:
        soma = sum(tupla)
        media = soma/len(tupla)
        resultado.append(media)
    return tuple(resultado)

#print(media_tuplas(((2,3,4),(3,4,5,6),(2,4),(4,8,9))))
