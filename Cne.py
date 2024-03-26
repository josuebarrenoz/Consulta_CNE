import PyCNE

def run():
    Cedula = int(input("Escribe un numero de Cedula: "))
    consulta = PyCNE.consulta('V',Cedula)
    print(consulta)

if __name__=="__main__":
    run()

