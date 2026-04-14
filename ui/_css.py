"""CSS global de la aplicación."""

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Nunito:wght@400;700&display=swap');
.main { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
.block-container { max-width: 800px; padding-left: 1rem !important; padding-right: 1rem !important; }
h1, h2, h3 { font-family: 'Fredoka One', cursive !important; }
p, li, label, .stMarkdown { font-family: 'Nunito', sans-serif !important; }

.card { background: white; border-radius: 20px; padding: 25px; margin: 15px 0; box-shadow: 0 8px 25px rgba(0,0,0,0.15); color: #2c3e50; }
.card-purple { border-left: 6px solid #9b59b6; }
.card-blue   { border-left: 6px solid #3498db; }
.card-green  { border-left: 6px solid #2ecc71; }
.card-orange { border-left: 6px solid #f39c12; }
.card-red    { border-left: 6px solid #e74c3c; }

.hero { text-align: center; padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 50%, #ffd200 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 3.5rem; font-family: 'Fredoka One', cursive; margin-bottom: 0; }
.hero-sub { text-align: center; font-size: 1.3rem; color: #ddd; margin-top: 0; }

.score-box { text-align: center; padding: 30px; border-radius: 20px; margin: 20px 0; color: #2c3e50; }
.score-green  { background: linear-gradient(135deg, #a8edea, #fed6e3); }
.score-yellow { background: linear-gradient(135deg, #ffecd2, #fcb69f); }
.score-red    { background: linear-gradient(135deg, #ff9a9e, #fecfef); }
.score-num { font-size: 4rem; font-weight: bold; font-family: 'Fredoka One', cursive; }

.kahoot-q { background: linear-gradient(135deg, #6c5ce7, #a29bfe); color: white; padding: 30px; border-radius: 20px; text-align: center; font-size: 1.4rem; font-weight: bold; margin: 15px 0; box-shadow: 0 5px 20px rgba(108,92,231,0.4); }

.timer { text-align: center; font-size: 2.5rem; font-family: 'Fredoka One', cursive; }
.timer-ok     { color: #2ecc71; }
.timer-warn   { color: #f39c12; }
.timer-danger { color: #e74c3c; animation: pulse 0.5s infinite; }
@keyframes pulse { 0%,100% { opacity:1; } 50% { opacity:0.5; } }

.badge { display: inline-block; padding: 5px 15px; border-radius: 20px; font-size: 0.85rem; font-weight: bold; color: white; margin-bottom: 10px; }
.badge-1 { background: #e74c3c; } .badge-2 { background: #3498db; } .badge-3 { background: #2ecc71; }
.badge-4 { background: #f39c12; } .badge-5 { background: #9b59b6; } .badge-6 { background: #1abc9c; } .badge-7 { background: #e67e22; }

div.stButton > button { border-radius: 15px !important; font-family: 'Nunito', sans-serif !important; font-weight: 700 !important; font-size: 1rem !important; padding: 10px 20px !important; transition: transform 0.2s !important; min-height: 48px !important; }
div.stButton > button:hover { transform: scale(1.05) !important; }

.result-correct { background: #d4edda; border-left: 5px solid #28a745; padding: 10px 15px; border-radius: 10px; margin: 5px 0; color: #155724; }
.result-wrong   { background: #f8d7da; border-left: 5px solid #dc3545; padding: 10px 15px; border-radius: 10px; margin: 5px 0; color: #721c24; }

.confetti { text-align: center; font-size: 3rem; animation: bounce 1s infinite; }
@keyframes bounce { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-20px); } }

.student-card { text-align: center; padding: 30px 15px; border-radius: 25px; cursor: pointer; transition: transform 0.3s; min-height: 180px; }
.student-card:hover { transform: scale(1.05); }

.stImage img { max-height: 300px !important; object-fit: contain !important; margin: 0 auto !important; display: block !important; }

.quiz-stats { display: flex; flex-wrap: wrap; gap: 6px; justify-content: center; background: white; border-radius: 15px; padding: 10px 12px; margin-bottom: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); color: #2c3e50; }
.quiz-stats span { font-family: 'Nunito', sans-serif; font-size: 0.9rem; font-weight: 700; padding: 4px 10px; background: #f4f4f8; border-radius: 20px; color: #333; white-space: nowrap; }

.stats-row { display: flex; gap: 10px; margin: 15px 0; flex-wrap: wrap; }
.stat-item { flex: 1 1 80px; text-align: center; padding: 15px 10px; border-radius: 15px; background: white; box-shadow: 0 4px 12px rgba(0,0,0,0.1); color: #2c3e50; }
.stat-item h3 { font-family: 'Fredoka One', cursive; font-size: 1.6rem; margin: 0 0 4px 0; color: inherit; }
.stat-item p  { font-size: 0.8rem; color: #666; margin: 0; font-family: 'Nunito', sans-serif; }
.stat-orange { border-top: 5px solid #f39c12; }
.stat-purple { border-top: 5px solid #9b59b6; }
.stat-blue   { border-top: 5px solid #3498db; }

#MainMenu { visibility: hidden !important; }
header[data-testid="stHeader"] { visibility: hidden !important; }
footer { visibility: hidden !important; }
[data-testid="stToolbar"]      { display: none !important; }
[data-testid="stDecoration"]   { display: none !important; }
[data-testid="stStatusWidget"] { display: none !important; }

.exam-header { background: white; border-radius: 20px; padding: 20px 25px; margin-bottom: 18px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 6px solid #2c3e50; color: #2c3e50; }
.exam-header h2 { font-family: 'Fredoka One', cursive; color: #2c3e50; margin: 0 0 4px 0; font-size: 1.6rem; }
.exam-header p  { color: #555; margin: 0; font-size: 0.95rem; font-family: 'Nunito', sans-serif; }
.exam-instrucciones { background: #fff9e6; border: 2px dashed #f39c12; border-radius: 12px; padding: 12px 18px; margin-bottom: 18px; font-family: 'Nunito', sans-serif; font-size: 0.95rem; color: #7d6608; }
.exam-pregunta { background: white; border-radius: 15px; padding: 20px 22px; margin: 12px 0; box-shadow: 0 3px 12px rgba(0,0,0,0.08); border-left: 5px solid #6c5ce7; color: #2c3e50; }
.exam-pregunta .num   { font-family: 'Fredoka One', cursive; color: #6c5ce7; font-size: 1.1rem; }
.exam-pregunta .texto { font-family: 'Nunito', sans-serif; font-size: 1.05rem; font-weight: 700; color: #2c3e50; margin: 6px 0 14px 0; }
.exam-result-correct { background: #d4edda; border-left: 5px solid #28a745; padding: 12px 16px; border-radius: 10px; margin: 5px 0; font-family: 'Nunito', sans-serif; color: #155724; }
.exam-result-wrong   { background: #f8d7da; border-left: 5px solid #dc3545; padding: 12px 16px; border-radius: 10px; margin: 5px 0; font-family: 'Nunito', sans-serif; color: #721c24; }
.exam-result-empty   { background: #fff3cd; border-left: 5px solid #ffc107; padding: 12px 16px; border-radius: 10px; margin: 5px 0; font-family: 'Nunito', sans-serif; color: #856404; }

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
"""
