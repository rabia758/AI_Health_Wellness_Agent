from fpdf import FPDF
from io import BytesIO

def generate_pdf(context):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(40, 10, f"Health Report for {context.name}")

    pdf.set_font("Arial", '', 12)
    pdf.ln(10)
    pdf.multi_cell(0, 10, f"Goals: {context.goal}")
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Diet Preferences: {context.diet_preferences}")
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Workout Plan: {context.workout_plan}")
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Meal Plan: {context.meal_plan}")
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Progress Logs: {context.progress_logs}")
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Handoff Logs: {context.handoff_logs}")

    buffer = BytesIO()
    pdf.output(buffer)
    pdf_bytes = buffer.getvalue()
    buffer.close()
    return pdf_bytes
