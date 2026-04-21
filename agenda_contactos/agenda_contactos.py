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

    def buscar_contacto(self):
        nombre_buscar = input("Nombre a buscar: ")
        encontrado = False
        for c in self.contactos:
            if c['nombre'] == nombre_buscar:
                print(f"Resultado: {c['nombre']} -> {c['telefono']}")
                encontrado = True
                break
        if not encontrado:
            print("No se encontró ningún contacto con ese nombre.")

    def eliminar_contacto(self):
        nombre_eliminar = input("Nombre del contacto a borrar: ")
        original_count = len(self.contactos)
        self.contactos = [c for c in self.contactos if c['nombre'].lower() != nombre_eliminar.lower()]
       
        if len(self.contactos) < original_count:
            print(f"Contacto '{nombre_eliminar}' eliminado con éxito.")
        else:
            print("No se encontró el contacto.")


def ejecutar_menu():
    mi_agenda = Agenda()
    while True:
        print("\n1. Ver | 2. Añadir |3. Buscar | 4. Eliminar | 5. Salir ")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mi_agenda.ver_contactos()
        elif opcion == "2":
            mi_agenda.añadir_contacto()
        elif opcion == "3":
            mi_agenda.buscar_contacto()
        elif opcion == "4":
            mi_agenda.eliminar_contacto()
        elif opcion == "5":
            print("Cerrando agenda...")
            break
        else:
            print("Opción no válida.")

ejecutar_menu()