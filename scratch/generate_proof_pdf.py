import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_pdf():
    pdf_path = "work/fl01_proof_statement.pdf"
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
    
    bold_body_style = ParagraphStyle(
        'BoldBody',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    story = []

    story.append(Paragraph("What Are You Proving? (Proof Statement)", title_style))
    story.append(Paragraph("<b>Author:</b> Rida Eman (CS Senior & ML Intern) | <b>Track:</b> AI Fluency (What Are You Proving) | <b>Date:</b> 2026-09-09", meta_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#6366f1'), spaceAfter=8))

    story.append(Paragraph("1. The One-Paragraph Proof Statement", h2_style))
    story.append(Paragraph("<b>The Claim:</b> I build production-ready machine learning models that extract reliable signals from messy, real-world data while strictly guarding against target leakage.", body_style))
    story.append(Paragraph("<b>The Person:</b> A Senior ML Engineering Manager or Lead Data Scientist who is exhausted by academic prototypes and needs someone who understands honest holdout splits and robust data pipelines.", body_style))
    story.append(Paragraph("<b>The Action:</b> I want them to schedule a technical interview to discuss how my end-to-end DuckDB and scikit-learn pipeline could be applied to their business problems.", body_style))
    
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>The Unified Statement:</b>", bold_body_style))
    p1 = "My portfolio proves that I can build production-ready machine learning pipelines that extract reliable signals from messy data while strictly guarding against target leakage, aimed directly at a Senior ML Engineering Manager who needs useful, honest prototypes rather than academic demos, so that they feel completely confident scheduling a technical interview with me."
    story.append(Paragraph(p1, body_style))

    story.append(Spacer(1, 15))
    story.append(Paragraph("2. The Honest 'Why'", h2_style))
    p2 = "<b>Why this needs to exist:</b><br/>A standard CV or LinkedIn profile claims that I 'know Python, SQL, and Machine Learning'; this portfolio actually proves it by showing my exact methodology for handling a 9.8M-row DuckDB dataset, enforcing zero-leakage client holdout splits, and deploying a verifiable model."
    story.append(Paragraph(p2, body_style))

    doc.build(story)
    print(f"Successfully generated PDF: {pdf_path}")

if __name__ == '__main__':
    generate_pdf()
