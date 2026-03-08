from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from io import BytesIO

def generate_project_pdf():
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
    styles = getSampleStyleSheet()
    
    # Custom Styles for a modern look
    styles.add(ParagraphStyle(name='MainTitle', fontSize=24, leading=30, spaceAfter=20, textColor=colors.HexColor("#1A237E"), alignment=1))
    styles.add(ParagraphStyle(name='SubTitle', fontSize=14, leading=18, spaceAfter=12, textColor=colors.grey))

    elements = []

    # --- Header ---
    elements.append(Paragraph("B0Bot Agent Core v0.1.0", styles['MainTitle']))
    elements.append(Paragraph("A Multi-Agent Autonomous Research System", styles['SubTitle']))
    elements.append(Spacer(1, 20))

    # --- Chapter 1: The Vision ---
    elements.append(Paragraph("1. Project Architecture", styles['Heading2']))
    elements.append(Paragraph(
        "B0Bot is designed as a state-driven autonomous agent. Unlike traditional linear programs, "
        "it uses a directed acyclic graph (DAG) to orchestrate tasks between specialized AI nodes.",
        styles['BodyText']
    ))
    elements.append(Spacer(1, 10))

    # --- Chapter 2: Tech Stack Table ---
    elements.append(Paragraph("2. Technical Specifications", styles['Heading2']))
    data = [
        ['Component', 'Technology', 'Role'],
        ['API Layer', 'FastAPI', 'High-speed Async Interface'],
        ['Orchestration', 'LangGraph', 'State Management & Memory'],
        ['Search Engine', 'Tavily AI', 'Optimized Agentic Web Search'],
        ['Language Model', 'OpenAI/Groq', 'Reasoning & Synthesis']
    ]
    t = Table(data, colWidths=[100, 100, 200])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#3F51B5")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    elements.append(t)
    elements.append(Spacer(1, 20))

    # --- Chapter 3: Lines of Code ---
    elements.append(Paragraph("3. Engineering Metrics", styles['Heading2']))
    elements.append(Paragraph("Total Codebase Size: ~130 Lines of Code", styles['BodyText']))
    elements.append(Paragraph("Focus: Modular, scalable, and fail-safe architecture.", styles['BodyText']))

    doc.build(elements)
    buffer.seek(0)
    return buffer