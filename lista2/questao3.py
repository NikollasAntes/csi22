def processar_lista(strings):
    nova_lista = []
    for string in strings:
        if any(char.isalnum() for char in string):
            nova_lista.append(string)
    return nova_lista

print(processar_lista(["nikollas123", "nikollas.123", "123", "nikollas", "*&¨%", "#$%1"]))
