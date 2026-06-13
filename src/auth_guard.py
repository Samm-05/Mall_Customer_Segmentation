import streamlit as st

from src.auth import (
    initialize_auth,
    is_authenticated,
    logout
)


def protect_page():

    initialize_auth()

    if not is_authenticated():

        st.warning(
            "Please login first."
        )

        st.switch_page(
            "dashboard/Login.py"
        )

        st.stop()


def render_user_panel():

    st.sidebar.markdown("---")

    st.sidebar.success(
        f"Logged in as: "
        f"{st.session_state.username}"
    )

    st.sidebar.info(
        f"Role: "
        f"{st.session_state.role}"
    )

    if st.sidebar.button(
        "Logout"
    ):

        logout()

        st.switch_page(
            "dashboard/Login.py"
        )