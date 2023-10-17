from data_stark import lista_personajes

lista_provisional = {}
lista = []
contador = 0
for i in lista_personajes:
    if i["color_ojos"] not in lista_provisional:
        lista_provisional[i["color_ojos"]] = []
    lista_provisional[i["color_ojos"]].append(i["nombre"])
for i in lista_provisional:
    print(f"{i} eyes: {', '.join(lista_provisional[i])}")

