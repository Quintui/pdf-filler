import sys
from fillpdf import fillpdfs

def get_pdf_fields(pdf_path):
    try:
        print(fillpdfs.get_form_fields(pdf_path))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get-pdf-fields.py <pdf_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    get_pdf_fields(pdf_path)