from fpdf import FPDF
from datetime import datetime
import os

def generate_daily_pdf_report(logo_path="data/logo.png"):
    os.makedirs("data/reports", exist_ok=True)
    filename = f"data/reports/report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
    pdf = FPDF()
    pdf.add_page()

    if os.path.exists(logo_path):
        pdf.image(logo_path, 10, 8, 33)
    pdf.set_font("Arial", "B", 16)
    pdf.cell(80)
    pdf.cell(30, 10, "Tagesabschluss-Bericht", 0, 1, "C")
    pdf.ln(20)

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Datum: {datetime.now().strftime('%d.%m.%Y')}", 0, 1)
    pdf.cell(0, 10, "Automatisch generierter Bericht", 0, 1)
    pdf.output(filename)
    return filename
