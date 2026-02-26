from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem,
    Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
import os


def generate_pdf(result: dict, file_path: str):

    doc = SimpleDocTemplate(file_path, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    title_style = styles["Heading1"]
    section_style = styles["Heading2"]
    normal_style = styles["BodyText"]

    idea = result["idea"]
    analysis = result["analysis"]

    # Title
    elements.append(Paragraph("Startup Analysis Report", title_style))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph(f"<b>Idea:</b> {idea}", section_style))
    elements.append(Spacer(1, 0.3 * inch))

    # Research
    research = analysis.get("research", {})
    elements.append(Paragraph("Market Research", section_style))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph(f"<b>Market Size:</b> {research.get('market_size', 'N/A')}", normal_style))
    elements.append(Paragraph(f"<b>Growth Rate:</b> {research.get('growth_rate', 'N/A')}", normal_style))
    elements.append(Spacer(1, 0.2 * inch))

    trends = research.get("key_trends", [])
    if trends:
        elements.append(Paragraph("<b>Key Trends:</b>", normal_style))
        elements.append(Spacer(1, 0.1 * inch))

        trend_items = []
        for t in trends:
            name = t.get("name", "")
            desc = t.get("description", "")
            trend_items.append(
                ListItem(Paragraph(f"{name}: {desc}", normal_style))
            )

        elements.append(ListFlowable(trend_items, bulletType='bullet'))
        elements.append(Spacer(1, 0.3 * inch))

    # Strategy (raw text support)
    strategy = analysis.get("strategy", {})
    elements.append(Paragraph("Business Strategy", section_style))
    elements.append(Spacer(1, 0.2 * inch))

    if isinstance(strategy, dict) and "raw_strategy" in strategy:
        elements.append(Paragraph(strategy["raw_strategy"].replace("\n", "<br/>"), normal_style))
    else:
        elements.append(Paragraph(str(strategy), normal_style))

    elements.append(Spacer(1, 0.3 * inch))

    # Finance
    finance = analysis.get("finance", {})
    revenue = finance.get("12_month_revenue_projection", [])

    if revenue:
        elements.append(Paragraph("12 Month Revenue Projection", section_style))
        elements.append(Spacer(1, 0.2 * inch))

        table_data = [["Month", "Revenue"]]
        for i, rev in enumerate(revenue):
            table_data.append([f"Month {i+1}", f"{rev:,.2f}"])

        table = Table(table_data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
            ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ]))

        elements.append(table)
        elements.append(Spacer(1, 0.3 * inch))

    # Critic
    critic = analysis.get("critic", {})
    elements.append(Paragraph("Evaluation Summary", section_style))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph(f"Critic Score: {critic.get('score', 'N/A')}", normal_style))
    elements.append(Paragraph(f"Feedback: {critic.get('feedback', 'N/A')}", normal_style))

    doc.build(elements)

    return file_path