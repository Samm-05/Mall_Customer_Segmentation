import streamlit as st


def require_admin():

    if (
        st.session_state.role
        != "Admin"
    ):

        st.error(
            "Admin Access Required"
        )

        st.stop()