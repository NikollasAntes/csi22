# vale ressaltar que no exemplo apresentado no enunciado da questao
# não se está calculando as médias das tuplas, mas sim a metade da soma
# a questão foi resolvida considerando-se a média das tuplas

from itertools import zip_longest

def media_tuplas(tuplas, valor_padrao = 0):
    resultado = []
    for grupo in zip_longest(*tuplas, fillvalue = valor_padrao):
        soma = sum(valor for valor in grupo if valor != valor_padrao)
        media = soma / len(grupo)
        resultado.append(media)
    return tuple(resultado)