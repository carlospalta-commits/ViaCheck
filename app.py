
import streamlit as st

st.set_page_config(page_title="ViaCheck", page_icon="🛣️")

st.title("🛣️ ViaCheck")
st.subheader("Inspector vial básico")

st.write("Registra una observación sobre el estado de una vía.")

ubicacion = st.text_input("Ubicación o abscisa de la vía")

tipo = st.selectbox(
    "Tipo de deterioro",
    ["Bache", "Fisura", "Hundimiento", "Problema de drenaje"]
)

severidad = st.selectbox(
    "Severidad observada",
    ["Baja", "Media", "Alta"]
)

if st.button("Evaluar deterioro"):
    if not ubicacion.strip():
        st.warning("Escribe la ubicación de la vía.")
    else:
        st.success("Registro de inspección generado")
        st.write("Ubicación:", ubicacion)
        st.write("Deterioro:", tipo)
        st.write("Severidad:", severidad)

        if severidad == "Baja":
            st.info("Recomendación: programar seguimiento.")
        elif severidad == "Media":
            st.warning("Recomendación: realizar una inspección técnica.")
        else:
            st.error(
                "Recomendación: priorizar la inspección técnica "
                "y evaluar medidas preventivas de seguridad."
            )

st.caption(
    "Herramienta educativa. No sustituye el diagnóstico de un ingeniero."
)
