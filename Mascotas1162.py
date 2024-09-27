print("Frida Abril Cisneros Hernandez")
#clase
class Mascota1162:
    def __init__(self):
        self.id_mascota1106= 0
        self.nombre1162= ""
        self.especies1162= ""
        self.edad1162= 0
        self.peso1162= 0.0
        self.id_cliente1162= 0
        self.historial1162= ""
    def datos1162(self):
        print(f"ID_mascota: {self.id_mascota1106}")
        print(f"Nombre de la mascota: {self.nombre1162}")
        print(f"Especies: {self.especies1162}")
        print(f"Edad: {self.edad1162}")
        print(f"Peso: {self.peso1162}")
        print(f"ID_cliente: {self.id_cliente1162}")
        print(f"Historial: {self.historial1162}")
    def lista_nombres1162(self):
        nombres=["Ayla","Pinto","Borrego","Pelusa","Canela","Coco","Lola"]
        print(nombres)
        for nom in nombres:
            print(nom)
    def tupla_edad1162(self):
        edades=("5 años","4 Años","3 Meses","7 meses","12 Años","9 Años")
        print(edades)
        for ed in edades:
            print(ed)
    def diccionarios_historial(self):
        historial={
            "Nombre: ": "Pelusa",
            "Especie: ": "Mamifero",
            "Padecimiento:": "chequeo",
        }
        print(historial)
        print("Lista de elementos")
        for his in historial:
            print(his)
    def Ingresado():
        print("Perito num.3 dado ingresado")
    def Alta():
        print("Perrito num.3 dado de alta")
        
#objetos
obj=Mascota1162()

#Asignar datos a atributos
obj.id_mascota1106=110201
obj.nombre1162= "Ayla"
obj.especies1162= "Mamifero"
obj.edad1162= 4
obj.peso1162= 12.1
obj.id_cliente1162=23455
obj.historial1162= "Ingreso el dia 9 de sep 2024"

#Mostrar datos
print("Datos")
obj.datos1162()
print("   ")
print("Lista de nombre")
obj.lista_nombres1162()
print("    ")
print("Tupla de edades")
obj.tupla_edad1162()
print("      ")
print ("Diccionario-historial")
obj.diccionarios_historial()
print("       ")
#llamar funciones
obj.Ingresado()
obj.Alta()







