"""Página: Tabla de puntuaciones."""
import streamlit as st
from leaderboard import (get_ranking, get_ranking_materia, get_ranking_dificultad,
                         get_temas_stats, get_preguntas_debiles,
                         LOGROS, DIFICULTADES_ORDEN, MATERIAS_ORDEN)
from utils import ESTUDIANTES


def _render_ranking(ranking, mostrar_mult=True):
    if not ranking:
        st.info("¡Nadie ha jugado en este modo todavía!")
        return
    medallas = ["🥇", "🥈", "🥉"]
    for i, p in enumerate(ranking):
        medalla = medallas[i] if i < 3 else f"#{i+1}"
        color = ["#ffd700", "#c0c0c0", "#cd7f32"][i] if i < 3 else "#9b59b6"
        logros_icons = " ".join(
            next((l["emoji"] for l in LOGROS if l["id"] == lid), "")
            for lid in p.get("logros", [])
        )
        score_fmt = f"{p.get('score', p['xp_total']):,}"
        extras = (f"📝 {p['total_respuestas']} preguntas &nbsp;|&nbsp; "
                  f"✅ {p['pct']}% efectividad &nbsp;|&nbsp; "
                  f"🔥 Racha: {p['max_racha']} &nbsp;|&nbsp; "
                  f"🎯 Mejor sesión: {p['mejor_sesion_xp']:,} XP &nbsp;|&nbsp; "
                  f"🎮 {p['sesiones']} sesiones")
        if mostrar_mult and p.get('max_multiplicador', 1) > 1:
            extras += f" &nbsp;|&nbsp; 💪 Mult máx: x{p['max_multiplicador']}"
        st.markdown(f"""
        <div class="card" style="border-left: 6px solid {color}; margin: 8px 0;">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
                <div>
                    <span style="font-size:1.8rem;">{medalla}</span>
                    <span style="font-size:1.3rem; font-weight:bold; margin-left:8px;">{p['nombre']}</span>
                    <span style="margin-left:6px; font-size:1rem;">{logros_icons}</span>
                </div>
                <div style="text-align:right;">
                    <div style="font-size:1.6rem; font-weight:bold; color:{color};">&#11088; {score_fmt}</div>
                    <div style="font-size:0.8rem; color:#888;">{p['xp_total']:,} XP bruto</div>
                </div>
            </div>
            <div style="margin-top:8px; font-size:0.85rem; color:#555;">{extras}</div>
        </div>
        """, unsafe_allow_html=True)


def render(go_home_fn, lang="es"):
    st.markdown('<div class="hero" style="font-size:2.5rem;">🏆 Tabla de Puntuaciones</div>', unsafe_allow_html=True)
    st.write("")

    tab_inf, tab_exam, tab_mat, tab_dif, tab_debiles = st.tabs([
        "♾️ Modo Infinito", "📝 Modo Examen", "📚 Por Materia", "💪 Por Dificultad", "📉 Áreas Débiles"
    ])

    with tab_inf:
        st.caption("🏆 Ranking por **Score Balanceado** = XP × efectividad × volumen")
        _render_ranking(get_ranking(modo='infinito'))

    with tab_exam:
        st.caption("📝 Solo sesiones de **Modo Examen**")
        _render_ranking(get_ranking(modo='examen'), mostrar_mult=False)

    with tab_mat:
        mat_sel = st.selectbox("Selecciona la materia:", MATERIAS_ORDEN, key="lb_mat_sel")
        _render_ranking(get_ranking_materia(mat_sel), mostrar_mult=False)

    with tab_dif:
        dif_tabs = st.tabs(DIFICULTADES_ORDEN)
        for i, dif in enumerate(DIFICULTADES_ORDEN):
            with dif_tabs[i]:
                _render_ranking(get_ranking_dificultad(dif),
                                mostrar_mult=(dif not in ("💀 Super Difícil", "☠️ Mega Difícil")))

    with tab_debiles:
        st.markdown("### 📉 Temas por mejorar — por estudiante")
        for nombre, info in ESTUDIANTES.items():
            temas = get_temas_stats(nombre)
            preguntas = get_preguntas_debiles(nombre)
            if not temas and not preguntas:
                continue
            with st.expander(f"{info['emoji']} {nombre}", expanded=True):
                if temas:
                    filas = []
                    for clave, ts in temas.items():
                        intentos = ts["intentos"]
                        correctas = ts["correctas"]
                        pct_t = int(100 * correctas / intentos) if intentos else 0
                        filas.append((ts["materia"], ts["topic"], correctas, intentos, pct_t))
                    filas.sort(key=lambda x: x[4])
                    st.markdown("**Precisión por tema:**")
                    for mat_t, topic_t, correctas_t, intentos_t, pct_t in filas:
                        color_b = "#e74c3c" if pct_t < 60 else ("#f39c12" if pct_t < 80 else "#2ecc71")
                        st.markdown(f"""
                        <div style="margin:4px 0;">
                            <span style="font-size:0.85rem; color:#555;"><b>{mat_t}</b> › {topic_t}</span>
                            <span style="font-size:0.85rem; font-weight:bold; color:{color_b}; margin-left:8px;">{pct_t}% ({correctas_t}/{intentos_t})</span>
                        </div>
                        """, unsafe_allow_html=True)
                        st.progress(pct_t / 100)

                if preguntas:
                    st.write("")
                    st.markdown("**Últimas preguntas incorrectas:**")
                    for pq in reversed(preguntas[-10:]):
                        mat_icon = {"Matemáticas": "🧮", "Ciencias": "🔬",
                                    "Estudios Sociales": "🌍", "Español": "📖"}.get(pq.get("materia", ""), "📝")
                        st.markdown(f"""
                        <div class="result-wrong" style="margin:5px 0; font-size:0.9rem;">
                            {mat_icon} <b>{pq.get('materia','')} › {pq.get('topic','')}</b>
                            &nbsp;<span style="color:#888; font-size:0.8rem;">{pq.get('fecha','')}</span><br>
                            <span>❓ {pq.get('pregunta','')[:120]}</span><br>
                            <span style="color:#dc3545;">✗ <b>{pq.get('respuesta_dada','')[:60]}</b></span>
                            &nbsp;&nbsp;
                            <span style="color:#28a745;">✓ <b>{pq.get('respuesta_correcta','')[:60]}</b></span>
                        </div>
                        """, unsafe_allow_html=True)

    st.write("")
    with st.expander("🏅 Todos los logros disponibles"):
        cols = st.columns(2)
        for i, logro in enumerate(LOGROS):
            with cols[i % 2]:
                st.markdown(f"{logro['emoji']} **{logro['nombre']}** — {logro['desc']}")

    st.write("")
    if st.button("⬅️ Volver al inicio", type="primary"):
        go_home_fn()
        st.rerun()
