from data_stark import lista_personajes 
import os

def normalizar_datos(lista, key, key2, key3):
    flag = False
    for i in lista:
        if i[key] != float:
            i[key] = round(float(i[key]), 2)
            flag = True
        if i[key2] != float:
            i[key2] = round(float(i[key2]), 2)
            flag = True
        if i[key3] != float:
            i[key3] = round(float(i[key3]), 2)
            flag = True
        if lista == []:
            flag = False
    return flag, lista

def obtener_dato(dicc:dict, key:str):
    if dicc == {} or "nombre" not in dicc:
        return False
    else:
        return dicc[key]

def obtener_nombre(dicc):
    if dicc == {} or "nombre" not in dicc:
        return False
    else:
        strr = f"Nombre: {dicc['nombre']}"
        return strr

def obtener_dato_y_nombre(dicc, key):
    str1 = obtener_dato(dicc, key)
    str2 = obtener_nombre(dicc)
    str3 = f"{str2} | {key}: {str1}"
    if str1 == False or str2 == False:
        return False
    else:
        return str3

def obtener_maximo(lista:list, key:str):
    maximo = lista[0][key]
    nombre_max = lista[0]["nombre"]
    if lista != [] and key == float or int:
        for i in lista:
            if i[key] > maximo:
                maximo = i[key]
                nombre_max = i["nombre"]
        return nombre_max, maximo
    else:
        return False
    
def obtener_minimo(lista:list, key:str):
    minimo = lista[0][key]
    nombre_min = lista[0]["nombre"]
    if lista != [] and key == float or int:
        for i in lista:
            if i[key] < minimo:
                minimo = i[key]
                nombre_min = i["nombre"]
        return nombre_min, minimo
    else:
        return False

def obtener_dato_cantidad(lista:list, key:str, max=False, min=False, both=False):
    str1 = ""
    match(key):
        case "fuerza":
            if max:
                str1 = f"{key} maxima: {obtener_maximo(lista, key)[1]} puntos de fuerza, corresponde a {obtener_maximo(lista, key)[0]}"
            if min:
                str1 = f"{key} minima: {obtener_minimo(lista, key)[1]} puntos de fuerza, corresponde a {obtener_minimo(lista, key)[0]}"
            if both:
                str1 = f"{key} maxima: {obtener_maximo(lista, key)[1]} puntos de fuerza, corresponde a {obtener_maximo(lista, key)[0]}\n{key} minima: {obtener_minimo(lista, key)[1]} puntos de fuerza, corresponde a {obtener_minimo(lista, key)[0]}"
        case "altura":
            if max:
                str1 = f"{key} maxima: {obtener_maximo(lista, key)[1]}cm, corresponde a {obtener_maximo(lista, key)[0]}"
            if min:
                str1 = f"{key} minima: {obtener_minimo(lista, key)[1]}cm, corresponde a {obtener_minimo(lista, key)[0]}"
            if both:
                str1 = f"{key} maxima: {obtener_maximo(lista, key)[1]}cm, corresponde a {obtener_maximo(lista, key)[0]}\n{key} minima: {obtener_minimo(lista, key)[1]}cm, corresponde a {obtener_minimo(lista, key)[0]}"
        case "peso":
            if max:
                str1 = f"{key} maxima: {obtener_maximo(lista, key)[1]}kg, corresponde a {obtener_maximo(lista, key)[0]}"
            if min:
                str1 = f"{key} minima: {obtener_minimo(lista, key)[1]}kg, corresponde a {obtener_minimo(lista, key)[0]}"
            if both:
                str1 = f"{key} maxima: {obtener_maximo(lista, key)[1]}kg, corresponde a {obtener_maximo(lista, key)[0]}\n{key} minima: {obtener_minimo(lista, key)[1]}kg, corresponde a {obtener_minimo(lista, key)[0]}"
    return str1
def sumar_dato_heroe(lista, key):
    suma = 0
    for i in lista:
        if type(i) != dict:
            print(type(i))
            return False
        else:
            suma += i[key]
    return suma

def dividir(dividendo, divisor):
    if dividendo != 0 and divisor != 0:
        return dividendo / divisor
    else:
        return False

def calcular_promedio(lista, key):
    suma = sumar_dato_heroe(lista, key)
    promedio = dividir(suma, len(lista))
    promedio = (round(promedio, 2))
    return promedio

def mostrar_promedio_dato(lista, key):
    if lista == []:
        return False
    else:
        match(key):
            case "altura":
                str1 = f"El promedio de {key} es: {calcular_promedio(lista, key)}cm"
            case "peso":
                str1 = f"El promedio de {key} es: {calcular_promedio(lista, key)}kg"
            case "fuerza":
                str1 = f"El promedio de {key} es: {calcular_promedio(lista, key)} puntos de fuerza"
        return str1
def color_es(lista, key, contarlos=False, mostrarlos=False):
    string = ""
    lista_provisional = {}
    for i in lista:
        if i[key] not in lista_provisional:
            lista_provisional[i[key]] = []
        lista_provisional[i[key]].append(i["nombre"])
    if mostrarlos:
        for i in lista_provisional:
            match(key):
                case "color_ojos":
                    string += f"Pelo {i}: {', '.join(lista_provisional[i])}\n"
                case "color_pelo":
                    string += f"Ojos {i}: {', '.join(lista_provisional[i])}\n"
                case "inteligencia":
                    string += f"Inteligencia {i}: {', '.join(lista_provisional[i])}\n"
    if contarlos:
        for i in lista_provisional:
            lista_provisional[i] = len(lista_provisional[i])
            match(key):
                    case "color_ojos":
                        string += f"Ojos {i}: {lista_provisional[i]}\n"
                    case "color_pelo":
                        string += f"Pelo {i}: {lista_provisional[i]}\n"
                    case "inteligencia":
                        string += f"Inteligencia {i}: {lista_provisional[i]}\n"
    print(string, end="")

def imprimir_menu():
    print("1) Normalizar datos")
    print("2) Mostrar dato y nombre de heroe")
    print("3) Mostrar maximo o minimo de algun dato")
    print("4) Mostrar promedio de algun dato")
    print("5) Mostrar todos los heroes del mismo dato")
def limpiar_consola():
    os.system("cls") 
lista_personajes = normalizar_datos(lista_personajes, "altura", "peso", "fuerza")[1]
def stark_marvel_app():
    flag = True
    flag2 = False
    while flag or pregunta == "s":
        imprimir_menu()
        print("------------------------------------------------------------------")   
        eleccion = input("Elija una opcion: ")
        while True:
            try:
                eleccion = int(eleccion)
                break
            except Exception:
                print("Opcion incorrecta")
        match(eleccion):
            case 1:
                limpiar_consola() 
                print("Datos normalizados")
                flag2 = True
            case 2:
                if flag2:
                    numero = input("Elija un numero de heroe 1-25: ")
                    print("------------------------------------------------------------------")
                    while True:
                        try:
                            numero = int(numero) - 1
                            break
                        except Exception:
                            print("Opcion incorrecta")
                    if numero < 0 or numero > 24:
                        print("Opcion incorrecta")
                    else:
                        eleccion = input("Elija el dato a mostrar (nombre, identidad, empresa, altura, peso, genero, color_ojos, color_pelo, fuerza, inteligencia): ").lower()
                        while eleccion != "nombre" and eleccion != "identidad" and eleccion != "empresa" and eleccion != "altura" and eleccion != "peso" and eleccion != "genero" and eleccion != "color_ojos" and eleccion != "color_pelo" and eleccion != "fuerza" and eleccion != "inteligencia":
                            eleccion = input("Dato incorrecto, (nombre, identidad, empresa, altura, peso, genero, color_ojos, color_pelo, fuerza, inteligencia): ").lower()
                        print(obtener_dato_y_nombre(lista_personajes[numero], eleccion))
                else:
                    print("No hay datos normalizados")
            case 3:
                if flag2: 
                    llave = input("Elija el dato a mostrar (altura, peso, fuerza): ").lower()
                    while llave != "altura" and llave != "peso" and llave != "fuerza":
                        llave = input("Dato incorrecto, (altura, peso, fuerza): ").lower()
                    genero = input("Desea ver el genero masculino, femenino, NB(no balls), o todos?: ").lower()
                    while genero != "masculino" and genero != "femenino" and genero != "nb" and genero != "todos":
                        genero = input("Dato incorrecto, (masculino, femenino, nb, todos): ").lower()
                    if genero == "todos":
                        numero = input("Desea ver el maximo, el minimo, o ambos?: ").lower()
                        while numero != "maximo" and numero != "minimo" and numero != "ambos":
                            numero = input("Dato incorrecto, (maximo, minimo, ambos): ").lower()
                        print("------------------------------------------------------------------")
                        match(numero):
                            case "maximo":
                                print(obtener_dato_cantidad(lista_personajes, llave, max=True))
                            case "minimo":
                                print(obtener_dato_cantidad(lista_personajes, llave, min=True))
                            case "ambos":
                                print(obtener_dato_cantidad(lista_personajes, llave, both=True)) 
                    else: 
                        numero = input("Desea ver el maximo, el minimo, o ambos?: ").lower()
                        lista_provisional = []
                        if genero == "femenino":
                            genero = "F"
                        elif genero == "masculino":
                            genero = "M"
                        else:
                            genero = "NB"
                        for i in lista_personajes:
                            if i["genero"] == genero:
                                lista_provisional.append(i)
                        match(numero):
                            case "maximo":
                                str1 = obtener_dato_cantidad(lista_provisional, llave, max=True)
                            case "minimo":
                                str1 = obtener_dato_cantidad(lista_provisional, llave, min=True)
                            case "ambos":
                                str1 = obtener_dato_cantidad(lista_provisional, llave, both=True)
                        print(str1)     
                else:
                    print("No hay datos normalizados") 
            case 4:
                if flag2:
                    eleccion = input("Elija el dato promedio a mostrar (altura, peso, fuerza): ").lower()
                    while eleccion != "altura" and eleccion != "peso" and eleccion != "fuerza":
                        eleccion = input("Dato incorrecto, (altura, peso, fuerza): ").lower()
                    genero = input("Desea ver el genero masculino, femenino, NB(no balls), o todos?: ").lower()
                    while genero != "masculino" and genero != "femenino" and genero != "nb" and genero != "todos":
                        genero = input("Dato incorrecto, (masculino, femenino, nb, todos): ").lower()
                    print("------------------------------------------------------------------")
                    if genero == "todos":
                        match(eleccion):
                            case "altura":
                                print(mostrar_promedio_dato(lista_personajes, "altura"))
                            case "peso":
                                print(mostrar_promedio_dato(lista_personajes, "peso"))
                            case "fuerza":
                                print(mostrar_promedio_dato(lista_personajes, "fuerza"))  
                    else:
                        lista_provisional = []
                        if genero == "femenino":
                            genero = "F"
                        elif genero == "masculino":
                            genero = "M"
                        else:
                            genero = "NB"
                        for i in lista_personajes:
                            if i["genero"] == genero:
                                lista_provisional.append(i)
                        match(eleccion):
                                case "altura":
                                    str1 = mostrar_promedio_dato(lista_provisional, "altura")
                                case "peso":
                                    str1 = mostrar_promedio_dato(lista_provisional, "peso")
                                case "fuerza":
                                    str1 = mostrar_promedio_dato(lista_provisional, "fuerza")
                        print(str1)
                else:
                    print("No hay datos normalizados")  
            case 5:
                if flag2:
                    llave = input("Elija el dato a mostrar (color_ojos, color_pelo, inteligencia): ").lower()
                    while llave != "color_ojos" and llave != "color_pelo" and llave != "inteligencia":
                        llave = input("Dato incorrecto, (color_ojos, color_pelo, inteligencia): ").lower()
                    eleccion = input(f"Desea mostrar los heroes o ver la cantidad por {llave}(heroe, cantidad):").lower()
                    while eleccion != "heroe" and eleccion != "cantidad":
                        eleccion = input("Dato incorrecto, (heroe, cantidad): ").lower()
                    print("------------------------------------------------------------------")
                    match(eleccion):
                        case "cantidad":
                            color_es(lista_personajes, llave, contarlos=True)
                        case "heroe":
                            color_es(lista_personajes, llave, mostrarlos=True)
                else:
                    print("No hay datos normalizados")
        flag = False
        print("------------------------------------------------------------------")   
        pregunta = input("Desea seguir usando el programa? (s/n): ").lower()
        limpiar_consola()
        while pregunta != "s" and pregunta != "n":
            pregunta = input("Opcion incorrecta (s/n): ").lower()
stark_marvel_app()