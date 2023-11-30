import sys
from fillpdf import fillpdfs

def set_pdf_fields(pdf_template, output_pdf, field_values):
    try:
        fillpdfs.write_fillable_pdf(pdf_template, output_pdf, field_values)
        print(f"PDF fields set successfully. Output PDF: {output_pdf}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python set-pdf-fields.py <original_pdf_with_form> <output_pdf> <field1=value1> <field2=value2> ...")

        sys.exit(1)

    pdf_template = sys.argv[1]
    output_pdf = sys.argv[2]

    field_values = {}
    for arg in sys.argv[3:]:
        field, value = arg.split('=')
        field_values[field] = value

    set_pdf_fields(pdf_template, output_pdf, field_values)