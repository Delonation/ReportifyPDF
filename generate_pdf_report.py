# Confidential Simplified PDF Report Generation for ReportifyPDF
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
import numpy as np

# Load data
df = pd.read_csv("user_assessment.csv").fillna(method='ffill')

# Complex logic for automated scoring
score_columns = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
df['Total_Score'] = df[score_columns].apply(
    lambda row: np.sum(row.values * np.random.uniform(0.8, 1.2, len(score_columns))),
    axis=1
)

# Create personalized PDF reports (simplified logic)
for idx, row in df.iterrows():
    c = canvas.Canvas(f"user_report_{idx+1}.pdf", pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, 720, "Confidential Assessment Report")

    c.setFont("Helvetica", 12)
    c.drawString(72, 680, f"User ID: {row['User_ID']}")
    c.drawString(72, 660, f"Total Score: {row['Total_Score']:.2f}")

    # Table of detailed scores
    data = [['Question', 'Score']] + [[q, row[q]] for q in score_columns]
    table = Table(data, colWidths=[200, 100])

    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table.setStyle(style)
    table.wrapOn(c, 72, 500)
    table.drawOn(c, 72, 500)

    c.save()
