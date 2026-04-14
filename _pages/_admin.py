"""Página: Panel de Administrador."""
import io
import csv
import streamlit as st
from auth import get_admin_pin
from leaderboard import get_all_players, get_temas_stats, get_preguntas_debiles
from utils import ESTUDIANTES
from scoring import get_level, get_rank


def render_admin_login():
    """Pantalla de login del admin."""
    st.markdown("""
    <div style="text-align:center; padding:20px;">
        <div style="font-size:4rem;">🔐</div>
        <h2 style="font-family:'Fredoka One',cursive; color:white; font-size:2rem;">Panel de Administrador</h2>
        <p style="color:#ddd;">Ingresa el PIN de administrador</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        pin = st.text_input("PIN Admin:", type="password", max_chars=4,
                            placeholder="••••", key="admin_pin_input",
                            label_visibility="collapsed")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("⬅️ Volver", use_container_width=True):
                st.session_state.phase = 'students'
                st.rerun()
        with c2:
            if st.button("🔓 Entrar", type="primary", use_container_width=True):
                if pin == get_admin_pin():
                    st.session_state.admin_auth = True
                    st.rerun()
                else:
                    st.error("❌ PIN incorrecto")


def render(go_home_fn, lang="es"):
    if not st.session_state.get('admin_auth'):
        render_admin_login()
        return

    st.markdown('<div class="hero" style="font-size:2.2rem;">👨‍💼 Panel de Administrador</div>', unsafe_allow_html=True)
    st.write("")

    data = get_all_players()

    # ── Tabs principales ──
    tab_resumen, tab_progreso, tab_debiles, tab_historial, tab_export = st.tabs([
        "📊 Resumen", "📈 Progreso", "⚠️ Áreas débiles", "📅 Historial", "📥 Exportar"
    ])

    # ── RESUMEN ──
    with tab_resumen:
        st.markdown("### Resumen general de estudiantes")
        for nombre, info in ESTUDIANTES.items():
            stats = data.get(nombre, {})
            if not stats or stats.get('total_respuestas', 0) == 0:
                st.markdown(f"""
                <div class="card card-blue">
                    <b>{info['emoji']} {nombre}</b> — Sin sesiones registradas aún
                </div>
                """, unsafe_allow_html=True)
                continue

            tr = stats.get("total_respuestas", 0)
            tc = stats.get("total_correctas", 0)
            pct = int(100 * tc / tr) if tr > 0 else 0
            xp = stats.get("xp_total", 0)
            level, _, _ = get_level(xp)
            rank = get_rank(xp)
            sesiones = stats.get("sesiones", 0)
            racha = stats.get("max_racha", 0)
            logros = len(stats.get("logros", []))

            color = info['color']
            pct_color = "#2ecc71" if pct >= 80 else ("#f39c12" if pct >= 60 else "#e74c3c")

            st.markdown(f"""
            <div class="card" style="border-left: 6px solid {color};">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                    <div>
                        <span style="font-size:2rem;">{info['emoji']}</span>
                        <span style="font-size:1.4rem; font-weight:bold; margin-left:8px;">{nombre}</span>
                        <span style="color:#666; font-size:0.9rem; margin-left:8px;">{info['grado']}</span>
                    </div>
                    <div style="text-align:right;">
                        <div style="font-size:1.5rem; font-weight:bold; color:{color};">⭐ {xp:,} XP</div>
                        <div style="font-size:0.85rem; color:#888;">{rank} — Nivel {level}</div>
                    </div>
                </div>
                <div style="display:flex; gap:15px; margin-top:12px; flex-wrap:wrap; font-size:0.9rem;">
                    <span>📝 <b>{tr}</b> preguntas</span>
                    <span style="color:{pct_color};">✅ <b>{pct}%</b> efectividad</span>
                    <span>🔥 Racha máx: <b>{racha}</b></span>
                    <span>🎮 <b>{sesiones}</b> sesiones</span>
                    <span>🏅 <b>{logros}</b> logros</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ── PROGRESO POR MATERIA ──
    with tab_progreso:
        st.markdown("### Progreso por materia")
        nombre_sel = st.selectbox("Estudiante:", list(ESTUDIANTES.keys()), key="prog_sel")
        stats = data.get(nombre_sel, {})
        por_materia = stats.get("por_materia", {})

        if not por_materia:
            st.info(f"{ESTUDIANTES[nombre_sel]['emoji']} {nombre_sel} no tiene sesiones registradas aún.")
        else:
            for materia, ms in por_materia.items():
                tr = ms.get("total_respuestas", 0)
                tc = ms.get("total_correctas", 0)
                pct = int(100 * tc / tr) if tr > 0 else 0
                color = "#2ecc71" if pct >= 80 else ("#f39c12" if pct >= 60 else "#e74c3c")
                emoji = {"Matemáticas": "🧮", "Ciencias": "🔬",
                         "Estudios Sociales": "🌍", "Español": "📖"}.get(materia, "📚")
                st.markdown(f"""
                <div style="margin:8px 0;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                        <span><b>{emoji} {materia}</b> — {ms.get('sesiones',0)} sesiones</span>
                        <span style="color:{color}; font-weight:bold;">{pct}% ({tc}/{tr})</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.progress(pct / 100)

        # Progreso por tema
        temas = get_temas_stats(nombre_sel)
        if temas:
            st.write("")
            st.markdown("#### Precisión por tema")
            filas = []
            for clave, ts in temas.items():
                intentos = ts["intentos"]
                correctas = ts["correctas"]
                pct_t = int(100 * correctas / intentos) if intentos else 0
                filas.append((ts["materia"], ts["topic"], correctas, intentos, pct_t))
            filas.sort(key=lambda x: x[4])
            for mat_t, topic_t, c_t, i_t, pct_t in filas:
                color_b = "#e74c3c" if pct_t < 60 else ("#f39c12" if pct_t < 80 else "#2ecc71")
                st.markdown(f"""
                <div style="margin:4px 0; display:flex; justify-content:space-between;">
                    <span style="font-size:0.85rem; color:#555;"><b>{mat_t}</b> › {topic_t}</span>
                    <span style="font-size:0.85rem; font-weight:bold; color:{color_b};">{pct_t}% ({c_t}/{i_t})</span>
                </div>
                """, unsafe_allow_html=True)
                st.progress(pct_t / 100)

    # ── ÁREAS DÉBILES ──
    with tab_debiles:
        st.markdown("### ⚠️ Preguntas que más fallan")
        nombre_sel2 = st.selectbox("Estudiante:", list(ESTUDIANTES.keys()), key="deb_sel")
        preguntas = get_preguntas_debiles(nombre_sel2)
        if not preguntas:
            st.info("No hay preguntas débiles registradas aún.")
        else:
            # Agrupar por tema y contar fallos
            conteo = {}
            for pq in preguntas:
                clave = f"{pq.get('materia','')} › {pq.get('topic','')}"
                conteo[clave] = conteo.get(clave, 0) + 1
            conteo_sorted = sorted(conteo.items(), key=lambda x: x[1], reverse=True)

            st.markdown("**Temas con más errores:**")
            for tema, fallos in conteo_sorted[:10]:
                st.markdown(f"- **{tema}**: {fallos} {'error' if fallos == 1 else 'errores'}")

            st.write("")
            st.markdown("**Últimas 10 preguntas incorrectas:**")
            for pq in reversed(preguntas[-10:]):
                mat_icon = {"Matemáticas": "🧮", "Ciencias": "🔬",
                            "Estudios Sociales": "🌍", "Español": "📖"}.get(pq.get("materia", ""), "📝")
                st.markdown(f"""
                <div class="result-wrong" style="margin:5px 0; font-size:0.88rem;">
                    {mat_icon} <b>{pq.get('materia','')} › {pq.get('topic','')}</b>
                    <span style="color:#888; font-size:0.8rem;"> — {pq.get('fecha','')}</span><br>
                    ❓ {pq.get('pregunta','')[:120]}<br>
                    <span style="color:#dc3545;">✗ <b>{pq.get('respuesta_dada','')[:60]}</b></span>
                    &nbsp;→&nbsp;
                    <span style="color:#28a745;">✓ <b>{pq.get('respuesta_correcta','')[:60]}</b></span>
                </div>
                """, unsafe_allow_html=True)

    # ── HISTORIAL ──
    with tab_historial:
        st.markdown("### 📅 Historial de sesiones")
        nombre_sel3 = st.selectbox("Estudiante:", list(ESTUDIANTES.keys()), key="hist_sel")
        stats3 = data.get(nombre_sel3, {})
        historial = stats3.get("historial", [])
        if not historial:
            st.info("Sin historial de sesiones.")
        else:
            for h in reversed(historial):
                modo_icon = "📝" if h.get("modo") == "examen" else "♾️"
                pct_h = h.get("pct", 0)
                color_h = "#2ecc71" if pct_h >= 80 else ("#f39c12" if pct_h >= 60 else "#e74c3c")
                st.markdown(f"""
                <div class="card" style="padding:12px 18px; margin:6px 0;">
                    <div style="display:flex; justify-content:space-between; flex-wrap:wrap; gap:6px;">
                        <div>
                            <span style="font-size:1.1rem;">{modo_icon}</span>
                            <b style="margin-left:6px;">{h.get('materia','')}</b>
                            <span style="color:#888; font-size:0.85rem; margin-left:8px;">{h.get('fecha','')}</span>
                        </div>
                        <div style="text-align:right;">
                            <span style="color:{color_h}; font-weight:bold;">{pct_h}%</span>
                            <span style="color:#888; font-size:0.85rem; margin-left:8px;">+{h.get('xp',0):,} XP</span>
                        </div>
                    </div>
                    <div style="font-size:0.82rem; color:#666; margin-top:4px;">
                        ✅ {h.get('correctas',0)}/{h.get('total',0)} correctas &nbsp;|&nbsp;
                        🔥 Racha: {h.get('racha',0)} &nbsp;|&nbsp;
                        {h.get('dificultad','')}
                    </div>
                </div>
                """, unsafe_allow_html=True)

    # ── EXPORTAR ──
    with tab_export:
        st.markdown("### 📥 Exportar reportes")
        nombre_exp = st.selectbox("Estudiante:", ["Todos"] + list(ESTUDIANTES.keys()), key="exp_sel")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("📊 Exportar resumen CSV", use_container_width=True):
                csv_data = _generar_csv_resumen(data, nombre_exp)
                st.download_button(
                    label="⬇️ Descargar resumen.csv",
                    data=csv_data,
                    file_name=f"resumen_{'todos' if nombre_exp == 'Todos' else nombre_exp.lower()}.csv",
                    mime="text/csv",
                    use_container_width=True
                )
        with col2:
            if st.button("📋 Exportar historial CSV", use_container_width=True):
                csv_data = _generar_csv_historial(data, nombre_exp)
                st.download_button(
                    label="⬇️ Descargar historial.csv",
                    data=csv_data,
                    file_name=f"historial_{'todos' if nombre_exp == 'Todos' else nombre_exp.lower()}.csv",
                    mime="text/csv",
                    use_container_width=True
                )

        st.write("")
        if st.button("📉 Exportar preguntas débiles CSV", use_container_width=True):
            csv_data = _generar_csv_debiles(data, nombre_exp)
            st.download_button(
                label="⬇️ Descargar preguntas_debiles.csv",
                data=csv_data,
                file_name=f"debiles_{'todos' if nombre_exp == 'Todos' else nombre_exp.lower()}.csv",
                mime="text/csv",
                use_container_width=True
            )

    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔒 Cerrar sesión admin", use_container_width=True):
            st.session_state.pop('admin_auth', None)
            st.rerun()
    with col2:
        if st.button("🏠 Volver al inicio", type="primary", use_container_width=True):
            st.session_state.pop('admin_auth', None)
            go_home_fn()
            st.rerun()


# ── Generadores CSV ──────────────────────────────────────────

def _generar_csv_resumen(data: dict, nombre_filtro: str) -> bytes:
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Estudiante", "XP Total", "Nivel", "Sesiones",
                     "Total Preguntas", "Correctas", "Efectividad %",
                     "Racha Máxima", "Mejor Sesión XP", "Logros"])
    nombres = [nombre_filtro] if nombre_filtro != "Todos" else list(data.keys())
    for nombre in nombres:
        stats = data.get(nombre, {})
        if not stats:
            continue
        tr = stats.get("total_respuestas", 0)
        tc = stats.get("total_correctas", 0)
        pct = int(100 * tc / tr) if tr > 0 else 0
        xp = stats.get("xp_total", 0)
        level, _, _ = get_level(xp)
        writer.writerow([
            nombre, xp, level, stats.get("sesiones", 0),
            tr, tc, pct, stats.get("max_racha", 0),
            stats.get("mejor_sesion_xp", 0), len(stats.get("logros", []))
        ])
    return output.getvalue().encode("utf-8-sig")


def _generar_csv_historial(data: dict, nombre_filtro: str) -> bytes:
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Estudiante", "Fecha", "Materia", "Modo", "Dificultad",
                     "Correctas", "Total", "Efectividad %", "XP Ganado", "Racha"])
    nombres = [nombre_filtro] if nombre_filtro != "Todos" else list(data.keys())
    for nombre in nombres:
        for h in data.get(nombre, {}).get("historial", []):
            writer.writerow([
                nombre, h.get("fecha", ""), h.get("materia", ""),
                h.get("modo", "infinito"), h.get("dificultad", ""),
                h.get("correctas", 0), h.get("total", 0), h.get("pct", 0),
                h.get("xp", 0), h.get("racha", 0)
            ])
    return output.getvalue().encode("utf-8-sig")


def _generar_csv_debiles(data: dict, nombre_filtro: str) -> bytes:
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Estudiante", "Fecha", "Materia", "Tema",
                     "Pregunta", "Respondió", "Respuesta Correcta"])
    nombres = [nombre_filtro] if nombre_filtro != "Todos" else list(data.keys())
    for nombre in nombres:
        for pq in data.get(nombre, {}).get("preguntas_debiles", []):
            writer.writerow([
                nombre, pq.get("fecha", ""), pq.get("materia", ""),
                pq.get("topic", ""), pq.get("pregunta", "")[:200],
                pq.get("respuesta_dada", ""), pq.get("respuesta_correcta", "")
            ])
    return output.getvalue().encode("utf-8-sig")
