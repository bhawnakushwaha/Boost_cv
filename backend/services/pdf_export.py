# import io
# import logging

# try:
#     from weasyprint import HTML, CSS
#     WEASYPRINT_INSTALLED = True
# except ImportError:
#     WEASYPRINT_INSTALLED = False

# logger = logging.getLogger('ats_resume_scorer')

# def generate_combined_pdf(html_docs: dict[str, str]) -> bytes:
#     if not WEASYPRINT_INSTALLED:
#         raise ImportError("WeasyPrint is not installed. PDF generation unavailable.")
        
#     documents = []
    
#     # Render all 3 HTML strings to WeasyPrint Document objects
#     for name, html_str in html_docs.items():
#         doc = HTML(string=html_str).render()
#         documents.append(doc)
    
#     # Merge them into the first document
#     first_doc = documents[0]
#     for other_doc in documents[1:]:
#         for page in other_doc.pages:
#             first_doc.pages.append(page)
            
#     # Write combined PDF bytes
#     pdf_bytes = first_doc.write_pdf()
#     return pdf_bytes

# import io
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.platypus import (
#     SimpleDocTemplate,
#     Paragraph,
#     Spacer,
#     PageBreak,
# )



import io
import logging

from xhtml2pdf import pisa

logger = logging.getLogger("ats_resume_scorer")


def generate_combined_pdf(html_docs: dict[str, str]) -> bytes:

    page_break = """
    <div style="page-break-after: always;"></div>
    """

    html = page_break.join(html_docs.values())

    pdf_buffer = io.BytesIO()

    status = pisa.CreatePDF(
        src=html,
        dest=pdf_buffer,
        encoding="utf-8",
    )

    if status.err:
        raise Exception("Failed to generate PDF")

    return pdf_buffer.getvalue()

