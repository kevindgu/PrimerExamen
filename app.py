import streamlit as st
import streamlit.components.v1 as components
import random
import re
import time
from utils import ESTUDIANTES, DIFICULTADES, check_answer
from scoring import new_score, record_answer, get_level, get_rank
from infinite import InfiniteGenerator
from leaderboard import (save_session, get_ranking, get_ranking_dificultad, get_ranking_materia,
                         get_temas_stats, get_preguntas_debiles,
                         get_player, LOGROS, DIFICULTADES_ORDEN, MATERIAS_ORDEN)
from musica import MUSIC_HTML

st.set_page_config(page_title="🧮 MatePlay", page_icon="🧮", layout="centered")

# --- CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Nunito:wght@400;700&display=swap');
.main { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
.block-container { max-width: 800px; padding-left: 1rem !important; padding-right: 1rem !important; }
h1, h2, h3 { font-family: 'Fredoka One', cursive !important; }
p, li, label, .stMarkdown { font-family: 'Nunito', sans-serif !important; }

.card { background: white; border-radius: 20px; padding: 25px; margin: 15px 0; box-shadow: 0 8px 25px rgba(0,0,0,0.15); color: #2c3e50; }
.card-purple { border-left: 6px solid #9b59b6; }
.card-blue { border-left: 6px solid #3498db; }
.card-green { border-left: 6px solid #2ecc71; }
.card-orange { border-left: 6px solid #f39c12; }
.card-red { border-left: 6px solid #e74c3c; }

.hero { text-align: center; padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 50%, #ffd200 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 3.5rem; font-family: 'Fredoka One', cursive; margin-bottom: 0; }
.hero-sub { text-align: center; font-size: 1.3rem; color: #ddd; margin-top: 0; }

.score-box { text-align: center; padding: 30px; border-radius: 20px; margin: 20px 0; color: #2c3e50; }
.score-green { background: linear-gradient(135deg, #a8edea, #fed6e3); }
.score-yellow { background: linear-gradient(135deg, #ffecd2, #fcb69f); }
.score-red { background: linear-gradient(135deg, #ff9a9e, #fecfef); }
.score-num { font-size: 4rem; font-weight: bold; font-family: 'Fredoka One', cursive; }

.kahoot-q { background: linear-gradient(135deg, #6c5ce7, #a29bfe); color: white; padding: 30px; border-radius: 20px; text-align: center; font-size: 1.4rem; font-weight: bold; margin: 15px 0; box-shadow: 0 5px 20px rgba(108,92,231,0.4); }

.timer { text-align: center; font-size: 2.5rem; font-family: 'Fredoka One', cursive; }
.timer-ok { color: #2ecc71; }
.timer-warn { color: #f39c12; }
.timer-danger { color: #e74c3c; animation: pulse 0.5s infinite; }
@keyframes pulse { 0%,100% { opacity:1; } 50% { opacity:0.5; } }

.badge { display: inline-block; padding: 5px 15px; border-radius: 20px; font-size: 0.85rem; font-weight: bold; color: white; margin-bottom: 10px; }
.badge-1 { background: #e74c3c; } .badge-2 { background: #3498db; } .badge-3 { background: #2ecc71; }
.badge-4 { background: #f39c12; } .badge-5 { background: #9b59b6; } .badge-6 { background: #1abc9c; } .badge-7 { background: #e67e22; }

div.stButton > button { border-radius: 15px !important; font-family: 'Nunito', sans-serif !important; font-weight: 700 !important; font-size: 1rem !important; padding: 10px 20px !important; transition: transform 0.2s !important; min-height: 48px !important; }
div.stButton > button:hover { transform: scale(1.05) !important; }

.nav-dot { display: inline-block; width: 35px; height: 35px; border-radius: 50%; text-align: center; line-height: 35px; margin: 3px; font-weight: bold; font-size: 0.8rem; }
.nav-done { background: #2ecc71; color: white; }
.nav-empty { background: #ddd; color: #666; }
.nav-current { background: #6c5ce7; color: white; box-shadow: 0 0 10px #6c5ce7; }

.result-correct { background: #d4edda; border-left: 5px solid #28a745; padding: 10px 15px; border-radius: 10px; margin: 5px 0; color: #155724; }
.result-wrong { background: #f8d7da; border-left: 5px solid #dc3545; padding: 10px 15px; border-radius: 10px; margin: 5px 0; color: #721c24; }

.confetti { text-align: center; font-size: 3rem; animation: bounce 1s infinite; }
@keyframes bounce { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-20px); } }

.student-card { text-align: center; padding: 30px 15px; border-radius: 25px; cursor: pointer; transition: transform 0.3s; min-height: 180px; }
.student-card:hover { transform: scale(1.05); }

.stImage img { max-height: 300px !important; object-fit: contain !important; margin: 0 auto !important; display: block !important; }

/* Stats bar del quiz */
.quiz-stats { display: flex; flex-wrap: wrap; gap: 6px; justify-content: center; background: white; border-radius: 15px; padding: 10px 12px; margin-bottom: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); color: #2c3e50; }
.quiz-stats span { font-family: 'Nunito', sans-serif; font-size: 0.9rem; font-weight: 700; padding: 4px 10px; background: #f4f4f8; border-radius: 20px; color: #333; white-space: nowrap; }

/* Stats de resultados en fila */
.stats-row { display: flex; gap: 10px; margin: 15px 0; flex-wrap: wrap; }
.stat-item { flex: 1 1 80px; text-align: center; padding: 15px 10px; border-radius: 15px; background: white; box-shadow: 0 4px 12px rgba(0,0,0,0.1); color: #2c3e50; }
.stat-item h3 { font-family: 'Fredoka One', cursive; font-size: 1.6rem; margin: 0 0 4px 0; color: inherit; }
.stat-item p { font-size: 0.8rem; color: #666; margin: 0; font-family: 'Nunito', sans-serif; }
.stat-orange { border-top: 5px solid #f39c12; }
.stat-purple { border-top: 5px solid #9b59b6; }
.stat-blue   { border-top: 5px solid #3498db; }

/* Ocultar menú de Streamlit y botón Stop */
#MainMenu { visibility: hidden !important; }
header[data-testid="stHeader"] { visibility: hidden !important; }
footer { visibility: hidden !important; }
[data-testid="stToolbar"] { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }
[data-testid="stStatusWidget"] { display: none !important; }

/* ── MODO EXAMEN ── */
.exam-header { background: white; border-radius: 20px; padding: 20px 25px; margin-bottom: 18px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 6px solid #2c3e50; color: #2c3e50; }
.exam-header h2 { font-family: 'Fredoka One', cursive; color: #2c3e50; margin: 0 0 4px 0; font-size: 1.6rem; }
.exam-header p { color: #555; margin: 0; font-size: 0.95rem; font-family: 'Nunito', sans-serif; }
.exam-instrucciones { background: #fff9e6; border: 2px dashed #f39c12; border-radius: 12px; padding: 12px 18px; margin-bottom: 18px; font-family: 'Nunito', sans-serif; font-size: 0.95rem; color: #7d6608; }
.exam-pregunta { background: white; border-radius: 15px; padding: 20px 22px; margin: 12px 0; box-shadow: 0 3px 12px rgba(0,0,0,0.08); border-left: 5px solid #6c5ce7; color: #2c3e50; }
.exam-pregunta .num { font-family: 'Fredoka One', cursive; color: #6c5ce7; font-size: 1.1rem; }
.exam-pregunta .texto { font-family: 'Nunito', sans-serif; font-size: 1.05rem; font-weight: 700; color: #2c3e50; margin: 6px 0 14px 0; }
.exam-result-correct { background: #d4edda; border-left: 5px solid #28a745; padding: 12px 16px; border-radius: 10px; margin: 5px 0; font-family: 'Nunito', sans-serif; color: #155724; }
.exam-result-wrong { background: #f8d7da; border-left: 5px solid #dc3545; padding: 12px 16px; border-radius: 10px; margin: 5px 0; font-family: 'Nunito', sans-serif; color: #721c24; }
.exam-result-empty { background: #fff3cd; border-left: 5px solid #ffc107; padding: 12px 16px; border-radius: 10px; margin: 5px 0; font-family: 'Nunito', sans-serif; color: #856404; }

/* ── MOBILE ── */
@media (max-width: 768px) {
    .hero { font-size: 2.2rem !important; padding: 12px 8px !important; }
    .hero-sub { font-size: 1rem !important; }
    .kahoot-q { font-size: 1.1rem !important; padding: 18px 14px !important; }
    .timer { font-size: 2rem !important; }
    .score-num { font-size: 2.8rem !important; }
    .score-box { padding: 18px 12px !important; }
    .card { padding: 14px !important; margin: 8px 0 !important; }
    .student-card { min-height: auto !important; padding: 14px 8px !important; }
    .student-card h2 { font-size: 1.2rem !important; }
    div.stButton > button { font-size: 1rem !important; padding: 12px 8px !important; min-height: 52px !important; }
    .stat-item h3 { font-size: 1.3rem !important; }
    .stImage img { max-height: 200px !important; }
    .block-container { padding-top: 1rem !important; }
}
</style>
""", unsafe_allow_html=True)

# --- Estado ---
if 'phase' not in st.session_state:
    st.session_state.phase = 'students'
    st.session_state.student = None
    st.session_state.materia = None
    st.session_state.mode = 'normal'
    st.session_state.questions = []
    st.session_state.answers = {}
    st.session_state.idx = 0
    st.session_state.kahoot_start = None
    st.session_state.kahoot_times = {}
    st.session_state.kahoot_streak = 0
    st.session_state.kahoot_score = 0
    st.session_state.kahoot_answered = False
    st.session_state.music_on = False
    st.session_state.last_spoken_qid = None
    st.session_state.speak_counter = 0
    st.session_state.force_speak = False

if 'music_on' not in st.session_state:
    st.session_state.music_on = False

# ===================== MÚSICA GLOBAL (siempre arriba) =====================
if st.session_state.music_on:
    st.iframe(MUSIC_HTML, height=1)

_music_label = "🔇 Silenciar música" if st.session_state.music_on else "🎵 Música"
if st.button(_music_label, key="music_global"):
    st.session_state.music_on = not st.session_state.music_on
    st.rerun()

def reset():
    music_pref = st.session_state.get('music_on', False)
    for k in list(st.session_state.keys()):
        del st.session_state[k]
    st.session_state.phase = 'students'
    st.session_state.music_on = music_pref

def go_home():
    reset()


def _tts_abby(texto, opciones=None, counter=0):
    """Lee la pregunta en voz alta usando el Web Speech API del navegador."""
    # Limpiar markdown y emojis para que suene natural
    limpio = re.sub(r'\*+', '', texto)
    limpio = re.sub(r'[_~`#]', '', limpio)
    limpio = re.sub(r'[^\w\s¿?¡!áéíóúüñÁÉÍÓÚÜÑ,.\-:()]', ' ', limpio)
    limpio = re.sub(r'\s+', ' ', limpio).strip()
    if opciones:
        ops = [re.sub(r'[^\w\s¿?¡!áéíóúüñÁÉÍÓÚÜÑ,.\-]', ' ', o).strip() for o in opciones]
        limpio += ". Las opciones son: " + ". ".join(ops)
    # Escapar comillas para JS
    limpio_js = limpio.replace('\\', '').replace('"', "'")
    components.html(f"""
    <script>
    (function(){{
        var _tick = {counter};
        if (!window.speechSynthesis) return;
        window.speechSynthesis.cancel();
        var u = new SpeechSynthesisUtterance("{limpio_js}");
        u.lang = 'es-MX';
        u.rate = 0.82;
        u.pitch = 1.15;
        // Si las voces todavía no cargaron, esperar
        function speak() {{
            var voices = window.speechSynthesis.getVoices();
            var es = voices.find(function(v) {{ return v.lang.startsWith('es'); }});
            if (es) u.voice = es;
            window.speechSynthesis.speak(u);
        }}
        if (window.speechSynthesis.getVoices().length > 0) {{
            speak();
        }} else {{
            window.speechSynthesis.onvoiceschanged = speak;
        }}
    }})();
    </script>
    """, height=0, scrolling=False)


# ===================== SELECCIÓN DE ESTUDIANTE =====================
if st.session_state.phase == 'students':
    st.markdown('<div class="hero">🏫 MatePlay</div>', unsafe_allow_html=True)
    st.markdown('<p class="hero-sub">¡Aprende jugando! ¿Quién va a practicar? 🎮✨</p>', unsafe_allow_html=True)
    st.write("")

    if st.button("🏆 Ver tabla de puntuaciones", width='stretch'):
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

# ===================== SELECCIÓN DE MATERIA =====================
elif st.session_state.phase == 'materias':
    nombre = st.session_state.student
    info = ESTUDIANTES[nombre]
    st.markdown(f'<div class="hero" style="font-size:2.5rem;">{info["emoji"]} ¡Hola {nombre}!</div>', unsafe_allow_html=True)
    st.markdown(f'<p class="hero-sub">¿Qué materia quieres practicar?</p>', unsafe_allow_html=True)
    st.write("")

    materias = info['materias']
    cols = st.columns(max(len(materias), 1))
    for i, (mat_nombre, mat_info) in enumerate(materias.items()):
        with cols[i % len(cols)]:
            st.markdown(f"""
            <div class="card card-blue" style="text-align:center;">
                <div style="font-size:3rem;">{mat_info['emoji']}</div>
                <h3>{mat_nombre}</h3>
                <p>{len(mat_info['topics'])} temas disponibles</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"{mat_info['emoji']} {mat_nombre}", key=f"mat_{mat_nombre}", type="primary"):
                st.session_state.materia = mat_nombre
                st.session_state.phase = 'menu'
                st.rerun()

    st.write("")
    if st.button("⬅️ Cambiar estudiante"):
        go_home()
        st.rerun()

# ===================== MENÚ MODO =====================
elif st.session_state.phase == 'menu':
    nombre = st.session_state.student
    info = ESTUDIANTES[nombre]
    materia = st.session_state.materia
    st.markdown(f'<div class="hero" style="font-size:2.2rem;">{info["emoji"]} {nombre} — {materia}</div>', unsafe_allow_html=True)
    st.session_state.phase = 'config'
    st.rerun()

# ===================== CONFIGURACIÓN =====================
elif st.session_state.phase == 'config':
    nombre = st.session_state.student
    info = ESTUDIANTES[nombre]
    materia = st.session_state.materia
    mat_info = info['materias'][materia]
    topics = mat_info['topics']

    st.markdown(f'<div class="hero" style="font-size:2rem;">{info["emoji"]} {nombre} — {materia}</div>', unsafe_allow_html=True)

    st.markdown('<div class="card card-blue">', unsafe_allow_html=True)
    temas = st.multiselect("📚 Elige los temas:", list(topics.keys()), default=list(topics.keys()))

    dif_emojis = {
        "Fácil": "🟢 Fácil", "Normal": "🟡 Normal", "Difícil": "🔴 Difícil",
        "💀 Super Difícil": "💀 Super Difícil", "☠️ Mega Difícil": "☠️ Mega Difícil",
    }
    dif_sel = st.radio("💪 Dificultad:", DIFICULTADES, index=1, horizontal=True, format_func=lambda x: dif_emojis[x])

    default_time = {"Fácil": 30, "Normal": 20, "Difícil": 45, "💀 Super Difícil": 15, "☠️ Mega Difícil": 10}[dif_sel]
    if dif_sel in ("💀 Super Difícil", "☠️ Mega Difícil"):
        timer = default_time
        st.info(f"⏱️ Tiempo fijo: **{timer} segundos** — bloqueado en este modo.")
    else:
        timer = st.select_slider("⏱️ Segundos por pregunta:", options=[10, 15, 20, 30, 45, 60, 90], value=default_time)
    st.markdown('</div>', unsafe_allow_html=True)

    col_modos = st.columns(2)
    with col_modos[0]:
        st.markdown("""
        <div class="card card-orange" style="text-align:center;">
            <h3>♾️ Modo Infinito</h3>
            <p>Las preguntas no se repiten. ¡Acumula XP y sube de nivel!</p>
            <p>🔥 Cada acierto sube tu multiplicador: x2, x3, x4...</p>
            <p>❌ Si fallas, el multiplicador vuelve a x1</p>
        </div>
        """, unsafe_allow_html=True)
    with col_modos[1]:
        st.markdown("""
        <div class="card card-blue" style="text-align:center;">
            <h3>📝 Modo Examen</h3>
            <p>Responde todas las preguntas y entrega al final.</p>
            <p>✏️ Selección única — Marque con X</p>
            <p>🔴 Siempre en dificultad <b>Difícil</b></p>
        </div>
        """, unsafe_allow_html=True)

    n_exam = st.select_slider("📝 Preguntas para el examen:", options=[5, 10, 15, 20, 25, 30], value=10)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⬅️ Volver"):
            st.session_state.phase = 'materias'
            st.rerun()
    with col2:
        if st.button("🚀 ¡A jugar!", type="primary"):
            if not temas:
                st.error("¡Elige al menos un tema! 📚")
            else:
                gen = InfiniteGenerator(mat_info['generator'], temas, dif_sel)
                first_q = gen.next()
                st.session_state.gen = gen
                st.session_state.current_q = first_q
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
                st.rerun()
    with col3:
        if st.button("📝 Modo Examen", type="secondary"):
            if not temas:
                st.error("¡Elige al menos un tema! 📚")
            else:
                # El examen siempre usa Difícil para mayor reto
                gen = InfiniteGenerator(mat_info['generator'], temas, "Difícil")
                preguntas_examen = [gen.next() for _ in range(n_exam)]
                st.session_state.exam_questions = preguntas_examen
                st.session_state.exam_submitted = False
                st.session_state.exam_results = None
                st.session_state.exam_session_saved = False
                st.session_state.dificultad = dif_sel
                st.session_state.current_topics = topics
                st.session_state.phase = 'exam'
                st.rerun()

# ===================== QUIZ INFINITO =====================
elif st.session_state.phase == 'quiz':
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

    # Stats bar compacta (funciona en móvil)
    st.markdown(f"""
    <div class="quiz-stats">
        <span>⭐ {sc['xp']} XP</span>
        <span>💪 x{sc['multiplier']}</span>
        <span>🔥 {sc['streak']} racha</span>
        <span>🏅 Nv.{level}</span>
    </div>
    """, unsafe_allow_html=True)

    if st.button("📊 Terminar", key="stop_top", width='stretch'):
        st.session_state.phase = 'results'
        st.rerun()

    # Barra de nivel
    st.progress(level_xp / level_needed, text=f"{rank} — {level_xp}/{level_needed} XP para Nv.{level+1}")

    # Timer
    timer_cls = "timer-ok" if remaining > 10 else ("timer-warn" if remaining > 5 else "timer-danger")
    st.markdown(f'<div class="timer {timer_cls}">⏱️ {int(remaining)}s</div>', unsafe_allow_html=True)
    st.progress(remaining / st.session_state.timer)

    # Pregunta
    st.markdown(f'<span class="badge badge-{hash(q["topic"])%7+1}">{q["topic"]}</span> <span class="badge badge-5">#{sc["total"]+1}</span>', unsafe_allow_html=True)
    st.markdown(f'<div class="kahoot-q">{q["question"]}</div>', unsafe_allow_html=True)

    # Imágenes (solo cuando no se ha respondido)
    # Las preguntas de comparar imagen2 se muestran directamente como botones abajo
    if not st.session_state.answered:
        if not q.get('imagen2') and q.get('imagen'):
            try: st.image(q['imagen'], width='stretch')
            except: pass

        # Texto de comparación (preguntas V/F y Sí/No con imagen)
        if q.get('texto_comparar'):
            st.markdown(f"""
            <div style="background:#f0f0ff; border-left:4px solid #9b59b6;
                        padding:12px 16px; border-radius:10px; margin:8px 0;
                        font-size:1rem; font-style:italic; color:#333;">
                {q['texto_comparar']}
            </div>""", unsafe_allow_html=True)

        # ── TTS para ABBY ──
        if st.session_state.student == 'ABBY':
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
                # Para imágenes no leer opciones (son "Imagen 1/2", no tiene sentido)
                _ops_tts = [] if q.get('imagen2') else q.get('opciones_btn', [])
                _tts_abby(q['question'], _ops_tts, counter=st.session_state.get('speak_counter', 0))
            if st.button("🔊 Escuchar pregunta de nuevo", key=f"tts_replay_{sc['total']}"):
                st.session_state.force_speak = True
                st.rerun()

    # --- RESPONDER ---
    if not st.session_state.answered:

        def _submit(ans):
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

            # ── Tracking de preguntas débiles y precisión por tema ──
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
                # Solo guardar si respondió algo (no tiempo vencido)
                st.session_state.setdefault('wrong_questions', []).append({
                    "fecha": time.strftime("%d/%m/%Y"),
                    "materia": _materia,
                    "topic": _topic,
                    "pregunta": q.get('question', ''),
                    "respuesta_dada": str(ans),
                    "respuesta_correcta": q.get('answer', ''),
                })

        opciones = q.get('opciones_btn', [])

        # Preguntas de comparar imágenes → las imágenes mismas son los botones
        if q.get('imagen2') and set(opciones) == {"Imagen 1", "Imagen 2"}:
            ci1, ci2 = st.columns(2)
            with ci1:
                try: st.image(q['imagen'], width='stretch')
                except: pass
                if st.button("✓ Esta imagen", key=f"opt_{sc['total']}_0", type="primary", width='stretch'):
                    _submit("Imagen 1")
                    st.rerun()
            with ci2:
                try: st.image(q['imagen2'], width='stretch')
                except: pass
                if st.button("✓ Esta imagen", key=f"opt_{sc['total']}_1", type="primary", width='stretch'):
                    _submit("Imagen 2")
                    st.rerun()
        else:
            cols = st.columns(2)
            for i_btn, opcion in enumerate(opciones):
                with cols[i_btn % 2]:
                    if st.button(opcion, key=f"opt_{sc['total']}_{i_btn}", type="primary", width='stretch'):
                        _submit(opcion)
                        st.rerun()

        # Timer expire
        if remaining <= 0 and not st.session_state.answered:
            _submit("")
            st.rerun()
        elif not st.session_state.answered:
            time.sleep(1)
            st.rerun()

    # --- RETROALIMENTACIÓN ---
    else:
        # Mostrar imagen y comparación también después de responder
        if q.get('imagen2'):
            c1, c2 = st.columns(2)
            with c1:
                try: st.image(q['imagen'], width='stretch')
                except: pass
            with c2:
                try: st.image(q['imagen2'], width='stretch')
                except: pass
        elif q.get('imagen'):
            try: st.image(q['imagen'], width='stretch')
            except: pass
        if q.get('texto_comparar'):
            st.markdown(f"""
            <div style="background:#f0f0ff; border-left:4px solid #9b59b6;
                        padding:12px 16px; border-radius:10px; margin:8px 0;
                        font-size:1rem; font-style:italic; color:#333;">
                {q['texto_comparar']}
            </div>""", unsafe_allow_html=True)

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
            if st.button("➡️ Siguiente pregunta", type="primary", width='stretch'):
                next_q = st.session_state.gen.next()
                st.session_state.current_q = next_q
                st.session_state.q_start = None
                st.session_state.answered = False
                st.rerun()
        with col2:
            if st.button("📊 Terminar y ver resultados", width='stretch'):
                st.session_state.phase = 'results'
                st.rerun()

# ===================== RESULTADOS =====================
elif st.session_state.phase == 'results':
    sc = st.session_state.score
    topics = st.session_state.get('current_topics', {})
    nombre = st.session_state.student
    info = ESTUDIANTES.get(nombre, {})
    materia = st.session_state.get('materia', '')
    level, level_xp, level_needed = get_level(sc['xp'])
    rank = get_rank(sc['xp'])

    # Guardar sesión y obtener logros nuevos
    if not st.session_state.get('session_saved'):
        temas_str = materia
        nuevos_logros = save_session(
            nombre, sc, materia, temas_str,
            st.session_state.get('dificultad', 'Normal'),
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

    # Score box
    score_cls = "score-green" if pct >= 80 else ("score-yellow" if pct >= 60 else "score-red")
    st.markdown(f"""
    <div class="score-box {score_cls}">
        <div style="font-size:2rem;">{rank}</div>
        <div class="score-num">{sc['xp']} XP</div>
        <div style="font-size:1.2rem;">Nivel <b>{level}</b> — {pct}% aciertos ({sc['correct']}/{sc['total']})</div>
    </div>
    """, unsafe_allow_html=True)

    # Stats en fila responsiva
    st.markdown(f"""
    <div class="stats-row">
        <div class="stat-item stat-orange"><h3>🔥 {sc['max_streak']}</h3><p>Racha máxima</p></div>
        <div class="stat-item stat-purple"><h3>💪 x{sc['max_multiplier']}</h3><p>Multiplicador máx</p></div>
        <div class="stat-item stat-blue"><h3>📝 {sc['total']}</h3><p>Preguntas vistas</p></div>
    </div>
    """, unsafe_allow_html=True)

    # Mensaje
    if nuevos_logros:
        st.markdown('<div class="card card-orange"><h3>🎉 ¡Nuevos logros desbloqueados!</h3></div>', unsafe_allow_html=True)
        for l in nuevos_logros:
            st.success(f"{l['emoji']} **{l['nombre']}** — {l['desc']}")

    if pct >= 90:
        st.success(f"🌟 ¡INCREÍBLE {nombre}! ¡Eres un genio! 🧠✨")
    elif pct >= 70:
        st.info(f"😊 ¡Muy bien {nombre}! Estás cerca de dominar estos temas. 💪")
    elif pct >= 50:
        st.warning(f"🤔 Vas avanzando {nombre}, pero hay temas que repasar. ¡Tú puedes! 📖")
    else:
        st.error(f"📚 {nombre}, necesitas practicar más. ¡Cada intento te hace mejor! 💪🌟")

    # Detalle por tema
    per_topic = {}
    for qid, correcto in sc['history']:
        # No tenemos el topic en history, usamos el score general
        pass

    st.write("")
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        if st.button("🔄 Jugar de nuevo", type="primary", width='stretch'):
            st.session_state.phase = 'config'
            st.session_state.session_saved = False
            st.rerun()
    with r1c2:
        if st.button("📚 Otra materia", width='stretch'):
            st.session_state.phase = 'materias'
            st.session_state.session_saved = False
            st.rerun()
    r2c1, r2c2 = st.columns(2)
    with r2c1:
        if st.button("🏆 Tabla de puntos", width='stretch'):
            st.session_state.phase = 'leaderboard'
            st.rerun()
    with r2c2:
        if st.button("🏠 Inicio", width='stretch'):
            go_home()
            st.rerun()

# ===================== EXAMEN — MARQUE CON X =====================
elif st.session_state.phase == 'exam':
    nombre = st.session_state.student
    info = ESTUDIANTES[nombre]
    materia = st.session_state.materia
    preguntas = st.session_state.exam_questions
    LETRAS = ["A", "B", "C", "D", "E", "F"]

    st.markdown(f"""
    <div class="exam-header">
        <h2>{info['emoji']} Examen — {materia}</h2>
        <p><b>Estudiante:</b> {nombre} &nbsp;|&nbsp; <b>Fecha:</b> {time.strftime('%d/%m/%Y')} &nbsp;|&nbsp; <b>Preguntas:</b> {len(preguntas)}</p>
    </div>
    <div class="exam-instrucciones">
        ✏️ <b>Instrucciones:</b> Marque con <b>X</b> la respuesta correcta. Solo puede seleccionar <b>una</b> opción por pregunta.
    </div>
    """, unsafe_allow_html=True)

    col_back, col_submit = st.columns([1, 2])
    with col_back:
        if st.button("⬅️ Cancelar"):
            st.session_state.phase = 'config'
            st.rerun()

    respuestas_seleccionadas = {}

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

            # Imagen(s) si existen
            if q.get('imagen2'):
                ci1, ci2 = st.columns(2)
                with ci1:
                    st.caption("Imagen 1")
                    try: st.image(q['imagen'], width='stretch')
                    except: pass
                with ci2:
                    st.caption("Imagen 2")
                    try: st.image(q['imagen2'], width='stretch')
                    except: pass
            elif q.get('imagen'):
                try: st.image(q['imagen'], width='stretch')
                except: pass

            if q.get('texto_comparar'):
                st.markdown(f"""
                <div style="background:#f0f0ff; border-left:4px solid #9b59b6;
                            padding:10px 14px; border-radius:8px; margin:6px 0;
                            font-size:0.95rem; font-style:italic; color:#333;">
                    {q['texto_comparar']}
                </div>""", unsafe_allow_html=True)

            sel = st.radio(
                label=f"q{i}",
                options=opciones_labeled,
                index=None,
                key=f"exam_radio_{i}",
                label_visibility="collapsed",
            )
            respuestas_seleccionadas[i] = sel
            st.write("")

        submitted = st.form_submit_button("📤 Entregar Examen", type="primary", use_container_width=True)

    if submitted:
        resultados = []
        for i, q in enumerate(preguntas):
            sel_labeled = respuestas_seleccionadas.get(i)
            if sel_labeled is None:
                respuesta_limpia = None
            else:
                # Quitar prefijo "A)  " para comparar
                respuesta_limpia = sel_labeled.split(")  ", 1)[-1].strip() if ")  " in sel_labeled else sel_labeled
            correcto = check_answer(q, respuesta_limpia) if respuesta_limpia else False
            resultados.append({
                "pregunta": q['question'],
                "topic": q.get('topic', ''),
                "opciones": q.get('opciones_btn', []),
                "respuesta_correcta": q['answer'],
                "seleccionada": respuesta_limpia,
                "correcto": correcto,
                "procedure": q.get('procedure', ''),
            })
        st.session_state.exam_results = resultados
        st.session_state.exam_submitted = True
        st.session_state.phase = 'exam_results'
        st.rerun()

# ===================== RESULTADOS DEL EXAMEN =====================
elif st.session_state.phase == 'exam_results':
    nombre = st.session_state.student
    info = ESTUDIANTES[nombre]
    materia = st.session_state.materia
    resultados = st.session_state.exam_results
    LETRAS = ["A", "B", "C", "D", "E", "F"]

    total = len(resultados)
    correctas = sum(1 for r in resultados if r['correcto'])
    vacias = sum(1 for r in resultados if r['seleccionada'] is None)
    pct = int(100 * correctas / total) if total else 0

    # ── Guardar examen en leaderboard (una sola vez) ──
    if not st.session_state.get('exam_session_saved'):
        # Calcular racha máxima
        _max_racha, _racha = 0, 0
        for r in resultados:
            if r['correcto']:
                _racha += 1
                _max_racha = max(_max_racha, _racha)
            else:
                _racha = 0

        _exam_score = {
            'xp': correctas * 50,       # 50 XP planos por correcta, sin multiplicador
            'correct': correctas,
            'total': total,
            'max_streak': _max_racha,
            'max_multiplier': 1,
            'history': [(i, r['correcto']) for i, r in enumerate(resultados)],
        }

        # Preguntas fallidas (solo las que respondió mal, no las vacías)
        _fallidas = [
            {
                "fecha": time.strftime("%d/%m/%Y"),
                "materia": materia,
                "topic": r.get('topic', ''),
                "pregunta": r['pregunta'][:150],
                "respuesta_dada": r.get('seleccionada') or '(sin responder)',
                "respuesta_correcta": r['respuesta_correcta'],
            }
            for r in resultados if not r['correcto']
        ]

        # Stats por tema del examen
        _topic_stats = {}
        for r in resultados:
            _tp = r.get('topic', 'General')
            _cl = f"{materia}::{_tp}"
            if _cl not in _topic_stats:
                _topic_stats[_cl] = {"materia": materia, "topic": _tp, "intentos": 0, "correctas": 0}
            _topic_stats[_cl]["intentos"] += 1
            if r['correcto']:
                _topic_stats[_cl]["correctas"] += 1

        save_session(nombre, _exam_score, materia, materia, "Difícil",
                     preguntas_fallidas=_fallidas, topic_stats_sesion=_topic_stats)
        st.session_state.exam_session_saved = True

    if pct >= 80:
        st.markdown('<div class="confetti">🎉🌟🏆🌟🎉</div>', unsafe_allow_html=True)
        st.balloons()

    st.markdown(f'<div class="hero" style="font-size:2rem;">{info["emoji"]} Resultados del Examen — {materia}</div>', unsafe_allow_html=True)

    score_cls = "score-green" if pct >= 80 else ("score-yellow" if pct >= 60 else "score-red")
    nota_letra = "A" if pct >= 90 else ("B" if pct >= 80 else ("C" if pct >= 70 else ("D" if pct >= 60 else "F")))
    st.markdown(f"""
    <div class="score-box {score_cls}">
        <div class="score-num">{pct}%</div>
        <div style="font-size:1.5rem; font-weight:bold;">Nota: {nota_letra}</div>
        <div style="font-size:1.1rem;">✅ {correctas} correctas &nbsp;|&nbsp; ❌ {total - correctas - vacias} incorrectas &nbsp;|&nbsp; ⬜ {vacias} sin responder</div>
    </div>
    """, unsafe_allow_html=True)

    if pct >= 90:
        st.success(f"🌟 ¡EXCELENTE {nombre}! ¡Dominas esta materia! 🧠✨")
    elif pct >= 80:
        st.success(f"😊 ¡Muy bien {nombre}! Casi perfecto. 💪")
    elif pct >= 60:
        st.warning(f"🤔 Vas bien {nombre}, pero hay preguntas que repasar. 📖")
    else:
        st.error(f"📚 {nombre}, necesitas practicar más. ¡Cada intento te hace mejor! 💪")

    st.write("")
    st.markdown("### 📋 Corrección del Examen")

    for i, r in enumerate(resultados):
        opciones = r['opciones']
        correcta = r['respuesta_correcta']
        seleccionada = r['seleccionada']

        # Identificar letra correcta y letra seleccionada
        letra_correcta = next((LETRAS[j] for j, o in enumerate(opciones) if check_answer({'answer': correcta, 'is_numeric': False}, o)), "?")
        if seleccionada:
            letra_sel = next((LETRAS[j] for j, o in enumerate(opciones) if o == seleccionada), "?")
        else:
            letra_sel = None

        if r['correcto']:
            css_class = "exam-result-correct"
            icono = "✅"
        elif seleccionada is None:
            css_class = "exam-result-empty"
            icono = "⬜"
        else:
            css_class = "exam-result-wrong"
            icono = "❌"

        opciones_html = " &nbsp; ".join(
            f"<b style='color:#28a745;'>[X] {LETRAS[j]}) {o}</b>" if o == correcta else
            (f"<s style='color:#dc3545;'>{LETRAS[j]}) {o}</s>" if o == seleccionada else f"{LETRAS[j]}) {o}")
            for j, o in enumerate(opciones)
        )

        st.markdown(f"""
        <div class="{css_class}">
            <b>{icono} {i+1}. {r['pregunta']}</b><br>
            <span style="font-size:0.9rem;">{opciones_html}</span>
            {"" if r['correcto'] else f"<br><span style='font-size:0.85rem; color:#666;'>Marcaste: <b>{letra_sel}) {seleccionada}</b> &nbsp;→&nbsp; Correcta: <b>{letra_correcta}) {correcta}</b></span>" if seleccionada else f"<br><span style='font-size:0.85rem; color:#666;'>Sin responder. Correcta: <b>{letra_correcta}) {correcta}</b></span>"}
        </div>
        """, unsafe_allow_html=True)

        if r.get('procedure') and not r['correcto']:
            with st.expander(f"📐 Ver explicación — pregunta {i+1}"):
                st.markdown(r['procedure'])

    st.write("")
    r1c1, r1c2, r1c3 = st.columns(3)
    with r1c1:
        if st.button("🔄 Hacer otro examen", type="primary"):
            st.session_state.phase = 'config'
            st.session_state.exam_submitted = False
            st.rerun()
    with r1c2:
        if st.button("📚 Otra materia"):
            st.session_state.phase = 'materias'
            st.rerun()
    with r1c3:
        if st.button("🏠 Inicio"):
            go_home()
            st.rerun()

# ===================== TABLA DE PUNTUACIONES =====================
elif st.session_state.phase == 'leaderboard':
    st.markdown('<div class="hero" style="font-size:2.5rem;">🏆 Tabla de Puntuaciones</div>', unsafe_allow_html=True)
    st.write("")

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
            extras = f"📝 {p['total_respuestas']} preguntas &nbsp;|&nbsp; ✅ {p['pct']}% efectividad &nbsp;|&nbsp; 🔥 Racha: {p['max_racha']} &nbsp;|&nbsp; 🎯 Mejor sesión: {p['mejor_sesion_xp']:,} XP &nbsp;|&nbsp; 🎮 {p['sesiones']} sesiones"
            if mostrar_mult:
                extras += f" &nbsp;|&nbsp; 💪 Mult máx: x{p.get('max_multiplicador', 1)}"
            st.markdown(f"""
            <div class="card" style="border-left: 6px solid {color}; margin: 8px 0;">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
                    <div>
                        <span style="font-size:1.8rem;">{medalla}</span>
                        <span style="font-size:1.3rem; font-weight:bold; margin-left:8px;">{p['nombre']}</span>
                        <span style="margin-left:6px; font-size:1rem;">{logros_icons}</span>
                    </div>
                    <div style="font-size:1.6rem; font-weight:bold; color:{color};">&#11088; {p['xp_total']:,} XP</div>
                </div>
                <div style="margin-top:8px; font-size:0.85rem; color:#555; flex-wrap:wrap;">{extras}</div>
            </div>
            """, unsafe_allow_html=True)

    tab_global, tab_mat, tab_dif, tab_debiles = st.tabs([
        "🌐 Global XP", "📚 Por Materia", "💪 Por Dificultad", "📉 Áreas Débiles"
    ])

    # ── Global ──
    with tab_global:
        _render_ranking(get_ranking())

    # ── Por Materia ──
    with tab_mat:
        mat_sel = st.selectbox("Selecciona la materia:", MATERIAS_ORDEN, key="lb_mat_sel")
        _render_ranking(get_ranking_materia(mat_sel), mostrar_mult=False)

    # ── Por Dificultad ──
    with tab_dif:
        dif_tabs = st.tabs(DIFICULTADES_ORDEN)
        for i, dif in enumerate(DIFICULTADES_ORDEN):
            with dif_tabs[i]:
                _render_ranking(get_ranking_dificultad(dif),
                                mostrar_mult=(dif not in ("💀 Super Difícil", "☠️ Mega Difícil")))

    # ── Áreas Débiles ──
    with tab_debiles:
        st.markdown("### 📉 Temas por mejorar — por estudiante")
        st.caption("Se actualiza al terminar cada sesión de quiz.")
        st.write("")
        for nombre, info in ESTUDIANTES.items():
            temas = get_temas_stats(nombre)
            preguntas = get_preguntas_debiles(nombre)
            if not temas and not preguntas:
                continue
            with st.expander(f"{info['emoji']} {nombre}", expanded=True):
                if temas:
                    # Calcular precisión por tema y ordenar de peor a mejor
                    filas = []
                    for clave, ts in temas.items():
                        intentos = ts["intentos"]
                        correctas = ts["correctas"]
                        pct_t = int(100 * correctas / intentos) if intentos else 0
                        filas.append((ts["materia"], ts["topic"], correctas, intentos, pct_t))
                    filas.sort(key=lambda x: x[4])  # peor primero

                    st.markdown("**Precisión por tema (de menor a mayor):**")
                    for mat_t, topic_t, correctas_t, intentos_t, pct_t in filas:
                        color_b = "#e74c3c" if pct_t < 60 else ("#f39c12" if pct_t < 80 else "#2ecc71")
                        st.markdown(f"""
                        <div style="margin:4px 0;">
                            <span style="font-size:0.85rem; color:#555; min-width:140px; display:inline-block;">
                                <b>{mat_t}</b> › {topic_t}
                            </span>
                            <span style="font-size:0.85rem; font-weight:bold; color:{color_b}; margin-left:8px;">
                                {pct_t}% ({correctas_t}/{intentos_t})
                            </span>
                        </div>
                        """, unsafe_allow_html=True)
                        st.progress(pct_t / 100)

                if preguntas:
                    st.write("")
                    st.markdown("**Últimas preguntas incorrectas:**")
                    for pq in reversed(preguntas[-10:]):  # últimas 10, más reciente primero
                        mat_icon = {"Matemáticas": "🧮", "Ciencias": "🔬",
                                    "Estudios Sociales": "🌍", "Español": "📖"}.get(pq.get("materia", ""), "📝")
                        st.markdown(f"""
                        <div class="result-wrong" style="margin:5px 0; font-size:0.9rem;">
                            {mat_icon} <b>{pq.get('materia','')} › {pq.get('topic','')}</b>
                            &nbsp;<span style="color:#888; font-size:0.8rem;">{pq.get('fecha','')}</span><br>
                            <span style="color:#333;">❓ {pq.get('pregunta','')[:120]}</span><br>
                            <span style="color:#dc3545;">✗ Respondió: <b>{pq.get('respuesta_dada','')[:60]}</b></span>
                            &nbsp;&nbsp;
                            <span style="color:#28a745;">✓ Correcta: <b>{pq.get('respuesta_correcta','')[:60]}</b></span>
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
        go_home()
        st.rerun()
