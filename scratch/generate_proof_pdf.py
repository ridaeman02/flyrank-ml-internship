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

    # Changed colors to strict professional grayscale/black (Removed Purple)
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#000000'),
        spaceAfter=4
    )

    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#555555'),
        spaceAfter=10
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#000000'),
        spaceBefore=10,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#222222'),
        spaceAfter=8
    )
    
    bold_body_style = ParagraphStyle(
        'BoldBody',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    story = []

    story.append(Paragraph("What Are You Proving? (Proof Statement)", title_style))
    story.append(Paragraph("<b>Author:</b> Rida Eman | <b>Date:</b> 2026-09-10", meta_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#cccccc'), spaceAfter=8))

    story.append(Paragraph("1. The One-Paragraph Proof Statement", h2_style))
    story.append(Paragraph("<b>The Claim:</b> I build machine learning models that work on real data without leaking future targets.", body_style))
    story.append(Paragraph("<b>The Person:</b> A Lead Data Scientist hiring for an engineering team.", body_style))
    story.append(Paragraph("<b>The Action:</b> Schedule a technical interview with me.", body_style))
    
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>The Unified Statement:</b>", bold_body_style))
    p1 = "My portfolio proves I can build honest machine learning pipelines on messy data. It is written for a Lead Data Scientist so they can review my code and invite me to an interview."
    story.append(Paragraph(p1, body_style))

    story.append(Spacer(1, 15))
    story.append(Paragraph("2. The Honest 'Why'", h2_style))
    p2 = "<b>Why this needs to exist:</b><br/>A resume simply lists Python and SQL as skills. This portfolio proves I can actually process 9 million rows of data and build a model that works on unseen clients."
    story.append(Paragraph(p2, body_style))

    doc.build(story)
    print(f"Successfully generated PDF: {pdf_path}")

if __name__ == '__main__':
    generate_pdf()
