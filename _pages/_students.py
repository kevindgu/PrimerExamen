"""Página: Selección de estudiante."""
import streamlit as st
from utils import ESTUDIANTES


def render(go_home_fn):
    st.markdown('<div class="hero">🏫 MatePlay</div>', unsafe_allow_html=True)
    st.markdown('<p class="hero-sub">¡Aprende jugando! ¿Quién va a practicar? 🎮✨</p>', unsafe_allow_html=True)
    st.write("")

    if st.button("🏆 Ver tabla de puntuaciones", use_container_width=True):
        st.session_state.phase = 'leaderboard'
        st.rerun()
    st.write("")

    cols = st.columns(3)
    for i, (nombre, info) in enumerate(ESTUDIANTES.items()):
        with cols[i]:
            st.markdown(f"""
            <div class="student-card" style="background: linear-gradient(135deg, {info['color']}22, {info['color']}44); border: 3px solid {info['color']};">
                <div style="font-size: 4rem;">{info['emoji']}</div>
                <h2 style="color: {info['color']}; margin: 5px 0;">{nombre}</h2>
                <p style="color: #666;">{info['grado']}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"{info['emoji']} ¡Soy {nombre}!", key=f"student_{nombre}", type="primary"):
                st.session_state.student = nombre
                st.session_state.phase = 'materias'
                st.rerun()
