from lovepdf.simple_pdf import SimplePdf
from lovepdf.constants import RESOURCES_DIR

import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage python -m lovepdf [pdf_file_name_out]")
        sys.exit(-1)

    file_name_out = sys.argv[1]
    if not file_name_out.endswith(".pdf"):
        file_name_out = "{}.pdf".format(file_name_out)

    # constants
    TEXT = "Hello Envio this PDF is created for you"
    img_path = os.path.join(RESOURCES_DIR, "example.png")

    simple_pdf = SimplePdf(TEXT, img_path)
    simple_pdf.create()
    simple_pdf.save_pdf(file_name_out)
