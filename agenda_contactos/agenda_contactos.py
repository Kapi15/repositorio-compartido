class Agenda:
    def __init__(self):
        self.contactos = [
            {"nombre": "Ana", "telefono": "123456789"},
            {"nombre": "Luis", "telefono": "987654321"}
        ]

    def ver_contactos(self):
        print("\n--- LISTA DE CONTACTOS ---")
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            for c in self.contactos:
                print(f"Nombre: {c['nombre']} | Teléfono: {c['telefono']}")

    def añadir_contacto(self):
        nombre = input("Introduce el nombre: ")
        telefono = input("Introduce el teléfono: ")
        self.contactos.append({"nombre": nombre, "telefono": telefono})
        print(f"¡Contacto {nombre} guardado!")

   

def ejecutar_menu():
    mi_agenda = Agenda()
    while True:
        print("\n1. Ver | 2. Añadir | ")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mi_agenda.ver_contactos()
        elif opcion == "2":
            mi_agenda.añadir_contacto()
        
        else:
            print("Opción no válida.")

ejecutar_menu()