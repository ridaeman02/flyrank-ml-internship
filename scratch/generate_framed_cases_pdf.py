import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_pdf():
    pdf_path = "work/fl02_framed_cases.pdf"
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

    h3_style = ParagraphStyle(
        'SectionH3',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#222222'),
        spaceBefore=6,
        spaceAfter=2
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#222222'),
        spaceAfter=4
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        fontName='Courier-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#000000'),
        backColor=colors.HexColor('#f5f5f5'),
        borderColor=colors.HexColor('#cccccc'),
        borderWidth=0.5,
        borderPadding=5,
        spaceAfter=6
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#222222')
    )

    story = []

    # Header
    story.append(Paragraph("Voice Card & Framed Case Studies (FL-02)", title_style))
    story.append(Paragraph("<b>Author:</b> Rida Eman | <b>Track:</b> AI Fluency (Frame It as Cases) | <b>Repo:</b> github.com/ridaeman02/flyrank-ml-internship", meta_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#cccccc'), spaceAfter=8))

    # Section 1: Voice Card
    story.append(Paragraph("1. Voice Card (Standing Instruction)", h2_style))
    voice_card_text = "Voice Card: Direct, plainspoken, honest, technical, zero buzzwords."
    story.append(Paragraph(voice_card_text, code_style))
    story.append(Paragraph("<b>Standing Instruction for Claude Project:</b><br/>"
                           "<i>\"Write like a real software and machine learning engineer. Be direct, concise, and plainspoken. Never use buzzwords or filler like 'spearheaded', 'game-changer', 'results-driven', 'delve', or 'seamless'. State what was built, the concrete decisions made, and the exact numbers without inflating them. Always use active voice.\"</i>", body_style))
    story.append(Spacer(1, 4))

    # Section 2: Before & After Comparison Table
    story.append(Paragraph("2. Before & After: Generic AI Copy vs. My Edited Version", h2_style))
    
    table_data = [
        [
            Paragraph("<b>Version</b>", table_header_style),
            Paragraph("<b>Copy</b>", table_header_style),
            Paragraph("<b>Why It Changed</b>", table_header_style)
        ],
        [
            Paragraph("<b>Before<br/>(Generic AI)</b>", table_cell_style),
            Paragraph("<i>\"I spearheaded an innovative, cutting-edge machine learning solution leveraging state-of-the-art predictive algorithms on massive big data to seamlessly revolutionize organic search optimization and drive unparalleled traffic growth.\"</i>", table_cell_style),
            Paragraph("Puffed up with meaningless buzzwords ('spearheaded', 'cutting-edge', 'leveraging', 'seamlessly'). Hides what the model actually does.", table_cell_style)
        ],
        [
            Paragraph("<b>After<br/>(My Edited Voice)</b>", table_cell_style),
            Paragraph("<b>\"I built a logistic regression pipeline in DuckDB and scikit-learn that scores decaying search pages across 9.8 million daily rows. Evaluated on unseen client domains, it reached 0.5000 Precision@50, beating FlyRank's fixed heuristic baseline of 0.4200.\"</b>", table_cell_style),
            Paragraph("Direct, grounded, and specific. Names exact tools, dataset size, split design, and empirical test result.", table_cell_style)
        ]
    ]

    t = Table(table_data, colWidths=[70, 260, 210])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#222222')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#fafafa')]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t)
    story.append(Spacer(1, 6))

    # Section 3: Framed Case 1
    story.append(Paragraph("3. Framed Case 1: Content Refresh Opportunity Scoring (Lead Project)", h2_style))
    story.append(Paragraph("<b>Beat 1: The Problem</b>", h3_style))
    story.append(Paragraph("SEO teams manage thousands of published articles. Over time, search traffic decays, but identifying which pages need a rewrite is usually done with blunt rules (e.g. 'any page older than 6 months'). Teams waste hours rewriting pages that would have recovered on their own or miss dying high-traffic pages until it is too late. They needed a model to rank pages by likelihood of continued decline.", body_style))

    story.append(Paragraph("<b>Beat 2: What I Did & Decided</b>", h3_style))
    story.append(Paragraph("• <b>Data Grain & Slicing:</b> Queried 9,841,378 daily performance rows from FlyRank warehouse in DuckDB at content page grain for March 2026.<br/>"
                           "• <b>Strict Leakage Prevention:</b> Isolated feature window (March 1–15) from outcome window (March 16–31). Exposed and removed target-derived leakage trap features that falsely inflated AUC to 0.9991.<br/>"
                           "• <b>Client Normalization:</b> Normalized impressions and clicks within each client to prevent memorizing client traffic scales.<br/>"
                           "• <b>Honest Split Choice:</b> Evaluated on a 75/25 <code>GroupShuffleSplit</code> by <code>client_hash_id</code> to measure generalization to unseen client domains.", body_style))

    story.append(Paragraph("<b>Beat 3: What Came of It</b>", h3_style))
    story.append(Paragraph("• Evaluated on unseen clients, Logistic Regression achieved <b>0.5000 Precision@50</b> vs baseline heuristic of <b>0.4200</b> (+19% relative precision lift).<br/>"
                           "• Built an Action Playbook with transparent reason codes (<code>stale_visible_page</code>, <code>low_ctr_visible_page</code>, <code>model_decline_risk</code>) for human editorial decision support.<br/>"
                           "• Deployed live research paper at <code>https://ridaeman02.github.io/flyrank-ml-internship/</code>.", body_style))
    story.append(Spacer(1, 4))

    # Section 4: Framed Case 2
    story.append(Paragraph("4. Framed Case 2: Leakage-Free Temporal ETL & Contract Verification", h2_style))
    story.append(Paragraph("<b>Beat 1: The Problem:</b> Future observations quietly leak into training features in temporal data, producing models that look great in notebooks but fail in production.<br/>"
                           "<b>Beat 2: What I Did & Decided:</b> Built a pre-flight assertion suite (<code>scripts/verify_data_contract.py</code>) that deterministically blocks execution if target columns leak into feature matrices or null bounds fail.<br/>"
                           "<b>Beat 3: What Came of It:</b> Reduced verification time from 20 minutes of manual inspection to under 1.2 seconds, integrated directly into GitHub Actions CI.", body_style))
    story.append(Spacer(1, 4))

    # Section 5: Bio & CTA
    story.append(Paragraph("5. Bio & Contact Copy (Pointing to the One Action)", h2_style))
    story.append(Paragraph("<b>Bio:</b> Computer Science undergraduate & Machine Learning Intern at FlyRank AI. Working on backend data pipelines (Python, DuckDB, SQL) and applied search ranking models. Focused on building honest models that work on messy real-world data.<br/>"
                           "<b>The One Action:</b> Invite me to a technical interview to discuss how my end-to-end DuckDB and scikit-learn pipeline applies to your data challenges. Contact: <code>ridaeman0002@gmail.com</code> | GitHub: <code>github.com/ridaeman02/flyrank-ml-internship</code>", body_style))

    doc.build(story)
    print(f"Successfully generated PDF: {pdf_path}")

if __name__ == '__main__':
    generate_pdf()
