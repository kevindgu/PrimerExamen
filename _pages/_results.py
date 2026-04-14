"""Página: Resultados del modo infinito."""
import streamlit as st
from scoring import get_level, get_rank
from leaderboard import save_session, LOGROS
from utils import ESTUDIANTES


def render(go_home_fn):
    sc = st.session_state.score
    nombre = st.session_state.student
    info = ESTUDIANTES.get(nombre, {})
    materia = st.session_state.get('materia', '')
    level, level_xp, level_needed = get_level(sc['xp'])
    rank = get_rank(sc['xp'])

    if not st.session_state.get('session_saved'):
        nuevos_logros = save_session(
            nombre, sc, materia, materia,
            st.session_state.get('dificultad', 'Normal'),
            modo='infinito',
            preguntas_fallidas=st.session_state.get('wrong_questions', []),
            topic_stats_sesion=st.session_state.get('topic_stats', {}),
        )
        st.session_state.session_saved = True
        st.session_state.nuevos_logros = nuevos_logros
    nuevos_logros = st.session_state.get('nuevos_logros', [])

    pct = int(100 * sc['correct'] / sc['total']) if sc['total'] else 0

    if pct >= 80:
        st.markdown('<div class="confetti">🎉🌟🏆🌟🎉</div>', unsafe_allow_html=True)
        st.balloons()

    st.markdown(f'<div class="hero" style="font-size:2.2rem;">{info.get("emoji","")} Resultados de {nombre}</div>', unsafe_allow_html=True)

    score_cls = "score-green" if pct >= 80 else ("score-yellow" if pct >= 60 else "score-red")
    st.markdown(f"""
    <div class="score-box {score_cls}">
        <div style="font-size:2rem;">{rank}</div>
        <div class="score-num">{sc['xp']} XP</div>
        <div style="font-size:1.2rem;">Nivel <b>{level}</b> — {pct}% aciertos ({sc['correct']}/{sc['total']})</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="stats-row">
        <div class="stat-item stat-orange"><h3>🔥 {sc['max_streak']}</h3><p>Racha máxima</p></div>
        <div class="stat-item stat-purple"><h3>💪 x{sc['max_multiplier']}</h3><p>Multiplicador máx</p></div>
        <div class="stat-item stat-blue"><h3>📝 {sc['total']}</h3><p>Preguntas vistas</p></div>
    </div>
    """, unsafe_allow_html=True)

    if nuevos_logros:
        st.markdown('<div class="card card-orange"><h3>🎉 ¡Nuevos logros desbloqueados!</h3></div>', unsafe_allow_html=True)
        for l in nuevos_logros:
            st.success(f"{l['emoji']} **{l['nombre']}** — {l['desc']}")

    if pct >= 90:   st.success(f"🌟 ¡INCREÍBLE {nombre}! ¡Eres un genio! 🧠✨")
    elif pct >= 70: st.info(f"😊 ¡Muy bien {nombre}! Estás cerca de dominar estos temas. 💪")
    elif pct >= 50: st.warning(f"🤔 Vas avanzando {nombre}, pero hay temas que repasar. 📖")
    else:           st.error(f"📚 {nombre}, necesitas practicar más. ¡Cada intento te hace mejor! 💪")

    st.write("")
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        if st.button("🔄 Jugar de nuevo", type="primary", use_container_width=True):
            st.session_state.phase = 'config'
            st.session_state.session_saved = False
            st.rerun()
    with r1c2:
        if st.button("📚 Otra materia", use_container_width=True):
            st.session_state.phase = 'materias'
            st.session_state.session_saved = False
            st.rerun()
    r2c1, r2c2 = st.columns(2)
    with r2c1:
        if st.button("🏆 Tabla de puntos", use_container_width=True):
            st.session_state.phase = 'leaderboard'
            st.rerun()
    with r2c2:
        if st.button("🏠 Inicio", use_container_width=True):
            go_home_fn()
            st.rerun()
