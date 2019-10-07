from lovepdf.simple_pdf import SimplePdf
from lovepdf.constants import RESOURCES_DIR

import sys
import os
import json

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage python -m lovepdf [config_file_path]")
        sys.exit(-1)

    if not os.path.isfile(sys.argv[1]):
        print("File {} doesn't exist".format(sys.argv[1]))
        sys.exit(-1)

    with open(sys.argv[1], 'r') as f:
        data = json.load(f)
        data = json.loads(data)

    file_name_out = data['file_name']
    if not file_name_out.endswith(".pdf"):
        file_name_out = "{}.pdf".format(file_name_out)

    # constants
    TEXT = "Hello Envio this PDF is created for you"
    img_path = os.path.join(RESOURCES_DIR, data['image_name'])
    if not os.path.isfile(img_path):
        print("No image with this name '{}' into the resources directory".format(data['image_name']))
        sys.exit(-1)

    simple_pdf = SimplePdf(data['txt'], img_path)
    simple_pdf.create()
    simple_pdf.save_pdf(file_name_out)
