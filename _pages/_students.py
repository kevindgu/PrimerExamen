"""Página: Selección de estudiante + autenticación PIN."""
import streamlit as st
from utils import ESTUDIANTES
from auth import render_pin_screen, is_authenticated
from i18n import t


def render(go_home_fn, lang="es"):
    nombre = st.session_state.get('student')
    if nombre and nombre in ESTUDIANTES:
        info = ESTUDIANTES[nombre]
        autenticado = render_pin_screen(nombre, info, lang)
        if autenticado:
            st.session_state.phase = 'materias'
            st.rerun()
        return

    st.markdown(f'<div class="hero">{t("app_title", lang)}</div>', unsafe_allow_html=True)
    st.markdown(f'<p class="hero-sub">{t("app_sub", lang)}</p>', unsafe_allow_html=True)
    st.write("")

    col_lb, col_admin = st.columns(2)
    with col_lb:
        if st.button(t("leaderboard_btn", lang), use_container_width=True):
            st.session_state.phase = 'leaderboard'
            st.rerun()
    with col_admin:
        if st.button(t("admin_btn", lang), use_container_width=True):
            st.session_state.phase = 'admin'
            st.rerun()
    st.write("")

    cols = st.columns(3)
    for i, (nombre_est, info) in enumerate(ESTUDIANTES.items()):
        with cols[i]:
            active_badge = f'<p style="color:#2ecc71; font-size:0.8rem;">{t("session_active", lang)}</p>' if is_authenticated(nombre_est) else ''
            st.markdown(f"""
            <div class="student-card" style="background: linear-gradient(135deg, {info['color']}22, {info['color']}44); border: 3px solid {info['color']};">
                <div style="font-size: 4rem;">{info['emoji']}</div>
                <h2 style="color: {info['color']}; margin: 5px 0;">{nombre_est}</h2>
                <p style="color: #666;">{info['grado']}</p>
                {active_badge}
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"{info['emoji']} ¡Soy {nombre_est}!", key=f"student_{nombre_est}", type="primary"):
                if is_authenticated(nombre_est):
                    st.session_state.student = nombre_est
                    st.session_state.phase = 'materias'
                else:
                    st.session_state.student = nombre_est
                st.rerun()
