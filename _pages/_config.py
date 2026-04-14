"""Página: Configuración de modo (Infinito / Examen)."""
import streamlit as st
from utils import ESTUDIANTES, DIFICULTADES
from scoring import new_score
from infinite import InfiniteGenerator


def render(lang="es"):
    nombre = st.session_state.student
    info = ESTUDIANTES[nombre]
    materia = st.session_state.materia
    mat_info = info['materias'][materia]
    topics = mat_info['topics']

    st.markdown(f'<div class="hero" style="font-size:2rem;">{info["emoji"]} {nombre} — {materia}</div>', unsafe_allow_html=True)
    st.write("")

    # Paso 1: elegir modo
    if 'config_mode' not in st.session_state:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="card card-orange" style="text-align:center; min-height:180px;">
                <div style="font-size:3rem;">♾️</div>
                <h3>Modo Infinito</h3>
                <p>Preguntas sin fin. Acumula XP, sube de nivel y rompe rachas.</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("♾️ Modo Infinito", type="primary", use_container_width=True):
                st.session_state.config_mode = 'infinito'
                st.rerun()
        with col2:
            st.markdown("""
            <div class="card card-blue" style="text-align:center; min-height:180px;">
                <div style="font-size:3rem;">📝</div>
                <h3>Modo Examen</h3>
                <p>Responde todas las preguntas y entrega al final. Estilo examen real.</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("📝 Modo Examen", type="primary", use_container_width=True):
                st.session_state.config_mode = 'examen'
                st.rerun()
        st.write("")
        if st.button("⬅️ Volver"):
            st.session_state.phase = 'materias'
            st.rerun()

    elif st.session_state.config_mode == 'infinito':
        _config_infinito(mat_info, topics)

    elif st.session_state.config_mode == 'examen':
        _config_examen(mat_info, topics)


def _config_infinito(mat_info, topics):
    st.markdown('<div class="card card-orange"><h3>♾️ Modo Infinito — Configuración</h3></div>', unsafe_allow_html=True)
    temas = st.multiselect("📚 Elige los temas:", list(topics.keys()), default=list(topics.keys()))

    dif_emojis = {
        "Fácil": "🟢 Fácil", "Normal": "🟡 Normal", "Difícil": "🔴 Difícil",
        "💀 Super Difícil": "💀 Super Difícil", "☠️ Mega Difícil": "☠️ Mega Difícil",
    }
    dif_sel = st.radio("💪 Dificultad:", DIFICULTADES, index=1, horizontal=True, format_func=lambda x: dif_emojis[x])
    default_time = {"Fácil": 30, "Normal": 20, "Difícil": 45, "💀 Super Difícil": 15, "☠️ Mega Difícil": 10}[dif_sel]
    if dif_sel in ("💀 Super Difícil", "☠️ Mega Difícil"):
        timer = default_time
        st.info(f"⏱️ Tiempo fijo: **{timer} segundos**")
    else:
        timer = st.select_slider("⏱️ Segundos por pregunta:", options=[10, 15, 20, 30, 45, 60, 90], value=default_time)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Cambiar modo"):
            del st.session_state.config_mode
            st.rerun()
    with col2:
        if st.button("🚀 ¡A jugar!", type="primary", use_container_width=True):
            if not temas:
                st.error("¡Elige al menos un tema! 📚")
            else:
                gen = InfiniteGenerator(mat_info['generator'], temas, dif_sel)
                st.session_state.gen = gen
                st.session_state.current_q = gen.next()
                st.session_state.score = new_score()
                st.session_state.timer = timer
                st.session_state.q_start = None
                st.session_state.answered = False
                st.session_state.last_gained = 0
                st.session_state.last_correct = None
                st.session_state.current_topics = topics
                st.session_state.dificultad = dif_sel
                st.session_state.wrong_questions = []
                st.session_state.topic_stats = {}
                st.session_state.phase = 'quiz'
                del st.session_state.config_mode
                st.rerun()


def _config_examen(mat_info, topics):
    st.markdown('<div class="card card-blue"><h3>📝 Modo Examen — Configuración</h3></div>', unsafe_allow_html=True)
    temas = st.multiselect("📚 Elige los temas:", list(topics.keys()), default=list(topics.keys()))
    n_exam = st.select_slider("📝 Número de preguntas:", options=[10, 15, 20, 25, 30, 35, 40, 45, 50], value=30)
    st.info("🔴 El examen siempre usa dificultad **Difícil** para mayor reto.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Cambiar modo"):
            del st.session_state.config_mode
            st.rerun()
    with col2:
        if st.button("📝 Iniciar Examen", type="primary", use_container_width=True):
            if not temas:
                st.error("¡Elige al menos un tema! 📚")
            else:
                gen = InfiniteGenerator(mat_info['generator'], temas, "Difícil")
                st.session_state.exam_questions = [gen.next() for _ in range(n_exam)]
                st.session_state.exam_submitted = False
                st.session_state.exam_results = None
                st.session_state.exam_session_saved = False
                st.session_state.dificultad = "Difícil"
                st.session_state.current_topics = topics
                st.session_state.phase = 'exam'
                del st.session_state.config_mode
                st.rerun()
