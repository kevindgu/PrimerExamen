"""Página: Selección de materia."""
import streamlit as st
from utils import ESTUDIANTES


def render(go_home_fn):
    nombre = st.session_state.student
    info = ESTUDIANTES[nombre]
    st.markdown(f'<div class="hero" style="font-size:2.5rem;">{info["emoji"]} ¡Hola {nombre}!</div>', unsafe_allow_html=True)
    st.markdown('<p class="hero-sub">¿Qué materia quieres practicar?</p>', unsafe_allow_html=True)
    st.write("")

    materias = info['materias']
    cols = st.columns(max(len(materias), 1))
    for i, (mat_nombre, mat_info) in enumerate(materias.items()):
        with cols[i % len(cols)]:
            st.markdown(f"""
            <div class="card card-blue" style="text-align:center;">
                <div style="font-size:3rem;">{mat_info['emoji']}</div>
                <h3>{mat_nombre}</h3>
                <p>{len(mat_info['topics'])} temas disponibles</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"{mat_info['emoji']} {mat_nombre}", key=f"mat_{mat_nombre}", type="primary"):
                st.session_state.materia = mat_nombre
                st.session_state.phase = 'config'
                st.rerun()

    st.write("")
    if st.button("⬅️ Cambiar estudiante"):
        go_home_fn()
        st.rerun()
