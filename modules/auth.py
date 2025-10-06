import streamlit as st

def authenticate(password_env):
    st.sidebar.header("🔐 Login")
    pw_input = st.sidebar.text_input("Passwort", type="password")
    if st.sidebar.button("Anmelden"):
        if pw_input == password_env:
            st.session_state["auth"] = True
            st.success("✅ Authentifizierung erfolgreich")
        else:
            st.error("❌ Falsches Passwort")
    return st.session_state.get("auth", False)
