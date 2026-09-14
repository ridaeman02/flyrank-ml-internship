import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, HRFlowable, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_pdf():
    pdf_path = "work/fl03_identity_kit.pdf"
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
        textColor=colors.HexColor('#1e1e1e'),
        spaceAfter=8
    )
    
    code_style = ParagraphStyle(
        'CodeStyle',
        fontName='Courier',
        fontSize=9,
        leading=11,
        textColor=colors.HexColor('#1e1e1e'),
        backColor=colors.HexColor('#fafafa'),
        borderColor=colors.HexColor('#94a3b8'),
        borderWidth=0.5,
        borderPadding=5,
        spaceAfter=8
    )

    story = []

    story.append(Paragraph("Identity Kit (FL-03)", title_style))
    story.append(Paragraph("<b>Author:</b> Rida Eman | <b>Track:</b> AI Fluency (Identity Kit) | <b>Date:</b> 2026-09-12", meta_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#cccccc'), spaceAfter=15))

    # Typography
    story.append(Paragraph("1. Typography", h2_style))
    story.append(Paragraph("<b>Heading Font:</b> JetBrains Mono (gives a crisp, technical ML engineering feel).", body_style))
    story.append(Paragraph("<b>Body Font:</b> Inter (highly legible, neutral, and clean for long-form case studies).", body_style))
    story.append(Spacer(1, 10))

    # Palette
    story.append(Paragraph("2. Palette (The 4-Color Tight Palette)", h2_style))
    
    palette_data = [
        [
            Paragraph("<b>Role</b>", body_style),
            Paragraph("<b>Hex Code</b>", body_style),
            Paragraph("<b>Description</b>", body_style)
        ],
        [
            Paragraph("Background", body_style),
            Paragraph("<code>#FAFAFA</code>", body_style),
            Paragraph("Near-white, soft on the eyes", body_style)
        ],
        [
            Paragraph("Text", body_style),
            Paragraph("<code>#1E1E1E</code>", body_style),
            Paragraph("Near-black, high contrast but not harsh", body_style)
        ],
        [
            Paragraph("Accent", body_style),
            Paragraph("<code>#3B82F6</code>", body_style),
            Paragraph("Slate Blue, used sparingly for links/buttons", body_style)
        ],
        [
            Paragraph("Muted/Borders", body_style),
            Paragraph("<code>#94A3B8</code>", body_style),
            Paragraph("Slate Gray, for subtle dividers", body_style)
        ]
    ]
    t = Table(palette_data, colWidths=[100, 100, 250])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#94a3b8')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t)
    story.append(Spacer(1, 15))

    # Logo / Favicon
    story.append(Paragraph("3. Logo / Favicon", h2_style))
    story.append(Paragraph("I created a clean, simple monogram ('RE' for Rida Eman). It uses a near-black circle background with near-white geometric letters carved out, keeping it entirely aligned with the tight palette.", body_style))
    
    img_path = "work/figures/favicon.png"
    if os.path.exists(img_path):
        img = Image(img_path, width=64, height=64)
        # hack to align left
        t_img = Table([[img]], colWidths=[64])
        t_img.setStyle(TableStyle([
            ('ALIGN', (0,0), (0,0), 'LEFT'),
            ('LEFTPADDING', (0,0), (0,0), 0),
        ]))
        story.append(t_img)
    
    story.append(Spacer(1, 15))

    # Claude Project Style Note
    story.append(Paragraph("4. The Claude Project Style Note", h2_style))
    note = (
        "<b>Style Note:</b> Use 'Inter' for body text and 'JetBrains Mono' for headings. The palette is minimalist: #FAFAFA (bg), #1E1E1E (text), and #3B82F6 (accent).<br/>"
        "<b>Mood:</b> The mood is calm, technical, and highly structured—the design should never compete with the data or the code."
    )
    story.append(Paragraph(note, code_style))

    doc.build(story)
    print(f"Successfully generated PDF: {pdf_path}")

if __name__ == '__main__':
    generate_pdf()
