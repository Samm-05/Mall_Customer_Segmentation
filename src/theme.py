import streamlit as st


def render_kpi(
        title,
        value):

    st.markdown(
        f"""
        <div class="kpi-card">

            <div class="kpi-title">
                {title}
            </div>

            <div class="kpi-value">
                {value}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


def page_header():

    st.markdown(
        """
        <div class="main-header">
            Mall Customer Analytics Platform
        </div>

        <div class="sub-header">
            Customer Segmentation • Business Intelligence • Analytics
        </div>
        """,
        unsafe_allow_html=True
    )