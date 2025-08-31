import PyCNE
import time

def formato(lines):

    #Limpiar los saltos de Lineas
    lines = [line.replace("\n", "") for line in lines];

    #Filtrar Datos: Eliminando lo que no es numero
    lines = [element for element in lines if element.isdigit()];

    #Creando elementos validos para la libreria PyCNE
    #Convertir los elementos en int para separarlos en 80000000
    lines = [int(element) for element in lines];

    #Separar Venezolanos de Extranjeros
    lines_venezolanos = [element for element in lines if element <= 80000000];
    lines_extranjeros = [element for element in lines if element >= 80000000];

    #Convertir los eleementos  en str para agregar simbolos
    lines_venezolanos = [str(element) for element in lines_venezolanos];
    lines_extranjeros = [str(element) for element in lines_extranjeros];

    #Agregando los simbolo "V-" y "E-"
    lines_venezolanos = ["V-" + element for element in lines_venezolanos];
    lines_extranjeros = ["E-" + element for element in lines_extranjeros];

    #Unir a lines_venezolano y lines_extranjeros en lines
    lines = lines_venezolanos + lines_extranjeros;

    return lines

def run():
    # Captura de eleemtos del archivo separados de comas para leerlo
    ruta = str(input("Escribe el nombre del archivo con su extension: "))
    with open(ruta, 'r', encoding="utf8") as f:
        lines = f.readlines()

    #Aplicando Formato para la libreria
    Cedulas = formato(lines);

    #Generando la consulta
    tiempo_inicio = time.time()
    consulta = PyCNE.consulta.multi(Cedulas)

    # Ordenando la data
    lines = [[element['cedula'], element['nombre']] for element in consulta.info]
    tiempo_final = time.time()

    #Testeando programa
    #print(lines)

    #Midiendo el tiempo de ejecucion
    tiempo_ejecucion = tiempo_final - tiempo_inicio
    print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")

    #Probando la Libreria
    #Cedula = int(input("Escribe un numero de Cedula: "))
    #consulta = PyCNE.consulta('V',Cedula)
    #print(consulta.nombre)

    #Escribiendo los resultados
    with open(r'Resultados.txt', 'w', encoding="utf8") as f:
        f.writelines(lines)

if __name__=="__main__":
    run()

