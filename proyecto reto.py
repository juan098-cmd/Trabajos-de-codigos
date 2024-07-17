def configurar_dificultad(configuraciones):
    dificultades = ["Fácil", "Medio", "Difícil"]
    eleccion = input("Seleccione la dificultad del juego (1: Fácil, 2: Medio, 3: Difícil): ")
    if eleccion in ['1', '2', '3']:
        configuraciones['dificultad'] = dificultades[int(eleccion) - 1]
    else:
        print("Selección no válida.")

def alternar_trampas(configuraciones):
    configuraciones['trampas_activadas'] = not configuraciones['trampas_activadas']
    print(f"Trampas {'activadas' if configuraciones['trampas_activadas'] else 'desactivadas'}.")

def seleccionar_personajes(configuraciones, personajes_disponibles):
    print("Seleccione personajes para su equipo:")
    for i, personaje in enumerate(personajes_disponibles):
        print(f"{i + 1}. {personaje['nombre']} - Habilidades: {', '.join(personaje['habilidades_especiales'])}")
    elecciones = input("Ingrese los números de los personajes separados por comas (ej. 1,3): ").split(',')
    configuraciones['equipo'] = [personajes_disponibles[int(eleccion) - 1] for eleccion in elecciones if eleccion.isdigit() and 1 <= int(eleccion) <= len(personajes_disponibles)]
    print("Personajes seleccionados:", ", ".join([personaje['nombre'] for personaje in configuraciones['equipo']]))

def modificar_habilidades(configuraciones):
    if not configuraciones['equipo']:
        print("Primero seleccione personajes para su equipo.")
        return
    print("Seleccione el personaje al que desea modificar sus habilidades:")
    for i, personaje in enumerate(configuraciones['equipo']):
        print(f"{i + 1}. {personaje['nombre']}")
    eleccion = input("Ingrese el número de su elección: ")
    if eleccion.isdigit() and 1 <= int(eleccion) <= len(configuraciones['equipo']):
        personaje_seleccionado = configuraciones['equipo'][int(eleccion) - 1]
        nuevas_habilidades = input(f"Ingrese las nuevas habilidades para {personaje_seleccionado['nombre']} separadas por comas: ").split(',')
        personaje_seleccionado['habilidades_especiales'] = [habilidad.strip() for habilidad in nuevas_habilidades]
        print(f"Nuevas habilidades de {personaje_seleccionado['nombre']}: {', '.join(personaje_seleccionado['habilidades_especiales'])}")
    else:
        print("Selección no válida.")

def modificar_ventajas_desventajas(configuraciones):
    if not configuraciones['equipo']:
        print("Primero seleccione personajes para su equipo.")
        return
    print("Seleccione el personaje al que desea modificar sus ventajas y desventajas:")
    for i, personaje in enumerate(configuraciones['equipo']):
        print(f"{i + 1}. {personaje['nombre']}")
    eleccion = input("Ingrese el número de su elección: ")
    if eleccion.isdigit() and 1 <= int(eleccion) <= len(configuraciones['equipo']):
        personaje_seleccionado = configuraciones['equipo'][int(eleccion) - 1]
        ventajas = input(f"Ingrese las ventajas para {personaje_seleccionado['nombre']} separadas por comas: ").split(',')
        desventajas = input(f"Ingrese las desventajas para {personaje_seleccionado['nombre']} separadas por comas: ").split(',')
        personaje_seleccionado['ventajas'] = [ventaja.strip() for ventaja in ventajas]
        personaje_seleccionado['desventajas'] = [desventaja.strip() for desventaja in desventajas]
        print(f"Ventajas de {personaje_seleccionado['nombre']}: {', '.join(personaje_seleccionado['ventajas'])}")
        print(f"Desventajas de {personaje_seleccionado['nombre']}: {', '.join(personaje_seleccionado['desventajas'])}")
    else:
        print("Selección no válida.")

def mostrar_configuraciones(configuraciones):
    print("\nConfiguraciones seleccionadas:")
    print(f"Dificultad: {configuraciones['dificultad']}")
    print(f"Trampas activadas: {'Sí' if configuraciones['trampas_activadas'] else 'No'}")
    print("Equipo seleccionado:")
    for personaje in configuraciones['equipo']:
        print(f" - {personaje['nombre']} (Habilidades: {', '.join(personaje['habilidades_especiales'])})")
        if 'ventajas' in personaje:
            print(f"   Ventajas: {', '.join(personaje['ventajas'])}")
        if 'desventajas' in personaje:
            print(f"   Desventajas: {', '.join(personaje['desventajas'])}")
    print()

def main():
    personajes = [
        {"nombre": "ernesto santisteban", "habilidades_especiales": ["Fuerza", "Defensa"]},
        {"nombre": "sebastian cordero", "habilidades_especiales": ["Magia", "Sabiduría"]},
        {"nombre": "christine", "habilidades_especiales": ["Precisión", "Agilidad"]},
        {"nombre": "santiago", "habilidades_especiales": ["Fuerza", "Defensa"]},
        {"nombre": "prometeo deportado", "habilidades_especiales": ["Magia", "Sabiduría"]},
        {"nombre": "juana estrella", "habilidades_especiales": ["Precisión", "Agilidad"]},
        {"nombre": "fernando coellar", "habilidades_especiales": ["Fuerza", "Defensa"]},
        {"nombre": "picchu", "habilidades_especiales": ["Magia", "Sabiduría"]},

    ]

    configuraciones = {
        "dificultad": "Medio",
        "trampas_activadas": False,
        "equipo": []
    }

    while True:
        print("\nMenú Principal:")
        print("1. Seleccionar personajes")
        print("2. Modificar habilidades de personajes")
        print("3. Configurar dificultad")
        print("4. Activar/Desactivar trampas")
        print("5. Modificar ventajas y desventajas de personajes")
        print("6. Mostrar configuraciones")
        print("7. Salir")

        eleccion = input("Ingrese el número de su elección: ")

        if eleccion == '1':
            seleccionar_personajes(configuraciones, personajes)
        elif eleccion == '2':
            modificar_habilidades(configuraciones)
        elif eleccion == '3':
            configurar_dificultad(configuraciones)
        elif eleccion == '4':
            alternar_trampas(configuraciones)
        elif eleccion == '5':
            modificar_ventajas_desventajas(configuraciones)
        elif eleccion == '6':
            mostrar_configuraciones(configuraciones)
        elif eleccion == '7':
            print("Saliendo del juego...")
            break
        else:
            print("Selección no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
