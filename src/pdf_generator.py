from pathlib import Path
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

REPORT_DIR = (
    Path("reports")
    / "generated_reports"
)

REPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def generate_executive_pdf(
        df,
        cluster_report,
        insights):

    pdf_path = (
        REPORT_DIR /
        "executive_report.pdf"
    )

    doc = SimpleDocTemplate(
        str(pdf_path)
    )

    styles = getSampleStyleSheet()

    content = []

    # ==================================
    # TITLE
    # ==================================

    content.append(
        Paragraph(
            "Mall Customer Analytics Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(
            1,
            20
        )
    )

    # ==================================
    # DATASET SUMMARY
    # ==================================

    content.append(
        Paragraph(
            "Dataset Summary",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            f"Total Customers: {len(df)}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Average Age: {df['Age'].mean():.2f}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Average Income: {df['Annual Income (k$)'].mean():.2f}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Average Spending: {df['Spending Score (1-100)'].mean():.2f}",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(
            1,
            20
        )
    )

    # ==================================
    # CLUSTER SUMMARY
    # ==================================

    content.append(
        Paragraph(
            "Cluster Analysis",
            styles["Heading1"]
        )
    )

    for cluster in cluster_report.index:

        row = cluster_report.loc[
            cluster
        ]

        content.append(
            Paragraph(
                f"Cluster {cluster}",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                f"Average Age: {row['Age']:.2f}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"Average Income: "
                f"{row['Annual Income (k$)']:.2f}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"Average Spending: "
                f"{row['Spending Score (1-100)']:.2f}",
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(
                1,
                10
            )
        )

    content.append(
        PageBreak()
    )

    # ==================================
    # EXECUTIVE INSIGHTS
    # ==================================

    content.append(
        Paragraph(
            "Executive Insights",
            styles["Heading1"]
        )
    )

    for insight in insights:

        content.append(
            Paragraph(
                f"• {insight}",
                styles["BodyText"]
            )
        )

    doc.build(content)

    return pdf_path