import streamlit as st

# Demo Users
USERS = {
    "admin": {
        "password": "admin123",
        "role": "Admin"
    },
    "user": {
        "password": "user123",
        "role": "User"
    }
}


def initialize_auth():

    if "authenticated" not in st.session_state:

        st.session_state.authenticated = False

    if "username" not in st.session_state:

        st.session_state.username = None

    if "role" not in st.session_state:

        st.session_state.role = None


def login(username, password):

    if username in USERS:

        if USERS[username]["password"] == password:

            st.session_state.authenticated = True

            st.session_state.username = username

            st.session_state.role = USERS[username]["role"]

            return True

    return False


def logout():

    st.session_state.authenticated = False

    st.session_state.username = None

    st.session_state.role = None


def is_authenticated():

    return st.session_state.authenticated