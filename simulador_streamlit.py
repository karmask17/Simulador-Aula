
import streamlit as st
import json

st.set_page_config(page_title="Simulador Docente", page_icon="🧑‍🏫", layout="centered")

# Cargar perfil del usuario (fijo por ahora, luego se puede hacer editable)
perfil = {
    "edad": "31-45",
    "experiencia": "1-3 años",
    "nivel_educativo": "secundaria",
    "materia": "historia",
    "numero_alumnos": 30,
    "estilo_ensenanza": "participativo"
}

# Cargar escenarios
@st.cache_data
def cargar_escenarios():
    with open("escenarios.json", "r", encoding="utf-8") as f:
        return json.load(f)

escenarios = cargar_escenarios()

# Estado de sesión
if "indice" not in st.session_state:
    st.session_state.indice = 0
if "completado" not in st.session_state:
    st.session_state.completado = False
if "historial" not in st.session_state:
    st.session_state.historial = []

# Mostrar escenario actual
if st.session_state.indice < len(escenarios):
    escenario = escenarios[st.session_state.indice]
    st.title(f"Escenario {escenario['id']}: {escenario['titulo']}")
    st.markdown(escenario["narrativa"].format(**perfil))

    st.markdown("""---""")
    opcion = st.radio("¿Qué eliges?", list(escenario["opciones"].keys()), format_func=lambda x: f"{x}. {escenario['opciones'][x]['texto']}")

    if st.button("Confirmar elección"):
        resultado = escenario["opciones"][opcion]
        st.session_state.historial.append({
            "escenario": escenario["titulo"],
            "opcion": opcion,
            "resultado": resultado
        })
        st.success(f"🎯 Resultado: {resultado['consecuencia']}")
        st.info(f"💡 Reflexión: {resultado['retroalimentacion']}")
        st.session_state.indice += 1

        if st.session_state.indice >= len(escenarios):
            st.session_state.completado = True
            st.experimental_rerun()

else:
    st.title("✅ ¡Has completado la etapa inicial del simulador!")
    st.markdown("### Resumen de tus decisiones:")
    for i, item in enumerate(st.session_state.historial, 1):
        st.markdown(f"""**{i}. {item['escenario']}**  
        Elegiste: **{item['opcion']}**  
        Resultado: *{item['resultado']['consecuencia']}*  
        Reflexión: _{item['resultado']['retroalimentacion']}_""")

    st.button("Reiniciar", on_click=lambda: st.session_state.clear())
