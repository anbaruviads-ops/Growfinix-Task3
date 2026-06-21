from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(
    username,
    mbti,
    recommendation
):

    file_path = f"reports/{username}.pdf"

    pdf = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Career Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1,12)
    )

    elements.append(
        Paragraph(
            f"MBTI: {mbti}",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1,12)
    )

    elements.append(
        Paragraph(
            recommendation,
            styles["Normal"]
        )
    )

    pdf.build(elements)

    return file_path