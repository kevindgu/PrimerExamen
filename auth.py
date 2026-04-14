"""Sistema de autenticación por PIN."""
import streamlit as st


def get_pins() -> dict:
    """Lee los PINs desde secrets."""
    try:
        return dict(st.secrets.get("pins", {}))
    except Exception:
        return {}


def get_admin_pin() -> str:
    """Lee el PIN de administrador desde secrets."""
    try:
        return str(st.secrets.get("ADMIN_PIN", "9999"))
    except Exception:
        return "9999"


def is_authenticated(nombre: str) -> bool:
    return st.session_state.get(f"auth_{nombre}", False)


def logout(nombre: str):
    st.session_state.pop(f"auth_{nombre}", None)


def render_pin_screen(nombre: str, info: dict, lang: str = "es") -> bool:
    from i18n import t
    if is_authenticated(nombre):
        return True

    st.markdown(f"""
    <div style="text-align:center; padding: 20px;">
        <div style="font-size:5rem;">{info['emoji']}</div>
        <h2 style="font-family:'Fredoka One',cursive; color:white; font-size:2.5rem; margin:10px 0;">
            {t('pin_title', lang, nombre=nombre)}
        </h2>
        <p style="color:#ddd; font-size:1.1rem;">{t('pin_sub', lang)}</p>
    </div>
    """, unsafe_allow_html=True)

    intentos = st.session_state.get(f"pin_intentos_{nombre}", 0)
    if intentos > 0:
        st.error(t('pin_wrong', lang, n=intentos))
    if intentos >= 3:
        st.error(t('pin_locked', lang))
        if st.button(t('pin_retry', lang), use_container_width=True):
            st.session_state[f"pin_intentos_{nombre}"] = 0
            st.rerun()
        return False

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        pin_input = st.text_input(
            "PIN:", type="password", max_chars=4,
            placeholder=t('pin_placeholder', lang),
            key=f"pin_input_{nombre}",
            label_visibility="collapsed"
        )
        st.markdown(f"<p style='text-align:center; color:#aaa; font-size:0.85rem;'>{t('pin_digits', lang)}</p>",
                    unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button(t('pin_back', lang), use_container_width=True):
                st.session_state.phase = 'students'
                st.session_state.pop(f"pin_intentos_{nombre}", None)
                st.session_state.student = None
                st.rerun()
        with col_b:
            entrar = st.button(t('pin_enter', lang), type="primary", use_container_width=True)

    if entrar or (pin_input and len(pin_input) == 4):
        pins = get_pins()
        if pin_input == pins.get(nombre, ""):
            st.session_state[f"auth_{nombre}"] = True
            st.session_state.pop(f"pin_intentos_{nombre}", None)
            st.rerun()
            return True
        elif len(pin_input) == 4:
            st.session_state[f"pin_intentos_{nombre}"] = intentos + 1
            st.rerun()
    return False
