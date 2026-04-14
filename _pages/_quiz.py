"""Página: Quiz infinito."""
import re
import time
import streamlit as st
import streamlit.components.v1 as components
from utils import check_answer
from scoring import record_answer, get_level, get_rank


def _tts_abby(texto, opciones=None, counter=0):
    limpio = re.sub(r'\*+', '', texto)
    limpio = re.sub(r'[_~`#]', '', limpio)
    limpio = re.sub(r'[^\w\s¿?¡!áéíóúüñÁÉÍÓÚÜÑ,.\-:()]', ' ', limpio)
    limpio = re.sub(r'\s+', ' ', limpio).strip()
    if opciones:
        ops = [re.sub(r'[^\w\s¿?¡!áéíóúüñÁÉÍÓÚÜÑ,.\-]', ' ', o).strip() for o in opciones]
        limpio += ". Las opciones son: " + ". ".join(ops)
    limpio_js = limpio.replace('\\', '').replace('"', "'")
    components.html(f"""
    <script>
    (function(){{
        var _tick = {counter};
        if (!window.speechSynthesis) return;
        window.speechSynthesis.cancel();
        var u = new SpeechSynthesisUtterance("{limpio_js}");
        u.lang = 'es-MX'; u.rate = 0.82; u.pitch = 1.15;
        function speak() {{
            var voices = window.speechSynthesis.getVoices();
            var es = voices.find(function(v) {{ return v.lang.startsWith('es'); }});
            if (es) u.voice = es;
            window.speechSynthesis.speak(u);
        }}
        if (window.speechSynthesis.getVoices().length > 0) {{ speak(); }}
        else {{ window.speechSynthesis.onvoiceschanged = speak; }}
    }})();
    </script>
    """, height=0, scrolling=False)


def render(lang="es"):
    q = st.session_state.current_q
    sc = st.session_state.score
    level, level_xp, level_needed = get_level(sc['xp'])
    rank = get_rank(sc['xp'])

    if st.session_state.q_start is None:
        st.session_state.q_start = time.time()
        st.session_state.answered = False
        st.session_state.last_correct = None

    elapsed = time.time() - st.session_state.q_start
    remaining = max(0, st.session_state.timer - elapsed)

    st.markdown(f"""
    <div class="quiz-stats">
        <span>⭐ {sc['xp']} XP</span>
        <span>💪 x{sc['multiplier']}</span>
        <span>🔥 {sc['streak']} racha</span>
        <span>🏅 Nv.{level}</span>
    </div>
    """, unsafe_allow_html=True)

    if st.button("📊 Terminar", key="stop_top", use_container_width=True):
        st.session_state.phase = 'results'
        st.rerun()

    st.progress(level_xp / level_needed, text=f"{rank} — {level_xp}/{level_needed} XP para Nv.{level+1}")

    timer_cls = "timer-ok" if remaining > 10 else ("timer-warn" if remaining > 5 else "timer-danger")
    st.markdown(f'<div class="timer {timer_cls}">⏱️ {int(remaining)}s</div>', unsafe_allow_html=True)
    st.progress(remaining / st.session_state.timer)

    st.markdown(f'<span class="badge badge-{hash(q["topic"])%7+1}">{q["topic"]}</span> <span class="badge badge-5">#{sc["total"]+1}</span>', unsafe_allow_html=True)
    st.markdown(f'<div class="kahoot-q">{q["question"]}</div>', unsafe_allow_html=True)

    if not st.session_state.answered:
        if not q.get('imagen2') and q.get('imagen'):
            try: st.image(q['imagen'], use_container_width=True)
            except: pass
        if q.get('texto_comparar'):
            st.markdown(f"""<div style="background:#f0f0ff; border-left:4px solid #9b59b6;
                padding:12px 16px; border-radius:10px; margin:8px 0;
                font-size:1rem; font-style:italic; color:#333;">{q['texto_comparar']}</div>""",
                unsafe_allow_html=True)
        if st.session_state.student == 'ABBY':
            _handle_tts(q, sc)

    if not st.session_state.answered:
        _render_answer_buttons(q, sc, remaining)
    else:
        _render_feedback(q, sc)


def _handle_tts(q, sc):
    _qid_now = q.get('_qid', hash(q['question']))
    _should_speak = False
    if _qid_now != st.session_state.get('last_spoken_qid'):
        _should_speak = True
        st.session_state.last_spoken_qid = _qid_now
        st.session_state.force_speak = False
    elif st.session_state.get('force_speak'):
        _should_speak = True
        st.session_state.force_speak = False
        st.session_state.speak_counter = st.session_state.get('speak_counter', 0) + 1
    if _should_speak:
        _ops_tts = [] if q.get('imagen2') else q.get('opciones_btn', [])
        _tts_abby(q['question'], _ops_tts, counter=st.session_state.get('speak_counter', 0))
    if st.button("🔊 Escuchar pregunta de nuevo", key=f"tts_replay_{sc['total']}"):
        st.session_state.force_speak = True
        st.rerun()


def _submit(q, sc, ans):
    elapsed_f = time.time() - st.session_state.q_start
    qid = q.get('_qid', hash(q['question']))
    correct = check_answer(q, ans)
    respondio = str(ans).strip() != ''
    gained = record_answer(sc, qid, correct and respondio,
                           tiempo_seg=elapsed_f, timer_total=st.session_state.timer,
                           dificultad=st.session_state.get('dificultad', 'Normal'))
    st.session_state.last_gained = gained
    st.session_state.last_correct = correct and respondio
    st.session_state.last_time = elapsed_f
    st.session_state.answered = True

    _materia = st.session_state.get('materia', '')
    _topic = q.get('topic', '')
    _clave = f"{_materia}::{_topic}"
    _ts = st.session_state.setdefault('topic_stats', {})
    if _clave not in _ts:
        _ts[_clave] = {"materia": _materia, "topic": _topic, "intentos": 0, "correctas": 0}
    _ts[_clave]["intentos"] += 1
    if correct and respondio:
        _ts[_clave]["correctas"] += 1
    elif respondio:
        st.session_state.setdefault('wrong_questions', []).append({
            "fecha": time.strftime("%d/%m/%Y"),
            "materia": _materia, "topic": _topic,
            "pregunta": q.get('question', ''),
            "respuesta_dada": str(ans),
            "respuesta_correcta": q.get('answer', ''),
        })


def _render_answer_buttons(q, sc, remaining):
    opciones = q.get('opciones_btn', [])
    if q.get('imagen2') and set(opciones) == {"Imagen 1", "Imagen 2"}:
        _key_base = f"{sc['total']}_{hash(q.get('question',''))%10000}"
        ci1, ci2 = st.columns(2)
        with ci1:
            try: st.image(q['imagen'], use_container_width=True)
            except: pass
            if st.button("✓ Esta imagen", key=f"opt_{_key_base}_0", type="primary", use_container_width=True):
                _submit(q, sc, "Imagen 1"); st.rerun()
        with ci2:
            try: st.image(q['imagen2'], use_container_width=True)
            except: pass
            if st.button("✓ Esta imagen", key=f"opt_{_key_base}_1", type="primary", use_container_width=True):
                _submit(q, sc, "Imagen 2"); st.rerun()
    else:
        n_opts = len(opciones)
        # Usar un key basado en total+hash para evitar duplicados en reruns
        _key_base = f"{sc['total']}_{hash(q.get('question',''))%10000}"
        for i_btn in range(0, n_opts, 2):
            row = opciones[i_btn:i_btn+2]
            cols = st.columns(len(row))
            for j, opcion in enumerate(row):
                with cols[j]:
                    if st.button(opcion, key=f"opt_{_key_base}_{i_btn+j}", type="primary", use_container_width=True):
                        _submit(q, sc, opcion); st.rerun()

    if remaining <= 0 and not st.session_state.answered:
        _submit(q, sc, ""); st.rerun()
    elif not st.session_state.answered:
        time.sleep(1); st.rerun()


def _render_feedback(q, sc):
    if q.get('imagen2'):
        c1, c2 = st.columns(2)
        with c1:
            try: st.image(q['imagen'], use_container_width=True)
            except: pass
        with c2:
            try: st.image(q['imagen2'], use_container_width=True)
            except: pass
    elif q.get('imagen'):
        try: st.image(q['imagen'], use_container_width=True)
        except: pass
    if q.get('texto_comparar'):
        st.markdown(f"""<div style="background:#f0f0ff; border-left:4px solid #9b59b6;
            padding:12px 16px; border-radius:10px; margin:8px 0;
            font-size:1rem; font-style:italic; color:#333;">{q['texto_comparar']}</div>""",
            unsafe_allow_html=True)

    correct = st.session_state.last_correct
    gained = st.session_state.last_gained
    if correct:
        st.markdown('<div class="confetti">🎉🌟🎉</div>', unsafe_allow_html=True)
        t = st.session_state.get('last_time', 0)
        st.success(f"¡Correcto! **+{gained} XP** — x{sc['multiplier']} 🔥 ({t:.1f}s)")
    else:
        st.error(f"❌ Incorrecto — **{gained} XP** 💔 multiplicador vuelve a x1")
        st.markdown(f'<div class="result-wrong"><b>Respuesta correcta:</b> {q["answer"]}</div>', unsafe_allow_html=True)
    if q.get('procedure'):
        with st.expander("📐 Ver procedimiento"):
            st.markdown(q['procedure'])

    col1, col2 = st.columns(2)
    with col1:
        if st.button("➡️ Siguiente pregunta", type="primary", use_container_width=True):
            st.session_state.current_q = st.session_state.gen.next()
            st.session_state.q_start = None
            st.session_state.answered = False
            st.rerun()
    with col2:
        if st.button("📊 Terminar y ver resultados", use_container_width=True):
            st.session_state.phase = 'results'
            st.rerun()
