"""Página: Selección de materia."""
import streamlit as st
from utils import ESTUDIANTES
from i18n import t


def render(go_home_fn, lang="es"):
    nombre = st.session_state.student
    info = ESTUDIANTES[nombre]
    st.markdown(f'<div class="hero" style="font-size:2.5rem;">{info["emoji"]} {t("hello", lang, nombre=nombre)}</div>', unsafe_allow_html=True)
    st.markdown(f'<p class="hero-sub">{t("choose_subject", lang)}</p>', unsafe_allow_html=True)
    st.write("")

    materias = info['materias']
    cols = st.columns(max(len(materias), 1))
    for i, (mat_nombre, mat_info) in enumerate(materias.items()):
        with cols[i % len(cols)]:
            st.markdown(f"""
            <div class="card card-blue" style="text-align:center;">
                <div style="font-size:3rem;">{mat_info['emoji']}</div>
                <h3>{mat_nombre}</h3>
                <p>{t("topics_available", lang, n=len(mat_info['topics']))}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"{mat_info['emoji']} {mat_nombre}", key=f"mat_{mat_nombre}", type="primary"):
                st.session_state.materia = mat_nombre
                st.session_state.phase = 'config'
                st.rerun()

    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button(t("change_student", lang)):
            go_home_fn()
            st.rerun()
    with col2:
        if st.button(t("logout", lang)):
            st.session_state.pop(f"auth_{nombre}", None)
            go_home_fn()
            st.rerun()
