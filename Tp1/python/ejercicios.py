def main():

     ###Ejercicio 1
    i = 0
    numeros = [1, 3, 5, 7, 9]

    while i < 1:

        num = int(input("Ingrese un numero del 0 al 9: "))
            
        if num < 0 or num > 9:
            print("Número fuera de rango. Intente nuevamente")
        else:
            i = 1

    if num in numeros:
        print(f"El número {num} está en la lista.")
    else:
        print(f"El número {num} no está en la lista.")
        
    
    #Ejercicio 2: Gestión de Conjuntos de Usuarios y Administradores

    usuarios = {"Marcela", "David", "Elvira", "Juan", "Marcos"}

    administradores = {"Juan", "Marcela"}

    administradores.discard("Juan")

    administradores.add("Marcos")

    print("Listado de usuarios:")
    for usuario in usuarios:
        if usuario in administradores:
            print(f"- {usuario}: Administrador")
        else:
            print(f"- {usuario}: Usuario común")

    
    # Ejercicio N3: Registro de Información en un Diccionario


    usuarios_info = {}

    while True:
        print("\n--- Registro de nuevo usuario ---")
        nombre = input("Ingrese el nombre: ")
        edad = input("Ingrese la edad: ")
        direccion = input("Ingrese la dirección: ")
        telefono = input("Ingrese el teléfono: ")

        usuario_info = {
            "Nombre": nombre,
            "Edad": edad,
            "Dirección": direccion,
            "Teléfono": telefono
        }

    
        usuarios_info[nombre] = usuario_info

        continuar = input("¿Desea agregar otro usuario? (si/no): ").lower()
        if continuar != "si":
            break


    print("\n=== Información de todos los usuarios ===")
    for nombre, info in usuarios_info.items():
        print(f"\nUsuario: {nombre}")
        for clave, valor in info.items():
            print(f"{clave}: {valor}")
   


    # Ejercicio N4: Gestión de Inventario de Instrumentos Musicales

    sucursales = [
        {
            "nombre": "Sucursal Centro",
            "instrumentos": [
                {"id": "P001", "precio": 15000, "tipo": "Percusión"},
                {"id": "C001", "precio": 20000, "tipo": "Cuerda"},
                {"id": "V001", "precio": 12000, "tipo": "Viento"},
            ]
        },
        {
            "nombre": "Sucursal Norte",
            "instrumentos": [
                {"id": "C002", "precio": 18000, "tipo": "Cuerda"},
                {"id": "V002", "precio": 16000, "tipo": "Viento"},
                {"id": "P002", "precio": 17000, "tipo": "Percusión"},
            ]
        }
    ]


    def listarInstrumentos():
        print("Lista de instrumentos por sucursal")
        for sucursal in sucursales:
            print(f"\nSucursal: {sucursal['nombre']}")
            for instrumento in sucursal["instrumentos"]:
                print(f"ID: {instrumento['id']}, Tipo: {instrumento['tipo']}, Precio: ${instrumento['precio']}")

    def instrumentosPorTipo(tipo):
        resultado = []
        for sucursal in sucursales:
            for instrumento in sucursal["instrumentos"]:
                if instrumento["tipo"].lower() == tipo.lower():
                    resultado.append(instrumento)
        return resultado


    def borrarInstrumento(id):
        for sucursal in sucursales:
            for instrumento in sucursal["instrumentos"]:
                if instrumento["id"] == id:
                    sucursal["instrumentos"].remove(instrumento)
                    print(f"Instrumento con ID '{id}' eliminado de {sucursal['nombre']}.")
                    return
        print(f"No se encontró ningún instrumento con ID '{id}'")


    def porcInstrumentosPorTipo(nombre_sucursal):
        for sucursal in sucursales:
            if sucursal["nombre"].lower() == nombre_sucursal.lower():
                instrumentos = sucursal["instrumentos"]
                total = len(instrumentos)
                if total == 0:
                    return {"Percusión": 0, "Viento": 0, "Cuerda": 0}

                conteo = {"Percusión": 0, "Viento": 0, "Cuerda": 0}
                for inst in instrumentos:
                    tipo = inst["tipo"]
                    conteo[tipo] += 1

                porcentajes = {tipo: (cantidad / total) * 100 for tipo, cantidad in conteo.items()}
                return porcentajes
        print("Sucursal no encontrada.")
        return None




 

main()