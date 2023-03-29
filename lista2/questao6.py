def reverter_lista(lista):
    i = len(lista) - 1
    while i >= 0:
        yield lista[i]
        i -= 1

lista = [4,7,8]
gen = reverter_lista(lista)
for i in range(len(lista)):
    print(next(gen))
