import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(ROOT_DIR))

import streamlit as st

from src.auth import (
    initialize_auth,
    login
)

st.set_page_config(
    page_title="Login",
    layout="centered"
)

initialize_auth()

st.title(
    "🔐 Mall Customer Analytics Login"
)

username = st.text_input(
    "Username"
)

password = st.text_input(
    "Password",
    type="password"
)

if st.button(
    "Login"
):

    success = login(
        username,
        password
    )

    if success:

        st.success(
            "Login Successful"
        )

        st.switch_page(
            "dashboard/Home.py"
        )

    else:

        st.error(
            "Invalid Credentials"
        )

st.markdown("---")

st.info(
    """
    Demo Credentials

    admin / admin123

    user / user123
    """
)