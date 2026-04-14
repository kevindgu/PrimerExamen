"""MatePlay — Router principal."""
import streamlit as st
import streamlit.components.v1 as components

from ui._css import CSS
from musica import MUSIC_HTML
from _pages._students import render as render_students
from _pages._materias import render as render_materias
from _pages._config import render as render_config
from _pages._quiz import render as render_quiz
from _pages._results import render as render_results
from _pages._exam import (render_exam, render_exam_results,
                         render_exam_correction, render_exam_correction_done)
from _pages._leaderboard import render as render_leaderboard

st.set_page_config(page_title="🧮 MatePlay", page_icon="🧮", layout="centered")
st.markdown(CSS, unsafe_allow_html=True)

# ── Estado inicial ────────────────────────────────────────────
if 'phase' not in st.session_state:
    st.session_state.update({
        'phase': 'students', 'student': None, 'materia': None,
        'music_on': False, 'last_spoken_qid': None,
        'speak_counter': 0, 'force_speak': False,
    })
if 'music_on' not in st.session_state:
    st.session_state.music_on = False

# ── Música global ─────────────────────────────────────────────
if st.session_state.music_on:
    components.html(MUSIC_HTML, height=0)

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


# ── Router ────────────────────────────────────────────────────
phase = st.session_state.phase

if phase == 'students':
    render_students(go_home)
elif phase == 'materias':
    render_materias(go_home)
elif phase in ('menu', 'config'):
    render_config()
elif phase == 'quiz':
    render_quiz()
elif phase == 'results':
    render_results(go_home)
elif phase == 'exam':
    render_exam()
elif phase == 'exam_results':
    render_exam_results(go_home)
elif phase == 'exam_correction':
    render_exam_correction()
elif phase == 'exam_correction_done':
    render_exam_correction_done(go_home)
elif phase == 'leaderboard':
    render_leaderboard(go_home)
