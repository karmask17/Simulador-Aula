
import json

def cargar_perfil():
    return {
        "edad": "31-45",
        "experiencia": "1-3 años",
        "nivel_educativo": "secundaria",
        "materia": "historia",
        "numero_alumnos": 30,
        "estilo_ensenanza": "participativo"
    }

def cargar_escenarios():
    with open("escenarios.json", "r", encoding="utf-8") as f:
        return json.load(f)

def mostrar_escenario(escenario, perfil):
    descripcion = escenario["narrativa"].format(**perfil)
    print(f"\n📘 {escenario['titulo']}")
    print(descripcion)
    for clave, opcion in escenario["opciones"].items():
        print(f"{clave}. {opcion['texto']}")

def procesar_decision(escenario, eleccion):
    eleccion = eleccion.upper()
    if eleccion in escenario["opciones"]:
        resultado = escenario["opciones"][eleccion]
        print("\n🎯 Resultado:", resultado["consecuencia"])
        print("💡 Reflexión:", resultado["retroalimentacion"])
        return True
    else:
        print("Opción no válida. Intenta de nuevo.")
        return False

def iniciar_simulador():
    perfil = cargar_perfil()
    escenarios = cargar_escenarios()

    for escenario in escenarios:
        mostrar_escenario(escenario, perfil)
        valido = False
        while not valido:
            eleccion = input("\nElige tu respuesta (A/B/C): ")
            valido = procesar_decision(escenario, eleccion)

    print("\n✅ Has completado la etapa inicial del simulador. ¡Buen trabajo!")

if __name__ == "__main__":
    iniciar_simulador()
