"""Página: Resultados del modo infinito."""
import streamlit as st
from scoring import get_level, get_rank
from leaderboard import save_session, LOGROS
from utils import ESTUDIANTES
from i18n import t


def render(go_home_fn, lang="es"):
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

    st.markdown(f'<div class="hero" style="font-size:2.2rem;">{info.get("emoji","")} {t("results_title", lang, nombre=nombre)}</div>', unsafe_allow_html=True)

    score_cls = "score-green" if pct >= 80 else ("score-yellow" if pct >= 60 else "score-red")
    st.markdown(f"""
    <div class="score-box {score_cls}">
        <div style="font-size:2rem;">{rank}</div>
        <div class="score-num">{sc['xp']} XP</div>
        <div style="font-size:1.2rem;">Nivel <b>{level}</b> — {pct}% ({sc['correct']}/{sc['total']})</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="stats-row">
        <div class="stat-item stat-orange"><h3>🔥 {sc['max_streak']}</h3><p>{t("max_streak", lang)}</p></div>
        <div class="stat-item stat-purple"><h3>💪 x{sc['max_multiplier']}</h3><p>{t("max_mult", lang)}</p></div>
        <div class="stat-item stat-blue"><h3>📝 {sc['total']}</h3><p>{t("questions_seen", lang)}</p></div>
    </div>
    """, unsafe_allow_html=True)

    if nuevos_logros:
        st.markdown(f'<div class="card card-orange"><h3>{t("new_achievements", lang)}</h3></div>', unsafe_allow_html=True)
        for l in nuevos_logros:
            st.success(f"{l['emoji']} **{l['nombre']}** — {l['desc']}")

    if pct >= 90:   st.success(t("msg_incredible", lang, nombre=nombre))
    elif pct >= 70: st.info(t("msg_good", lang, nombre=nombre))
    elif pct >= 50: st.warning(t("msg_ok", lang, nombre=nombre))
    else:           st.error(t("msg_bad", lang, nombre=nombre))

    st.write("")
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        if st.button(t("play_again", lang), type="primary", use_container_width=True):
            st.session_state.phase = 'config'
            st.session_state.session_saved = False
            st.rerun()
    with r1c2:
        if st.button(t("other_subject", lang), use_container_width=True):
            st.session_state.phase = 'materias'
            st.session_state.session_saved = False
            st.rerun()
    r2c1, r2c2 = st.columns(2)
    with r2c1:
        if st.button(t("leaderboard", lang), use_container_width=True):
            st.session_state.phase = 'leaderboard'
            st.rerun()
    with r2c2:
        if st.button(t("home", lang), use_container_width=True):
            go_home_fn()
            st.rerun()
