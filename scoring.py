"""Sistema de puntos, XP y rachas."""

MAX_MULTIPLIER = 4


def new_score():
    return {
        'xp': 0,
        'streak': 0,
        'multiplier': 1,
        'max_streak': 0,
        'max_multiplier': 1,
        'correct': 0,
        'total': 0,
        'history': [],
    }


PENALIDAD = {
    "Fácil":            0,    # sin castigo
    "Normal":          50,    # -50 XP
    "Difícil":         75,    # -75 XP
    "💀 Super Difícil": 100,  # -100 XP
    "☠️ Mega Difícil":  150,  # -150 XP
}

def record_answer(score, pregunta_id, correcto, tiempo_seg=0, timer_total=20, base_xp=100, dificultad="Normal"):
    """
    Registra respuesta y calcula XP ganada.
    - base_xp: 100 puntos base por acierto
    - speed_bonus: hasta +100 extra si responde rápido (proporcional al tiempo restante)
    - multiplier: x1 → x2 → x3 → x4 (máximo), se resetea a x1 si falla
    - XP = (base_xp + speed_bonus) × multiplier
    """
    score['total'] += 1
    if correcto:
        score['correct'] += 1
        score['streak'] += 1

        # Bonus por velocidad: entre 0 y 100 extra
        if timer_total > 0 and tiempo_seg < timer_total:
            speed_bonus = int(100 * (1 - tiempo_seg / timer_total))
        else:
            speed_bonus = 0

        gained = (base_xp + speed_bonus) * score['multiplier']
        score['xp'] += gained

        # Subir multiplicador (máximo x4)
        if score['multiplier'] < MAX_MULTIPLIER:
            score['multiplier'] += 1

        if score['streak'] > score['max_streak']:
            score['max_streak'] = score['streak']
        if score['multiplier'] > score['max_multiplier']:
            score['max_multiplier'] = score['multiplier']
    else:
        penalty = PENALIDAD.get(dificultad, 50)
        score['xp'] = max(0, score['xp'] - penalty)
        gained = -penalty
        score['streak'] = 0
        score['multiplier'] = 1

    score['history'].append((pregunta_id, correcto))
    return gained


def get_level(xp):
    level = 1
    needed = 500
    remaining = xp
    while remaining >= needed:
        remaining -= needed
        level += 1
        needed = int(needed * 1.3)
    return level, remaining, needed


def get_rank(xp):
    level, _, _ = get_level(xp)
    ranks = [
        (1, "🐣 Principiante"),
        (3, "🌱 Aprendiz"),
        (5, "⭐ Estudiante"),
        (8, "🔥 Avanzado"),
        (12, "💎 Experto"),
        (16, "🏆 Maestro"),
        (20, "👑 Leyenda"),
        (25, "🌟 Genio Supremo"),
    ]
    rank = ranks[0][1]
    for min_level, name in ranks:
        if level >= min_level:
            rank = name
    return rank
