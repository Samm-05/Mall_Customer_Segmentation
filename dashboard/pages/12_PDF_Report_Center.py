import sys
from pathlib import Path

ROOT_DIR = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
)

sys.path.append(
    str(ROOT_DIR)
)

import streamlit as st

from src.auth_guard import (
    protect_page,
    render_user_panel
)

from src.role_guard import (
    require_admin
)

require_admin()

protect_page()

render_user_panel()

from src.services.analytics_service import (
    get_clustered_data
)

from src.services.report_service import (
    generate_cluster_report
)

from src.executive_insights import (
    generate_insights
)

from src.pdf_generator import (
    generate_executive_pdf
)

st.set_page_config(
    page_title="PDF Report Center",
    layout="wide"
)

st.title(
    "📄 PDF Report Center"
)

st.markdown(
    """
    Generate professional PDF reports
    for customer analytics.
    """
)

df, X, labels = get_clustered_data()

report = generate_cluster_report(
    df
)

insights = generate_insights(
    df
)

if st.button(
    "Generate Executive PDF Report"
):

    pdf_path = generate_executive_pdf(
        df,
        report,
        insights
    )

    st.success(
        "PDF Generated Successfully"
    )

    with open(
        pdf_path,
        "rb"
    ) as pdf_file:

        st.download_button(
            label="Download PDF Report",
            data=pdf_file,
            file_name="Mall_Customer_Report.pdf",
            mime="application/pdf"
        )

st.markdown("---")

st.subheader(
    "Preview Data"
)

st.dataframe(
    report,
    use_container_width=True
)