import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_pdf():
    pdf_path = "work/fl08_future_portfolio_plan.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#1e1b4b'),
        spaceAfter=4
    )

    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#475569'),
        spaceAfter=10
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#4338ca'),
        spaceBefore=10,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#334155'),
        spaceAfter=8
    )

    story = []

    story.append(Paragraph("Send the Link / Habit / Future Cases (FL-08)", title_style))
    story.append(Paragraph("<b>Author:</b> Rida Eman (CS Senior & ML Intern) | <b>Track:</b> AI Fluency (Send the Link) | <b>Date:</b> 2026-09-09", meta_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#6366f1'), spaceAfter=8))

    story.append(Paragraph("1. How to Add the Next Case (The Protocol)", h2_style))
    p1 = (
        "To prevent my portfolio from going stale, every new case study will follow the 'Three-Beat Shape' directly in my Claude Project:<br/><br/>"
        "1. <b>Problem</b>: What was the business or technical friction? <i>(e.g., Data pipelines were timing out due to memory limits.)</i><br/>"
        "2. <b>What I Did</b>: The specific engineering or modeling action taken. <i>(e.g., Re-wrote the extraction layer in DuckDB to stream parquet partitions.)</i><br/>"
        "3. <b>What Came of It</b>: The quantitative, honest result. <i>(e.g., Pipeline runtime dropped from 4 hours to 12 minutes with zero data leakage.)</i><br/><br/>"
        "<b>The Process Habit:</b><br/>"
        "1. Open my existing <code>FlyRank ML Portfolio & Research Showcase</code> Claude Project.<br/>"
        "2. Paste raw notes, code snippets, or metric screenshots into a prompt.<br/>"
        "3. Ask Claude: <i>'Draft a new case study section using the Three-Beat Shape based on these raw notes. Keep the tone direct, factual, and aligned with my identity kit.'</i><br/>"
        "4. Append the generated markdown directly to <code>docs/index.html</code> under a new Case Study block."
    )
    story.append(Paragraph(p1, body_style))

    story.append(Paragraph("2. The Next Real Piece of Work", h2_style))
    p2 = (
        "<b>Project Name:</b> Automated Model Drift Monitoring Dashboard<br/>"
        "<b>Description:</b> I am currently building a serverless Python script that checks our live model endpoints every 24 hours to detect concept drift in search volume features. Once deployed, this will be my second major portfolio piece, demonstrating MLOps monitoring and production reliability."
    )
    story.append(Paragraph(p2, body_style))

    story.append(Paragraph("3. Reminder Evidence", h2_style))
    p3 = (
        "I have set a recurring calendar event to enforce this habit.<br/><br/>"
        "<b>Event Title:</b> Portfolio Audit & Next Case Sync<br/>"
        "<b>Frequency:</b> Every 6 weeks<br/>"
        "<b>Action:</b> Check if a new project has shipped. If yes, dump notes into Claude Project and update the live portfolio."
    )
    story.append(Paragraph(p3, body_style))
    story.append(Spacer(1, 10))

    img_path = "work/figures/calendar_reminder.png"
    if os.path.exists(img_path):
        img = Image(img_path, width=450, height=187)
        story.append(img)
        story.append(Spacer(1, 5))
        story.append(Paragraph("<font size=8 color='#64748b'>Figure 1: Screenshot evidence of recurring calendar reminder to update the portfolio via Claude Project.</font>", body_style))

    doc.build(story)
    print(f"Successfully generated PDF: {pdf_path}")

if __name__ == '__main__':
    generate_pdf()
