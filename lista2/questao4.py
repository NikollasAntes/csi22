def verificar_caracteres(string1, string2):
    for char in string1:
        if char not in string2:
            return False
    return True

#print(verificar_caracteres("nikollas", "nikolas"))
#print(verificar_caracteres("nikolla", "nikolas"))
#print(verificar_caracteres("nikollas", "nikola"))
