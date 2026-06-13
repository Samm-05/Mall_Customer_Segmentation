import sys
from pathlib import Path

ROOT_DIR = (
    Path(__file__).resolve()
    .parent.parent.parent
)

sys.path.append(
    str(ROOT_DIR)
)

import streamlit as st
import pandas as pd
from io import BytesIO

from src.services.analytics_service import (
    get_clustered_data
)


from src.auth_guard import (
    protect_page,
    render_user_panel
)

protect_page()

render_user_panel()

st.title(
    "Report Center"
)

df, X, labels = get_clustered_data()

csv = df.to_csv(
    index=False
)

st.download_button(
    "Download CSV",
    csv,
    "customer_segments.csv",
    "text/csv"
)

buffer = BytesIO()

with pd.ExcelWriter(
    buffer,
    engine="openpyxl"
) as writer:

    df.to_excel(
        writer,
        index=False
    )

st.download_button(
    "Download Excel",
    buffer.getvalue(),
    "customer_segments.xlsx"
)

st.dataframe(
    df.head(25)
)