"""Páginas: Modo Examen (exam, exam_results, exam_correction, exam_correction_done)."""
import time
import streamlit as st
from utils import ESTUDIANTES, check_answer
from leaderboard import save_session, add_correction_xp

LETRAS = ["A", "B", "C", "D", "E", "F"]


def render_exam(lang="es"):
    nombre = st.session_state.student
    info = ESTUDIANTES[nombre]
    materia = st.session_state.materia
    preguntas = st.session_state.exam_questions

    st.markdown(f"""
    <div class="exam-header">
        <h2>{info['emoji']} Examen — {materia}</h2>
        <p><b>Estudiante:</b> {nombre} &nbsp;|&nbsp; <b>Fecha:</b> {time.strftime('%d/%m/%Y')} &nbsp;|&nbsp; <b>Preguntas:</b> {len(preguntas)}</p>
    </div>
    <div class="exam-instrucciones">
        ✏️ <b>Instrucciones:</b> Marque con <b>X</b> la respuesta correcta. Solo puede seleccionar <b>una</b> opción por pregunta.
    </div>
    """, unsafe_allow_html=True)

    if st.button("⬅️ Cancelar"):
        st.session_state.phase = 'config'
        st.rerun()

    respuestas = {}
    with st.form("exam_form"):
        for i, q in enumerate(preguntas):
            opciones_orig = q.get('opciones_btn', [])
            opciones_labeled = [f"{LETRAS[j]})  {opciones_orig[j]}" for j in range(len(opciones_orig))]
            st.markdown(f"""
            <div class="exam-pregunta">
                <div class="num">Pregunta {i + 1}</div>
                <div class="texto">{q['question']}</div>
            </div>
            """, unsafe_allow_html=True)
            if q.get('imagen2'):
                ci1, ci2 = st.columns(2)
                with ci1:
                    st.caption("Imagen 1")
                    try: st.image(q['imagen'], use_container_width=True)
                    except: pass
                with ci2:
                    st.caption("Imagen 2")
                    try: st.image(q['imagen2'], use_container_width=True)
                    except: pass
            elif q.get('imagen'):
                try: st.image(q['imagen'], use_container_width=True)
                except: pass
            if q.get('texto_comparar'):
                st.markdown(f"""<div style="background:#f0f0ff; border-left:4px solid #9b59b6;
                    padding:10px 14px; border-radius:8px; margin:6px 0;
                    font-size:0.95rem; font-style:italic; color:#333;">{q['texto_comparar']}</div>""",
                    unsafe_allow_html=True)
            respuestas[i] = st.radio(label=f"q{i}", options=opciones_labeled, index=None,
                                     key=f"exam_radio_{i}", label_visibility="collapsed")
            st.write("")
        submitted = st.form_submit_button("📤 Entregar Examen", type="primary", use_container_width=True)

    if submitted:
        resultados = []
        for i, q in enumerate(preguntas):
            sel = respuestas.get(i)
            resp_limpia = sel.split(")  ", 1)[-1].strip() if sel and ")  " in sel else sel
            correcto = check_answer(q, resp_limpia) if resp_limpia else False
            resultados.append({
                "pregunta": q['question'], "topic": q.get('topic', ''),
                "opciones": q.get('opciones_btn', []), "respuesta_correcta": q['answer'],
                "imagen": q.get('imagen', ''), "imagen2": q.get('imagen2', ''),
                "is_numeric": q.get('is_numeric', False),
                "seleccionada": resp_limpia, "correcto": correcto,
                "procedure": q.get('procedure', ''),
            })
        st.session_state.exam_results = resultados
        st.session_state.exam_submitted = True
        st.session_state.phase = 'exam_results'
        st.rerun()


def render_exam_results(go_home_fn, lang="es"):
    nombre = st.session_state.student
    info = ESTUDIANTES[nombre]
    materia = st.session_state.materia
    resultados = st.session_state.exam_results

    total = len(resultados)
    correctas = sum(1 for r in resultados if r['correcto'])
    vacias = sum(1 for r in resultados if r['seleccionada'] is None)
    pct = int(100 * correctas / total) if total else 0

    if not st.session_state.get('exam_session_saved'):
        _max_racha, _racha = 0, 0
        for r in resultados:
            if r['correcto']: _racha += 1; _max_racha = max(_max_racha, _racha)
            else: _racha = 0
        _exam_score = {'xp': correctas * 50, 'correct': correctas, 'total': total,
                       'max_streak': _max_racha, 'max_multiplier': 1,
                       'history': [(i, r['correcto']) for i, r in enumerate(resultados)]}
        _fallidas = [{"fecha": time.strftime("%d/%m/%Y"), "materia": materia,
                      "topic": r.get('topic', ''), "pregunta": r['pregunta'][:150],
                      "respuesta_dada": r.get('seleccionada') or '(sin responder)',
                      "respuesta_correcta": r['respuesta_correcta']}
                     for r in resultados if not r['correcto']]
        _topic_stats = {}
        for r in resultados:
            _tp = r.get('topic', 'General')
            _cl = f"{materia}::{_tp}"
            if _cl not in _topic_stats:
                _topic_stats[_cl] = {"materia": materia, "topic": _tp, "intentos": 0, "correctas": 0}
            _topic_stats[_cl]["intentos"] += 1
            if r['correcto']: _topic_stats[_cl]["correctas"] += 1
        save_session(nombre, _exam_score, materia, materia, "Difícil",
                     modo='examen', preguntas_fallidas=_fallidas, topic_stats_sesion=_topic_stats)
        st.session_state.exam_session_saved = True

    if pct >= 80:
        st.markdown('<div class="confetti">🎉🌟🏆🌟🎉</div>', unsafe_allow_html=True)
        st.balloons()

    st.markdown(f'<div class="hero" style="font-size:2rem;">{info["emoji"]} Resultados del Examen — {materia}</div>', unsafe_allow_html=True)
    score_cls = "score-green" if pct >= 80 else ("score-yellow" if pct >= 60 else "score-red")
    nota = "A" if pct >= 90 else ("B" if pct >= 80 else ("C" if pct >= 70 else ("D" if pct >= 60 else "F")))
    st.markdown(f"""
    <div class="score-box {score_cls}">
        <div class="score-num">{pct}%</div>
        <div style="font-size:1.5rem; font-weight:bold;">Nota: {nota}</div>
        <div style="font-size:1.1rem;">✅ {correctas} correctas &nbsp;|&nbsp; ❌ {total-correctas-vacias} incorrectas &nbsp;|&nbsp; ⬜ {vacias} sin responder</div>
    </div>
    """, unsafe_allow_html=True)

    if pct >= 90:   st.success(f"🌟 ¡EXCELENTE {nombre}! ¡Dominas esta materia! 🧠✨")
    elif pct >= 80: st.success(f"😊 ¡Muy bien {nombre}! Casi perfecto. 💪")
    elif pct >= 60: st.warning(f"🤔 Vas bien {nombre}, pero hay preguntas que repasar. 📖")
    else:           st.error(f"📚 {nombre}, necesitas practicar más. ¡Cada intento te hace mejor! 💪")

    st.write("")
    st.markdown("### 📋 Corrección del Examen")
    for i, r in enumerate(resultados):
        opciones = r['opciones']
        correcta = r['respuesta_correcta']
        seleccionada = r['seleccionada']
        letra_correcta = next((LETRAS[j] for j, o in enumerate(opciones)
                                if check_answer({'answer': correcta, 'is_numeric': False}, o)), "?")
        letra_sel = next((LETRAS[j] for j, o in enumerate(opciones) if o == seleccionada), "?") if seleccionada else None
        if r['correcto']:       css, icono = "exam-result-correct", "✅"
        elif seleccionada is None: css, icono = "exam-result-empty", "⬜"
        else:                   css, icono = "exam-result-wrong", "❌"
        opciones_html = " &nbsp; ".join(
            f"<b style='color:#28a745;'>[X] {LETRAS[j]}) {o}</b>" if o == correcta else
            (f"<s style='color:#dc3545;'>{LETRAS[j]}) {o}</s>" if o == seleccionada else f"{LETRAS[j]}) {o}")
            for j, o in enumerate(opciones))
        detalle = ("" if r['correcto'] else
                   f"<br><span style='font-size:0.85rem; color:#666;'>Marcaste: <b>{letra_sel}) {seleccionada}</b> → Correcta: <b>{letra_correcta}) {correcta}</b></span>"
                   if seleccionada else
                   f"<br><span style='font-size:0.85rem; color:#666;'>Sin responder. Correcta: <b>{letra_correcta}) {correcta}</b></span>")
        st.markdown(f"""
        <div class="{css}">
            <b>{icono} {i+1}. {r['pregunta']}</b><br>
            <span style="font-size:0.9rem;">{opciones_html}</span>{detalle}
        </div>
        """, unsafe_allow_html=True)
        if r.get('procedure') and not r['correcto']:
            with st.expander(f"📐 Ver explicación — pregunta {i+1}"):
                st.markdown(r['procedure'])

    _malas = [r for r in resultados if not r['correcto'] and r['seleccionada'] is not None]
    if _malas and st.session_state.get('exam_session_saved'):
        st.write("")
        st.markdown(f"""
        <div class="card card-orange" style="text-align:center;">
            <div style="font-size:1.8rem;">✏️</div>
            <div style="font-size:1.15rem; font-weight:bold; margin:6px 0;">Ronda de corrección — {len(_malas)} preguntas incorrectas</div>
            <div style="font-size:0.95rem; color:#555;">Respóndelas bien y ganas <b>25 XP</b> por cada una.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("✏️ Iniciar ronda de corrección", type="primary", use_container_width=True):
            st.session_state.correction_questions = _malas
            st.session_state.correction_idx = 0
            st.session_state.correction_xp = 0
            st.session_state.correction_results = []
            st.session_state.correction_answered = False
            st.session_state.correction_last_correct = None
            st.session_state.phase = 'exam_correction'
            st.rerun()

    st.write("")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🔄 Hacer otro examen", type="primary"):
            st.session_state.phase = 'config'; st.session_state.exam_submitted = False; st.rerun()
    with c2:
        if st.button("📚 Otra materia"):
            st.session_state.phase = 'materias'; st.rerun()
    with c3:
        if st.button("🏠 Inicio"):
            go_home_fn(); st.rerun()


def render_exam_correction(lang="es"):
    nombre = st.session_state.student
    info = ESTUDIANTES[nombre]
    cqs = st.session_state.correction_questions
    cidx = st.session_state.correction_idx

    if cidx >= len(cqs):
        st.session_state.phase = 'exam_correction_done'; st.rerun()

    r = cqs[cidx]
    total_cq = len(cqs)
    st.markdown(f'<div class="hero" style="font-size:1.8rem;">{info["emoji"]} Ronda de Corrección</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="exam-header">
        <h2>✏️ Pregunta {cidx + 1} de {total_cq}</h2>
        <p>Respóndela bien → <b style="color:#f39c12;">+25 XP</b> &nbsp;|&nbsp; Incorrecta → 0 XP</p>
    </div>
    """, unsafe_allow_html=True)
    st.progress(cidx / total_cq)

    if r.get('seleccionada'):
        st.markdown(f"""<div style="background:#fff3cd; border-left:4px solid #ffc107; border-radius:10px;
            padding:10px 15px; margin-bottom:10px; font-size:0.92rem; color:#856404;">
            ⚠️ La vez anterior respondiste: <b>{r['seleccionada']}</b> — ¡estaba incorrecto!</div>""",
            unsafe_allow_html=True)

    st.markdown(f'<div class="exam-pregunta"><div class="texto">❓ {r["pregunta"]}</div></div>', unsafe_allow_html=True)
    if r.get('imagen'): st.image(r['imagen'])
    if r.get('imagen2'): st.image(r['imagen2'])

    if st.session_state.get('correction_answered'):
        fue_correcto = st.session_state.correction_last_correct
        if fue_correcto:
            st.markdown("""<div style="background:#d4edda; border-left:5px solid #28a745; border-radius:10px;
                padding:14px 18px; text-align:center; font-size:1.2rem; font-weight:bold; color:#155724;">
                ✅ ¡Correcto! +25 XP</div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div style="background:#f8d7da; border-left:5px solid #dc3545; border-radius:10px;
                padding:14px 18px; text-align:center; font-size:1.1rem; font-weight:bold; color:#721c24;">
                ❌ Incorrecto — 0 XP<br>
                <span style="font-size:0.95rem; font-weight:normal;">Correcta: <b>{r['respuesta_correcta']}</b></span>
                </div>""", unsafe_allow_html=True)
        lbl = "➡️ Siguiente" if cidx + 1 < total_cq else "🏁 Ver resumen"
        if st.button(lbl, type="primary", use_container_width=True):
            st.session_state.correction_idx += 1
            st.session_state.correction_answered = False
            st.session_state.correction_last_correct = None
            st.rerun()
    else:
        op_labels = [f"{LETRAS[j]}) {o}" for j, o in enumerate(r['opciones'])]
        sel = st.radio("Selecciona la respuesta correcta:", op_labels, index=None, key=f"corr_radio_{cidx}")
        if st.button("✅ Confirmar respuesta", type="primary", use_container_width=True, disabled=(sel is None)):
            idx_sel = op_labels.index(sel) if sel else -1
            texto_sel = r['opciones'][idx_sel] if idx_sel >= 0 else ""
            fue_correcto = check_answer({'answer': r['respuesta_correcta'], 'is_numeric': r.get('is_numeric', False)}, texto_sel)
            xp = 25 if fue_correcto else 0
            st.session_state.correction_xp += xp
            st.session_state.correction_results.append({
                "pregunta": r['pregunta'], "correcto": fue_correcto, "xp_ganado": xp,
                "respuesta_dada": texto_sel, "respuesta_correcta": r['respuesta_correcta'],
            })
            st.session_state.correction_answered = True
            st.session_state.correction_last_correct = fue_correcto
            st.rerun()


def render_exam_correction_done(go_home_fn, lang="es"):
    nombre = st.session_state.student
    info = ESTUDIANTES[nombre]
    materia = st.session_state.materia
    cresults = st.session_state.get('correction_results', [])
    total_xp = st.session_state.get('correction_xp', 0)
    total_cq = len(cresults)
    bien = sum(1 for c in cresults if c['correcto'])

    if not st.session_state.get('correction_xp_saved'):
        add_correction_xp(nombre, total_xp, materia)
        st.session_state.correction_xp_saved = True

    if bien == total_cq and total_cq > 0:
        st.markdown('<div class="confetti">🎉✨🎉</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="hero" style="font-size:1.8rem;">{info["emoji"]} Corrección completada</div>', unsafe_allow_html=True)
    pct = int(100 * bien / total_cq) if total_cq else 0
    score_cls = "score-green" if pct >= 70 else ("score-yellow" if pct >= 40 else "score-red")
    st.markdown(f"""
    <div class="score-box {score_cls}">
        <div class="score-num">+{total_xp} XP</div>
        <div style="font-size:1.3rem; font-weight:bold;">✅ {bien} de {total_cq} corregidas correctamente</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Resumen de correcciones")
    for c in cresults:
        if c['correcto']:
            st.markdown(f'<div class="exam-result-correct">✅ <b>+25 XP</b> — {c["pregunta"][:100]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f"""<div class="exam-result-wrong">❌ <b>0 XP</b> — {c['pregunta'][:100]}<br>
                <span style="font-size:0.85rem;">Respondiste: <b>{c['respuesta_dada']}</b> → Correcta: <b>{c['respuesta_correcta']}</b></span>
                </div>""", unsafe_allow_html=True)

    st.write("")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔄 Nuevo examen", type="primary"):
            st.session_state.phase = 'config'; st.session_state.exam_submitted = False; st.rerun()
    with c2:
        if st.button("🏠 Inicio"):
            go_home_fn(); st.rerun()
