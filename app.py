import streamlit as st

# Opciones de nombres de routers
router_options = ["Router_Actual1", "Router_Actual2", "Router_Actual3"]
new_router_options = ["Nuevo_Router1", "Nuevo_Router2", "Nuevo_Router3"]

# Contenedor para secciones en una fila
col1, col2, col3 = st.columns([1, 0.1, 1])

with col1:
    st.header("Datos del Router Actual")
    router_actual = st.selectbox("Nombre del Router", router_options)
    st.text_input("Puerto 1 (Velocidad: 100 Mbps)", value="LAN")
    st.text_input("Puerto 2 (Velocidad: 100 Mbps)", value="WAN")
    st.text_input("Puerto 3 (Velocidad: 100 Mbps)", value="Libre")
    st.text_input("Puerto 4 (Velocidad: 100 Mbps)", value="Libre")

    with col2:
        st.write("")
        st.write("")
        st.markdown("&#8594;")  # Flecha derecha

        with col3:
            st.header("Datos del Nuevo Router")
            nuevo_router = st.selectbox(
                "Nombre del Router", new_router_options)
            st.text_input("Puerto 1 (Velocidad: 100 Mbps)")
            st.text_input("Puerto 2 (Velocidad: 100 Mbps)")
            st.text_input("Puerto 3 (Velocidad: 100 Mbps)")
            st.text_input("Puerto 4 (Velocidad: 100 Mbps)")

            # Comentarios (sección 3)
            st.header(
                "Comentarios")
            st.text_area(
                "Comentarios")

            # Botón para enviar el formulario
            if st.button("Enviar"):
                st.success("Formulario enviado exitosamente!")
                
                
                
                
